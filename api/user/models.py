from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password, check_password as django_check_password
# from masters.models import MstDepartments,MstUserDesignation,MstCreditOfficerLevels,MstLanguages
from utils.management.file_rename import upload_to_user_profile_pic

YES_NO = (('Y', 'Yes'), ('N', 'No'))
GENDER = (('M','Male'), ('F','Female'), ('O','Other'), ('N/A','Not Applicable'))
REC_STATUS = (('A','Active'), ('N','New'), ('M','Modified'), ('R','Rejected'), ('C','Closed'), ('X','Cancelled'))

class SecUserManager(BaseUserManager):

    def create_user(self, txt_login_id, password=None, **extra_fields):
        if not txt_login_id:
            raise ValueError("The login id must be set")

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)

        user = self.model(txt_login_id=txt_login_id, **extra_fields)

        if password:
            user.set_password(password)
        else:
            # IMPORTANT: allows first save during createsuperuser
            user.set_unusable_password()

        user.save(using=self._db)
        return user

    def create_superuser(self, txt_login_id, password=None, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        extra_fields['is_active'] = True

        return self.create_user(txt_login_id, password, **extra_fields)





class SecUserMaster(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)

    # Required fields
    txt_login_id = models.CharField(max_length=48, unique=True, db_index=True)
    password = models.CharField(
    max_length=128,
    db_column="txt_user_signature"
    )
    # Optional fields
    flg_functional_id = models.CharField(max_length=1, choices=YES_NO, default='N', null=True, blank=True)
    flg_force_passwd_chg = models.CharField(max_length=1, choices=YES_NO, null=True, blank=True)
    dat_last_passwd_chg = models.DateField(null=True, blank=True)

    txt_user_fname = models.CharField(max_length=48, null=True, blank=True)
    txt_user_mname = models.CharField(max_length=48, null=True, blank=True)
    txt_user_lname = models.CharField(max_length=48, null=True, blank=True)

    enu_user_gender = models.CharField(max_length=4, choices=GENDER, null=True, blank=True)
    dat_user_birth = models.DateField(null=True, blank=True)

    id_parent_company_3rdparty = models.ForeignKey('campaign.MstThirdParties',null=True,blank=True,related_name='user_master',on_delete=models.DO_NOTHING)
    txt_parent_company_name = models.CharField(max_length=48, null=True, blank=True)
    flg_parent_company_verified = models.CharField(max_length=1, choices=YES_NO, default='N', null=True, blank=True)
    dat_time_parent_company_verified = models.DateTimeField(null=True, blank=True)
    txt_parent_company_verified_by = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True,related_name='verified_parent_company')

    is_superuser = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False, null=True, blank=True)
    is_enduser = models.BooleanField(default=False, null=True, blank=True)
    is_client = models.BooleanField(default=False, null=True, blank=True)
    is_verified = models.BooleanField(default=False, null=True, blank=True)
    is_pass_changed = models.BooleanField(default=False, null=True, blank=True)
    is_2fa = models.BooleanField(default=False, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    txt_employee_id = models.CharField(max_length=48, null=True, blank=True)
    # cod_language = models.CharField(max_length=4, default='ENG', null=True, blank=True)
    cod_language=models.ForeignKey('masters.MstLanguages',on_delete=models.SET_NULL,null=True,blank=True,related_name='user_master_language')
    txt_user_email_id = models.CharField(max_length=96, null=True, blank=True)
    txt_user_mobile_phone = models.CharField(max_length=48, null=True, blank=True)

    txt_device_assigned = models.CharField(max_length=96, null=True, blank=True)
    txt_fcm_token = models.TextField(null=True, blank=True)
    dat_time_fcm_expiry = models.DateTimeField(null=True, blank=True)

    cod_home_module = models.ForeignKey(
    'masters.SysInstallModule',   
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='home_module_users'
)
    cod_home_menu = models.OneToOneField('masters.SecMenuOptions',null=True,blank=True,on_delete=models.SET_NULL,related_name='user_home_menu')

    dat_time_t_and_c_accepted = models.DateTimeField(null=True, blank=True)
    dat_time_welcome_dismissed = models.DateTimeField( null=True, blank=True)

    # cod_department = models.CharField(max_length=4, null=True, blank=True)
    cod_department=models.ForeignKey('masters.MstDepartments',on_delete=models.SET_NULL,null=True,blank=True,related_name='user_master_department')
    # cod_user_designation = models.CharField(max_length=4, null=True, blank=True)
    cod_user_designation=models.ForeignKey('masters.MstUserDesignation',on_delete=models.SET_NULL,null=True,blank=True,related_name='user_master_designation')
    # cod_credit_officer_level = models.CharField(max_length=4, null=True, blank=True)
    cod_credit_officer_level=models.ForeignKey('masters.MstCreditOfficerLevels',on_delete=models.SET_NULL,null=True,blank=True,related_name='user_master_credit_officer')

    # txt_manager_login_id = models.CharField(max_length=48, null=True, blank=True)
    txt_manager_login_id=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='managing_users')
    # txt_default_reviewer_id = models.CharField(max_length=48, null=True, blank=True)
    txt_default_reviewer_id=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='reviewing_users')
    # txt_credit_approver_id = models.CharField(max_length=48, null=True, blank=True)
    txt_credit_approver_id=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='credit_approved_users')

    cod_home_branch = models.CharField(max_length=6, null=True, blank=True)

    flg_disabled = models.CharField(max_length=1, choices=YES_NO, null=True, blank=True)
    flg_user_logged_in = models.CharField(max_length=1, choices=YES_NO, null=True, blank=True)

    dat_last_login = models.DateField(null=True, blank=True)
    num_failed_pwd = models.SmallIntegerField(null=True, blank=True)

    dat_profile_created = models.DateField(null=True, blank=True)
    dat_profile_expiry = models.DateField(null=True, blank=True)

    cod_time_zone = models.ForeignKey(
    'masters.MstTimeZone',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='users'
)


    # 2FA and other optional fields
    cod_2fa_question_1 = models.CharField(max_length=4, null=True, blank=True)
    txt_2fa_answer_1 = models.CharField(max_length=48, null=True, blank=True)
    cod_2fa_question_2 = models.CharField(max_length=4, null=True, blank=True)
    txt_2fa_answer_2 = models.CharField(max_length=48, null=True, blank=True)
    cod_2fa_question_3 = models.CharField(max_length=4, null=True, blank=True)
    txt_2fa_answer_3 = models.CharField(max_length=48, null=True, blank=True)
    cod_2fa_question_4 = models.CharField(max_length=4, null=True, blank=True)
    txt_2fa_answer_4 = models.CharField(max_length=48, null=True, blank=True)
    cod_2fa_question_5 = models.CharField(max_length=4, null=True, blank=True)
    txt_2fa_answer_5 = models.CharField(max_length=48, null=True, blank=True)

    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS, default='A', null=True, blank=True)

    # txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
    txt_last_maker_id=models.ForeignKey('self',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    # txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
    txt_last_checker_id=models.ForeignKey('self',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    # manager and auth settings
    objects = SecUserManager()
    USERNAME_FIELD = 'txt_login_id'
    REQUIRED_FIELDS = []  # only txt_login_id is required

    class Meta:
        db_table = "sec_user_master"
        indexes = [
            models.Index(fields=["txt_login_id"]),
            models.Index(fields=["cod_rec_status"]),
        ]

    def __str__(self):
        return f"{self.txt_login_id} ({self.cod_rec_status})"

    # @property
    # def password(self):
    #     return self.txt_user_signature

    # @password.setter
    # def password(self, raw):
    #     self.set_password(raw)

    # def set_password(self, raw_password):
    #     if raw_password is None:
    #         self.txt_user_signature = None
    #     else:
    #         self.txt_user_signature = make_password(raw_password)
    def save(self, *args, **kwargs):
     if self.is_superuser:
        if not self.password and not self._state.adding:
            raise ValueError("Superuser must have a password")
     super().save(*args, **kwargs)






    # def check_password(self, raw_password):
    #     if not self.txt_user_signature:
    #         return False
    #     import re, hashlib
    #     val = self.txt_user_signature
    #     if re.fullmatch(r'[0-9a-f]{32}', val or ''):
    #         if hashlib.md5(raw_password.encode()).hexdigest() == val:
    #             self.set_password(raw_password)
    #             self.save(update_fields=['txt_user_signature'])
    #             return True
    #         return False
    #     return django_check_password(raw_password, val)


from django.db import models

YES_NO = (
    ('Y', 'Yes'),
    ('N', 'No'),
)

class SecUserAccessLog(models.Model):
    txt_login_id = models.CharField(max_length=48)
    dat_time_login = models.DateTimeField()
    flg_success = models.CharField(max_length=1,choices=YES_NO,null=True,blank=True)
    txt_ip_address_source = models.CharField(max_length=96,null=True,blank=True)
    txt_browser_used = models.CharField(max_length=48,null=True,blank=True )
    txt_os_used = models.CharField(max_length=48,null=True,blank=True)
    txt_user_agent_string = models.TextField(null=True,blank=True)
    txt_login_fail_reason = models.CharField(max_length=48,null=True,blank=True)

    class Meta:
        db_table = "sec_user_access_log"
        unique_together = ("txt_login_id", "dat_time_login")
        verbose_name = "User Access Log"
        verbose_name_plural = "User Access Logs"

    def __str__(self):
        return f"{self.txt_login_id} - {self.dat_time_login}"



CSS_THEME_CHOICES = [
    ('DW', 'Default White'),
    ('DK', 'Dark'),
    # Add more theme codes if needed
]

class SecUserPreferences(models.Model):
    txt_login_id = models.OneToOneField(SecUserMaster,on_delete=models.SET_NULL,null=True,blank=True, related_name='profile')
    txt_photos_default_dir = models.CharField(max_length=255, null=True, blank=True)
    txt_docs_default_dir = models.CharField(max_length=255, null=True, blank=True)
    bin_user_profile_pic = models.ImageField(upload_to=upload_to_user_profile_pic,null=True,blank=True)
    cod_css_theme = models.CharField(max_length=4, choices=CSS_THEME_CHOICES, null=True, blank=True)

    class Meta:
        db_table = "sec_user_preferences"

    def __str__(self):
        return f"{self.txt_login_id} Preferences"

class SecUserPswdHist(models.Model):
    id = models.BigAutoField(primary_key=True)  # Django-required surrogate PK
    txt_login_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='password_history')
    txt_user_signature = models.CharField(max_length=255)
    dat_passwd_from = models.DateField(null=True, blank=True)
    dat_passwd_to = models.DateField(null=True, blank=True)
    txt_pswd_changed_by = models.CharField(max_length=48, null=True, blank=True)

    class Meta:
        db_table = "sec_user_pswd_hist"
        verbose_name = "User Password History"
        verbose_name_plural = "User Password Histories"

        indexes = [


            models.Index(
                fields=["txt_login_id", "txt_user_signature", "dat_passwd_from"],
                name="idx_sec_user_pswd_hist"
            )
        ]

    def __str__(self):
        return f"{self.txt_login_id} | {self.dat_passwd_from}"
