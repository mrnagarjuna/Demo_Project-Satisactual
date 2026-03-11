from django.db import models
from utils.constants.choices import YES_NO_CHOICES,REC_STATUS_CHOICES
from ..user.models import SecUserMaster
from django.utils import timezone

# Create your models here


class SecUserRoles(models.Model):
    cod_user_role = models.CharField(max_length=4,unique=True)
    txt_user_role_desc = models.CharField(max_length=48,null=True,blank=True)
    cod_home_menu = models.OneToOneField('masters.SecMenuOptions',null=True,blank=True,on_delete=models.SET_NULL,related_name='role_home_menu')
    flg_hr_admin = models.CharField(max_length=1,choices=YES_NO_CHOICES,default="N")
    flg_sec_admin = models.CharField(max_length=1,choices=YES_NO_CHOICES,default="N")
    flg_sysadmin = models.CharField( max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)
    flg_self_service_role = models.CharField(max_length=1,choices=YES_NO_CHOICES,default="N")
    flg_default_value = models.CharField(max_length=1,choices=YES_NO_CHOICES,default="N")

    num_time_start_wkday = models.SmallIntegerField(default=800) 
    num_time_end_wkday = models.SmallIntegerField(default=1800)
    num_time_start_wkend = models.SmallIntegerField(default=800)
    num_time_end_wkend = models.SmallIntegerField(default=1300)
    num_time_start_holiday = models.SmallIntegerField(default=0)
    num_time_end_holiday = models.SmallIntegerField(default=0)
    num_seconds_inactivity_timeout = models.SmallIntegerField(default=300)

    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default="A" )
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True,blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True,blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "sec_user_roles"
        unique_together = ("cod_user_role", "cod_rec_status")
        verbose_name = "User Role"
        verbose_name_plural = "User Roles"

    def __str__(self):
        return f"{self.cod_user_role} - {self.txt_user_role_desc}"




class SecUserXRoles(models.Model):
    txt_login_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='user_x_roles')
    cod_user_role = models.ForeignKey(SecUserRoles,on_delete=models.SET_NULL,null=True,blank=True,related_name='user_x_roles')
    dat_time_disclosure_ack = models.DateTimeField(null=True,blank=True)
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default="A")
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True,blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True,blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "sec_user_x_roles"
        unique_together = (
            "txt_login_id",
            "cod_user_role",
            "cod_rec_status",
        )
        verbose_name = "User Role Mapping"
        verbose_name_plural = "User Role Mappings"

    def __str__(self):
        return f"{self.txt_login_id} → {self.cod_user_role}"
    
class SecUserRoleMenus(models.Model):
    id = models.BigAutoField(primary_key=True)
    cod_user_role = models.ForeignKey(SecUserRoles,on_delete=models.SET_NULL,null=True,blank=True,related_name='role_menus')
    cod_menu_option = models.ForeignKey('masters.SecMenuOptions',null=True,blank=True,on_delete=models.SET_NULL,related_name='user_role_menus')
    flg_get = models.CharField(max_length=1,choices=YES_NO_CHOICES, default='Y')
    # flg_create = models.CharField(max_length=1,choices=YES_NO_CHOICES, default='N')
    flg_post = models.CharField(max_length=1,choices=YES_NO_CHOICES, default='N')
    flg_put = models.CharField(max_length=1,choices=YES_NO_CHOICES, default='N')
    flg_delete = models.CharField(max_length=1,choices=YES_NO_CHOICES, default='N')
    num_display_order = models.SmallIntegerField(null=True,blank=True)
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True,blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True,blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "sec_user_role_menus"
        unique_together = (
           "cod_user_role",
            "cod_menu_option",
            "cod_rec_status",
        )
       

    def __str__(self):
        return f"{self.cod_user_role} - {self.cod_menu_option} ({self.cod_rec_status})"
    
class SecUserRoleDisclosures(models.Model):
    id = models.BigAutoField(primary_key=True)
    cod_disclosure = models.CharField(max_length=4)
    cod_user_role = models.ForeignKey(SecUserRoles,on_delete=models.SET_NULL,null=True,blank=True,related_name='role_disclosures')
    num_sequence = models.SmallIntegerField(null=True,blank=True)
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES)
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True,blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True,blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "sec_user_role_disclosures"
        managed = True
        unique_together=(
            "cod_disclosure",
            "cod_user_role",
            "cod_rec_status",
        )
        
        verbose_name = "User Role Disclosure"
        verbose_name_plural = "User Role Disclosures"

    def __str__(self):
        return f"{self.cod_disclosure} - {self.cod_user_role} ({self.cod_rec_status})"
    

