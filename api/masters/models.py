from django.db import models
from utils.constants.choices import REC_STATUS_CHOICES, YES_NO_CHOICES,AUDIT_PERIODICITY_CHOICES,FOREX_CATEGORY,OFFICE_TYPE,AUDIT_FREQ_CHOICES,BASE_COLL_TYPE_CHOICES,DEPR_METHOD_CHOICES,REVIEW_FREQ_CHOICES,BASE_CHANNEL_CHOICES,FREQ_VERIFICATION_CHOICES,DOC_PURPOSE_CHOICES,MAIL_PROTOCOL_CHOICES,CROP_CLASS_CHOICES,RESIDENCE_TYPE_CHOICES,CUST_TYPE_CHOICES,KYC_RISK_CHOICES,OLD_ACCT_PROD_CHOICES,GENDER_CHOICES,WING_CHOICES,PHONE_TYPE_CHOICES,MSG_TYPE_CHOICES,BILLING_FREQUENCY
from django.utils import timezone
from ..campaign.models import MstThirdParties
from utils.management.file_rename import upload_to_menuoption


class MstAddrTypes(models.Model):
    cod_addr_type = models.CharField(max_length=8,null=True,blank=True)
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_addr_type_desc = models.CharField(max_length=48, null=True, blank=True)
    flg_accept_as_primary = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True, default='N')
    flg_accept_for_individual = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_accept_for_organization = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    dat_last_maker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')
    


    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'mst_addr_types'
        # managed = False  # Use existing table
        unique_together = ('cod_addr_type', 'cod_rec_status')  # composite primary key

class MstDepartmentSupportTeam(models.Model):
    cod_department = models.ForeignKey('masters.MstDepartments',on_delete=models.SET_NULL,null=True,blank=True,related_name='department_support_team')
    id_third_party = models.ForeignKey(MstThirdParties,null=True,blank=True,on_delete=models.DO_NOTHING,related_name="departments_support_team")
    txt_login_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',   on_delete=models.SET_NULL,null=True,blank=True,db_column='txt_login_id',  related_name='support_team_memberships')
    dat_from = models.DateField(null=True, blank=True)
    dat_to = models.DateField(null=True, blank=True)
    flg_hr_admin = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_sec_admin = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    txt_role = models.CharField(max_length=48, null=True, blank=True)
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'mst_department_support_team'
        unique_together = ('cod_department',  'cod_rec_status', 'id_third_party')

    def __str__(self):
        return f"{self.cod_department} - {self.txt_login_id}"
    
class MstDepartments(models.Model):
    cod_department = models.CharField(max_length=4)  # '2101', '2102'
    id_third_party = models.ForeignKey(MstThirdParties,null=True,blank=True,on_delete=models.DO_NOTHING,related_name="departments") # 21
    txt_department_name = models.CharField(max_length=96, null=True, blank=True)  # 'Schn Learning Centers'
    txt_dept_head_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_dept_head_id') 
    txt_dept_deputy_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_dept_deputy_id') 
    cod_parent_department = models.ForeignKey('self',null=True,blank=True,on_delete=models.SET_NULL,related_name='child_departments')
    flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')  # 'N'
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')  # 'A'
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')  # 'SYSTEM'
    dat_last_maker = models.DateField(null=True, blank=True, default='2018-01-01')  # '2018-01-01'
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')  # 'SYSTEM'
    dat_last_checker = models.DateField(null=True, blank=True, default='2018-01-01')
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')  
    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'mst_departments'
        unique_together = ('cod_department', 'id_third_party', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_department} - {self.txt_department_name}"
    
class MstDisabilityCodes(models.Model):
    cod_disability = models.CharField(max_length=4)  # PK part 1
    txt_disability_desc = models.CharField(max_length=48, null=True, blank=True)

    flg_loss_of_legs = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_loss_of_arms = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_loss_of_vision = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_loss_of_hearing = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_mental_disability = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_certificate_required = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')  # PK part 2

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'mst_disability_codes'
        unique_together = ('cod_disability', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_disability} - {self.txt_disability_desc}"
    
class MstDisclosureLang(models.Model):
    cod_disclosure = models.ForeignKey('masters.MstDisclosures',on_delete=models.SET_NULL,null=True,blank=True,related_name='disclosure_lang')
    cod_language = models.ForeignKey('masters.MstLanguages',on_delete=models.SET_NULL,null=True,blank=True,related_name='disclosure_lang')
    txt_disclosure_phrasing = models.TextField(null=True, blank=True)
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'mst_disclosure_lang'
        unique_together = ('cod_disclosure', 'cod_language', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_disclosure} - {self.cod_language} - {self.cod_rec_status}"
    
class MstDisclosures(models.Model):
    cod_disclosure = models.CharField(max_length=4)
    txt_disclosure_desc = models.CharField(max_length=255, null=True, blank=True)
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'mst_disclosures'
        unique_together = ('cod_disclosure', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_disclosure} - {self.cod_rec_status}"

class MstDistrictCodes(models.Model):
    cod_district = models.CharField(max_length=12)
    cod_state = models.ForeignKey('masters.MstStateCodes',on_delete=models.SET_NULL,null=True,blank=True,related_name='districts_list_state')
    cod_country = models.ForeignKey('masters.MstCountryCodes',on_delete=models.SET_NULL,null=True,blank=True,related_name='districts_list_country')
    txt_district_name = models.CharField(max_length=96, null=True, blank=True)
    flg_default_value = models.CharField( max_length=1, choices=YES_NO_CHOICES,default='N')
    cod_rec_status = models.CharField( max_length=1, choices=REC_STATUS_CHOICES,default='A')
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "mst_district_codes"
        unique_together = ('cod_district', 'cod_state', 'cod_country', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_district} - {self.txt_district_name}"
    
class MstCityClasses(models.Model):
    cod_city_class = models.CharField(max_length=4)
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_city_class_desc = models.CharField(max_length=48, null=True, blank=True)

    amt_mthly_rent_hni = models.FloatField(null=True, blank=True)
    amt_mthly_rent_affluent = models.FloatField(null=True, blank=True)
    amt_mthly_rent_emerging = models.FloatField(null=True, blank=True)
    amt_mthly_rent_mass = models.FloatField(null=True, blank=True)

    amt_mthly_exp_per_head_hni = models.FloatField(null=True, blank=True)
    amt_mthly_exp_per_head_affluent = models.FloatField(null=True, blank=True)
    amt_mthly_exp_per_head_emerging = models.FloatField(null=True, blank=True)
    amt_mthly_exp_per_head_mass = models.FloatField(null=True, blank=True)

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        """Automatically update maker/checker dates."""
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'mst_city_classes'
        unique_together = ('cod_city_class', 'cod_rec_status')  # Composite primary key
        managed = True
    
# class MstApplScoringModels(models.Model):
#     cod_scoring_model = models.CharField(max_length=4)
#     dat_valid_from = models.DateField()
#     dat_valid_to = models.DateField(null=True, blank=True)
#     txt_scoring_model_name = models.CharField(max_length=48)

#     num_min_inc_score = models.SmallIntegerField(null=True, blank=True)
#     num_inc_score_weight = models.SmallIntegerField(null=True, blank=True)

#     num_min_coll_score = models.SmallIntegerField(null=True, blank=True)
#     num_coll_score_weight = models.SmallIntegerField(null=True, blank=True)

#     num_min_bureau_score = models.SmallIntegerField(null=True, blank=True)
#     num_bureau_score_weight = models.SmallIntegerField(null=True, blank=True)

#     num_min_relation_score = models.SmallIntegerField(null=True, blank=True)
#     num_relation_score_weight = models.SmallIntegerField(null=True, blank=True)

#     num_min_guarantor_score = models.SmallIntegerField(null=True, blank=True)
#     num_guarantor_score_weight = models.SmallIntegerField(null=True, blank=True)

#     num_min_insurance_score = models.SmallIntegerField(null=True, blank=True)
#     num_insurance_score_weight = models.SmallIntegerField(null=True, blank=True)

#     num_min_debt_score = models.SmallIntegerField(null=True, blank=True)
#     num_debt_score_weight = models.SmallIntegerField(null=True, blank=True)

#     num_intercept = models.FloatField(null=True, blank=True)

#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')
#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)
#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.pk:  
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table = 'mst_appl_scoring_models'
#         unique_together = ('cod_scoring_model', 'dat_valid_from', 'cod_rec_status')

# class MstAssignmentTypes(models.Model):
#     cod_assignment_typ = models.CharField(max_length=4)
#     txt_assignment_type_desc = models.CharField(max_length=48, null=True, blank=True)
#     flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')
#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)
#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.pk:  
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)


#     class Meta:
#         db_table = 'mst_assignment_types'
#         unique_together = ('cod_assignment_typ', 'cod_rec_status')

class MstAuditChecklist(models.Model):
    cod_audit_item = models.CharField(max_length=4, primary_key=False)
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_item_desc = models.CharField(max_length=96, null=True, blank=True)
    num_display_sequence = models.SmallIntegerField(default=90)

    flg_group_loan_check = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_commercial_loan_check = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_secured_loan_check = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_guarantor_required_check = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_fixed_rate_check = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_multi_disburse_check = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_debt_consolidation_check = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_rate_discount_check = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_early_payoff_allowed_check = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_interest_subvention_check = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_priority_sector_check = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)

    flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "mst_audit_checklist"
        unique_together = ('cod_audit_item', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_audit_item} - {self.txt_item_desc}"
    
class MstAuditTypes(models.Model):
    cod_audit_type = models.CharField(max_length=4)
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES)

    txt_audit_type_desc = models.CharField(max_length=48, null=True, blank=True)
    enu_audit_periodicity = models.CharField(max_length=1, choices=AUDIT_PERIODICITY_CHOICES, default='X')

    num_days_audit = models.SmallIntegerField(default=7)
    num_days_audit_findings = models.SmallIntegerField(default=3)
    num_days_audit_response = models.SmallIntegerField(default=3)
    num_days_audit_review = models.SmallIntegerField(default=3)

    flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)


    class Meta:
        db_table = "mst_audit_types"
        unique_together = ('cod_audit_type', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_audit_type} - {self.txt_audit_type_desc}"

# class MstBankBranches(models.Model):
#     cod_ifsc_bank_branch = models.CharField(max_length=48)
#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

#     txt_bank_branch_name = models.CharField(max_length=48, null=True, blank=True)
#     cod_bank = models.CharField(max_length=4)
#     txt_micr_code = models.CharField(max_length=48, null=True, blank=True)
#     txt_branch_address = models.CharField(max_length=96, null=True, blank=True)
#     txt_branch_contact = models.CharField(max_length=96, null=True, blank=True)
#     txt_branch_city = models.CharField(max_length=48, null=True, blank=True)

#     cod_branch_district = models.CharField(max_length=8, null=True, blank=True)
#     cod_branch_state = models.CharField(max_length=8, null=True, blank=True)
#     cod_pin_code = models.CharField(max_length=8, null=True, blank=True)
#     txt_post_office_name = models.CharField(max_length=48, null=True, blank=True)

#     num_longitude = models.FloatField(null=True, blank=True)
#     num_latitude = models.FloatField(null=True, blank=True)

#     enu_office_type = models.CharField(max_length=1, choices=OFFICE_TYPE, null=True, blank=True)
#     dat_office_open = models.DateField(null=True, blank=True)
#     dat_office_closed = models.DateField(null=True, blank=True)

#     txt_license_number = models.CharField(max_length=48, null=True, blank=True)
#     dat_revalidation = models.DateField(null=True, blank=True)

#     # All Y/N Flags
#     flg_general_banking = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_hsg_cons_vehicle_finance = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_corporate_banking = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_agri_finance = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_specialized_msme = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_forex = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_cap_mkt_inv_banking = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_govt_business = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_taxes = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_ppf_pension_services = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_cust_self_service = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_ultra_small = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_treasury_branch = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_forex_treasury = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_currency_chest = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_small_coin_depot = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_asset_recovery_branch = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_clearing_payment_svc = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_deposit_processing_center = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_loan_processing_center = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_forex_processing_center = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_trade_fin_processing_center = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_administrative_office = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_extension_counter = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_satellite_office = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_mobile_office = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_service_branch = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_mobile_atm = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_onsite_atm = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_offsite_atm = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_rep_office = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_exchg_bureau = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)

#     enu_auth_forex_dealer_category = models.CharField(max_length=1, choices=FOREX_CATEGORY, null=True, blank=True)
#     dat_forex_authorized = models.DateField(null=True, blank=True)

#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)
#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.pk:  
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table = "mst_bank_branches"
#         unique_together = ('cod_ifsc_bank_branch', 'cod_rec_status')

#     def __str__(self):
#         return f"{self.cod_ifsc_bank_branch} - {self.txt_bank_branch_name}"
    
# class MstBankCodes(models.Model):
#     cod_bank = models.CharField(max_length=48)
#     txt_bank_short_name = models.CharField(max_length=48, null=True, blank=True)
#     txt_bank_name = models.CharField(max_length=96, null=True, blank=True)

#     cod_bank_type = models.CharField(max_length=4, null=True, blank=True)
#     cod_owner_bank = models.CharField(max_length=4, null=True, blank=True)
#     cod_owner_country = models.CharField(max_length=4, null=True, blank=True)

#     dat_opened = models.DateField(null=True, blank=True)
#     dat_closed_or_merged = models.DateField(null=True, blank=True)
#     cod_bank_merged_with = models.CharField(max_length=4, null=True, blank=True)

#     flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)
#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.pk:  
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table = 'mst_bank_codes'
#         unique_together = (('cod_bank', 'cod_rec_status'),)

#     def __str__(self):
#         return self.txt_bank_name or self.cod_bank
    
# class MstBankTypes(models.Model):
#     cod_bank_type = models.CharField(max_length=4)
#     txt_bank_type_desc = models.CharField(max_length=48, null=True, blank=True)

#     flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)

#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.pk:  
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table = "mst_bank_types"
#         unique_together = (("cod_bank_type", "cod_rec_status"),)

#     def __str__(self):
#         return self.txt_bank_type_desc or self.cod_bank_type
    
# class MstBlockCodes(models.Model):
#     cod_block = models.CharField(max_length=12)
#     cod_district = models.CharField(max_length=12)
#     cod_state = models.CharField(max_length=8)
#     cod_country = models.CharField(max_length=4)
#     txt_block_name = models.CharField(max_length=48, null=True, blank=True)
#     flg_default_value = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
#     cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')
#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)
#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)
#     class Meta:
#         db_table = "mst_block_codes"
#         unique_together = (
#             'cod_block',
#             'cod_district',
#             'cod_state',
#             'cod_country',
#             'cod_rec_status'
#         )

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.cod_block} - {self.txt_block_name}"
    
# class MstCardLogos(models.Model):
#     cod_logo = models.CharField(max_length=4)
#     txt_logo_name = models.CharField(max_length=48, null=True, blank=True)
#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)

#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table = 'mst_card_logos'
#         unique_together = ('cod_logo', 'cod_rec_status')   # Composite Primary Key
#         # managed = True

#     def __str__(self):
#         return f"{self.cod_logo} - {self.txt_logo_name}"
    
# class MstCenterTypes(models.Model):
#     cod_center_type = models.CharField(max_length=4)
#     txt_center_type_desc = models.CharField(max_length=48, null=True, blank=True)

#     flg_default_value = models.CharField(
#         max_length=1, choices=YES_NO_CHOICES, default='N'
#     )

#     num_min_center_members = models.SmallIntegerField(null=True, blank=True)
#     num_max_center_members = models.SmallIntegerField(null=True, blank=True)

#     min_meetings_first_disburse = models.SmallIntegerField(null=True, blank=True)
#     min_meetings_next_disburse = models.SmallIntegerField(null=True, blank=True)

#     enu_center_audit_freq = models.CharField(
#         max_length=1, choices=AUDIT_FREQ_CHOICES, default='Q'
#     )

#     cod_rec_status = models.CharField(
#         max_length=1, choices=REC_STATUS_CHOICES, default='A'
#     )

#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)

#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)

#     class Meta:
#         db_table = 'mst_center_types'
#         unique_together = ('cod_center_type', 'cod_rec_status')  # composite PK
#         #managed = True

#     def __str__(self):
#         return self.cod_center_type
    
# class MstClauseLibrary(models.Model):
#     id_clause = models.BigIntegerField()
#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

#     txt_clause_desc = models.CharField(max_length=96)
#     txt_clause_heading = models.CharField(max_length=96)
#     txt_clause_phrasing = models.TextField()   # MEDIUMTEXT → TextField in Django

#     id_clause_group = models.BigIntegerField(null=True, blank=True)
#     num_sequence = models.SmallIntegerField(null=True, blank=True)

#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)

#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         """Auto-update maker/checker timestamps."""
#         if not self.pk:
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table = 'mst_clause_library'
#         unique_together = ('id_clause', 'cod_rec_status')
#        # managed = True

# class MstClauseLibraryLang(models.Model):

#     id_clause = models.BigIntegerField()
#     cod_language = models.CharField(max_length=96)

#     txt_clause_heading = models.CharField(max_length=96)
#     txt_clause_phrasing = models.TextField()

#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)

#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         """Update maker/checker dates automatically."""
#         if not self.pk:
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table = "mst_clause_library_lang"
#         unique_together = ("id_clause", "cod_rec_status", "cod_language")
#         managed = True

#     def __str__(self):
#         return f"{self.id_clause} - {self.cod_language}"
    
# class MstCollateralTypes(models.Model):
#     cod_coll_type = models.CharField(max_length=4)
#     cod_base_coll_type = models.CharField(max_length=1, choices=BASE_COLL_TYPE_CHOICES, null=True, blank=True)
#     txt_coll_type_desc = models.CharField(max_length=48, null=True, blank=True)
#     num_max_ltv_pct = models.SmallIntegerField(null=True, blank=True)
#     rat_depreciation = models.FloatField(null=True, blank=True)
#     num_years_active_life = models.SmallIntegerField(default=5)
#     enu_depr_method = models.CharField(max_length=1, choices=DEPR_METHOD_CHOICES, default='S')
#     num_pct_salvage_value = models.FloatField(null=True, blank=True)
#     enu_review_frequency = models.CharField(max_length=1, choices=REVIEW_FREQ_CHOICES, default='O')
#     flg_asset_registry_available = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     id_thirdparty_registry = models.BigIntegerField(null=True, blank=True)
#     txt_asset_registry_coll_type = models.CharField(max_length=48, null=True, blank=True)
#     flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
#     num_min_days_to_mature = models.SmallIntegerField(default=0)
#     num_max_days_to_mature = models.SmallIntegerField(default=0)
#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')
#     txt_last_maker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
#     dat_last_maker = models.DateField(null=True, blank=True)
#     txt_last_checker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         """Update maker/checker dates automatically."""
#         if not self.pk:
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table = 'mst_collateral_types'
#         unique_together = ('cod_coll_type', 'cod_rec_status')

#     def __str__(self):
#         return f"{self.cod_coll_type} - {self.txt_coll_type_desc}"
    
class MstCountryCodes(models.Model):
    cod_country = models.CharField(max_length=4)
    txt_country_name = models.CharField(max_length=48, null=True, blank=True)
    txt_country_short_name = models.CharField(max_length=48)
    txt_nationality_name = models.CharField(max_length=48, null=True, blank=True)
    cod_country_alternative = models.CharField(max_length=4, null=True, blank=True)
    txt_phone_code = models.CharField(max_length=48, null=True, blank=True)
    num_hours_gmt_offset = models.FloatField(null=True, blank=True)

    flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        """Update maker/checker dates automatically."""
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'mst_country_codes'
        unique_together = ('cod_country', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_country} - {self.txt_country_name}"
    
# class MstCovenantCodes(models.Model):
#     cod_covenant = models.CharField(max_length=4)
#     txt_covenant_desc = models.CharField(max_length=48, null=True, blank=True)
#     cod_covenant_type = models.CharField(max_length=4, null=True, blank=True)
#     txt_covenant_phrasing = models.TextField(null=True, blank=True)
#     txt_remedial_action = models.TextField(null=True, blank=True)
#     num_days_remediation_grace = models.SmallIntegerField(null=True, blank=True)
#     txt_penal_action = models.TextField(null=True, blank=True)
#     cod_covenant_key_ratio = models.CharField(max_length=4, null=True, blank=True)
#     num_min_value_default = models.FloatField(null=True, blank=True)
#     num_max_value_default = models.FloatField(null=True, blank=True)
#     enu_freq_verification = models.CharField(max_length=1, choices=FREQ_VERIFICATION_CHOICES, null=True, blank=True)
#     txt_verification_method = models.CharField(max_length=255, null=True, blank=True)
#     cod_doc_type = models.CharField(max_length=4, null=True, blank=True)
#     enu_doc_purpose = models.CharField(max_length=1, choices=DOC_PURPOSE_CHOICES, null=True, blank=True)

#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES)

#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)
#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         """Update maker/checker dates automatically."""
#         if not self.pk:
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)


#     class Meta:
#         db_table = 'mst_covenant_codes'
#         unique_together = ('cod_covenant', 'cod_rec_status')

#     def __str__(self):
#         return f"{self.cod_covenant} - {self.txt_covenant_desc}"
    
# class MstCovenantTypes(models.Model):
#     id = models.BigAutoField(primary_key=True)

#     cod_covenant_type = models.CharField(max_length=4)
#     txt_covenant_type_desc = models.CharField(max_length=48, null=True, blank=True)
#     flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)
#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         """Update maker/checker dates automatically."""
#         if not self.pk:
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)


#     class Meta:
#         db_table = 'mst_covenant_types'
#         unique_together = ('cod_covenant_type', 'cod_rec_status')

#     def __str__(self):
#         return f"{self.cod_covenant_type} - {self.txt_covenant_type_desc}"
    
class MstCreditOfficerLevels(models.Model):
    id = models.BigAutoField(primary_key=True)

    cod_credit_officer_level = models.CharField(max_length=4)
    txt_credit_officer_level_desc = models.CharField(max_length=48, null=True, blank=True)

    amt_max_approving_authority = models.FloatField(null=True, blank=True)
    amt_single_approver_limit = models.FloatField(null=True, blank=True)
    amt_annual_approval_limit = models.FloatField(null=True, blank=True)

    flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        """Update maker/checker dates automatically."""
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)


    class Meta:
        db_table = 'mst_credit_officer_levels'
        unique_together = ('cod_credit_officer_level', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_credit_officer_level} - {self.txt_credit_officer_level_desc}"

# class MstCropTypes(models.Model):
#     id = models.BigAutoField(primary_key=True)

#     cod_crop_type = models.CharField(max_length=4)
#     enu_crop_class = models.CharField(
#         max_length=10,
#         choices=CROP_CLASS_CHOICES,
#         default='BASIC'
#     )
#     txt_crop_type_desc = models.CharField(max_length=96, null=True, blank=True)

#     num_kgs_yield_per_acre = models.SmallIntegerField(null=True, blank=True)
#     amt_purch_price_per_kg = models.FloatField(null=True, blank=True)
#     amt_input_costs_per_acre = models.FloatField(null=True, blank=True)

#     max_harvests_per_year = models.SmallIntegerField(null=True, blank=True)
#     num_mths_crop_cycle = models.SmallIntegerField(null=True, blank=True)
#     num_days_shelf_life = models.SmallIntegerField(null=True, blank=True)

#     cod_rec_status = models.CharField(
#         max_length=1,
#         choices=REC_STATUS_CHOICES
#     )

#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)
#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         """Update maker/checker dates automatically."""
#         if not self.pk:
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table = "mst_crop_types"
#         unique_together = ('cod_crop_type', 'cod_rec_status')

#     def __str__(self):
#         return f"{self.cod_crop_type} - {self.txt_crop_type_desc}"
    
class MstCurrency(models.Model):
    id = models.BigAutoField(primary_key=True)

    cod_currency = models.CharField(max_length=4)
    txt_currency_desc = models.CharField(max_length=48, null=True, blank=True)
    txt_currency_symbol = models.CharField(max_length=1, null=True, blank=True)
    cod_country = models.OneToOneField('masters.MstCountryCodes',on_delete=models.SET_NULL,null=True,blank=True,related_name='country_currency')

    num_decimal_places = models.SmallIntegerField(null=True, blank=True)
    txt_minor_unit_name = models.CharField(max_length=48, null=True, blank=True)

    flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        """Update maker/checker dates automatically."""
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "mst_currency"
        unique_together = ('cod_currency', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_currency} - {self.txt_currency_desc}"
    
class SecMenuOptions(models.Model):
    id = models.BigAutoField(primary_key=True)

    cod_menu_option = models.CharField(max_length=4)
    txt_menu_desc = models.CharField(max_length=96, null=True, blank=True)
    txt_menu_helptext = models.TextField(null=True, blank=True)
    url=models.CharField(max_length=128,null=True,blank=True)

    bin_menu_icon = models.CharField(max_length=96, null=True, blank=True)

    flg_is_root_menu = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_show_as_menu = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')

    cod_parent_menu_option = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True,
    related_name='child_menus')

    txt_menu_param_1 = models.CharField(max_length=96, null=True, blank=True)
    txt_menu_param_2 = models.CharField(max_length=96, null=True, blank=True)
    txt_menu_param_3 = models.CharField(max_length=96, null=True, blank=True)

    cod_module = models.CharField(max_length=4, null=True, blank=True)
    

    flg_public = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        """Update maker/checker dates automatically."""
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "sec_menu_options"
        unique_together = ('cod_menu_option', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_menu_option} - {self.txt_menu_desc}"


class MstLanguages(models.Model):
    cod_language = models.CharField(max_length=4)
    txt_language_name = models.CharField( max_length=48,null=True,blank=True)
    txt_iso_3char_code = models.CharField(max_length=4,null=True,blank=True)
    txt_iso_2char_code = models.CharField(max_length=4,null=True,blank=True)
    flg_default_value = models.CharField( max_length=1,choices=YES_NO_CHOICES,default='N')
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True,blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True,blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    class Meta:
        db_table = 'mst_languages'
        unique_together = ('cod_language', 'cod_rec_status')
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return f"{self.cod_language} - {self.txt_language_name}"
    
# class MstLegalDisputeType(models.Model):
#     cod_legal_dispute = models.CharField(max_length=4)
#     txt_legal_dispute_desc = models.CharField(max_length=48,null=True,blank=True)
#     flg_default_value = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
#     flg_criminal = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N',
#     help_text="Indicates if this is a Civil or Criminal matter")
#     cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')
#     txt_last_maker_id = models.CharField(max_length=48,null=True,blank=True)
#     dat_last_maker = models.DateField(null=True,blank=True)
#     txt_last_checker_id = models.CharField(max_length=48,null=True,blank=True)
#     dat_last_checker = models.DateField(null=True,blank=True)
#     flg_cognizable_offence = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
#     flg_bailable_offence = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')

#     class Meta:
#         db_table = "mst_legal_dispute_types"

#         unique_together = (
#             ('cod_legal_dispute', 'cod_rec_status'),
#         )
#         verbose_name = "Legal Dispute Type"
#         verbose_name_plural = "Legal Dispute Types"

#     def __str__(self):
#         return f"{self.cod_legal_dispute} - {self.txt_legal_dispute_desc}"
    
class MstMajorCity(models.Model):
    cod_city_class = models.OneToOneField('masters.MstCityClasses',on_delete=models.SET_NULL,null=True,blank=True,related_name='major_city')
    cod_country = models.ForeignKey('masters.MstCountryCodes',on_delete=models.SET_NULL,null=True,blank=True,related_name='major_cities_lists_country')
    cod_state_code = models.ForeignKey('masters.MstStateCodes',on_delete=models.SET_NULL,null=True,blank=True,related_name='major_cities_lists_state')
    txt_city_name = models.CharField(max_length=48,null=True,blank=True)
    num_longitude_nw = models.FloatField(null=True, blank=True)
    num_latitude_nw = models.FloatField(null=True, blank=True)
    num_longitude_se = models.FloatField(null=True, blank=True)
    num_latitude_se = models.FloatField(null=True, blank=True)
    cod_time_zone = models.ForeignKey('masters.MstTimeZone',on_delete=models.SET_NULL,null=True,blank=True,
    related_name='major_cities')
    num_hours_gmt_offset = models.FloatField(null=True,blank=True)
    flg_daylight_savings = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)
    cod_city = models.CharField(max_length=4,null=True,blank=True)
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True,blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True,blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    class Meta:
        db_table = "mst_major_cities"
        unique_together = (
            ('cod_city', 'cod_country', 'cod_rec_status'),
        )
        verbose_name = "Major City"
        verbose_name_plural = "Major Cities"

    def __str__(self):
        return f"{self.txt_city_name} ({self.cod_country})"
    
class MstUserDesignation(models.Model):
    cod_designation = models.CharField(max_length=4)
    id_third_party = models.ForeignKey('campaign.MstThirdParties',on_delete=models.CASCADE,null=True,blank=True)
    txt_designation_desc = models.CharField(max_length=48,null=True,blank=True)
    cod_parent_designation = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True,related_name='child_designations_list')
    flg_senior_management = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    flg_default_value = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True,blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True,blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    class Meta:
        db_table = "mst_user_designation"
        unique_together = (

            ('cod_designation', 'cod_rec_status'),
        )
        verbose_name = "User Designation"
        verbose_name_plural = "User Designations"

    def __str__(self):
        return f"{self.cod_designation} - {self.txt_designation_desc}"
    
# models.py
from django.db import models

YES_NO = (
    ('Y', 'Yes'),
    ('N', 'No'),
)

REC_STATUS = (
    ('A', 'Active'),
    ('N', 'New'),
    ('M', 'Modified'),
    ('R', 'Rejected'),
    ('C', 'Closed'),
    ('X', 'Cancelled'),
)


class MstStateCodes(models.Model):
    cod_state = models.CharField(max_length=6)
    cod_country = models.ForeignKey(MstCountryCodes,on_delete=models.SET_NULL,null=True,blank=True,related_name='states_list')
    txt_state_short_code = models.CharField(max_length=4, null=True, blank=True)
    txt_state_name = models.CharField(max_length=48, null=True, blank=True)
    flg_default_value = models.CharField(max_length=1,choices=YES_NO,default='N')
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS,default='A')
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    class Meta:
        db_table = "mst_state_codes"
        unique_together = (
            'cod_state',
            'cod_country',
            'cod_rec_status'
        )
        verbose_name = "State Code"
        verbose_name_plural = "State Codes"

    def __str__(self):
        return f"{self.cod_state} - {self.txt_state_name}"
    
# class CusMaster(models.Model):
#     id_customer = models.BigIntegerField()
#     enu_cust_typ = models.CharField(max_length=1, choices=CUST_TYPE_CHOICES, default='I')
#     flg_new_cust = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
#     dat_cust_since = models.DateField(null=True, blank=True)

#     cod_home_branch = models.CharField(max_length=8, null=True, blank=True)
#     enu_old_acct_prod_typ = models.CharField(max_length=3, choices=OLD_ACCT_PROD_CHOICES, null=True, blank=True)
#     num_old_acct = models.CharField(max_length=16, null=True, blank=True)

#     txt_cust_fname = models.CharField(max_length=96, null=True, blank=True)
#     txt_cust_mname = models.CharField(max_length=96, null=True, blank=True)
#     txt_cust_lname = models.CharField(max_length=96, null=True, blank=True)
#     txt_cust_org_name = models.CharField(max_length=255, null=True, blank=True)

#     enu_cust_gender = models.CharField(max_length=3, choices=GENDER_CHOICES, default='N/A')
#     cod_prefix = models.CharField(max_length=4, null=True, blank=True)
#     dat_cust_birth = models.DateField(null=True, blank=True)

#     flg_expired = models.CharField(max_length=1, choices=YES_NO, null=True, blank=True)
#     dat_expired = models.DateField(null=True, blank=True)

#     cod_country = models.CharField(max_length=4, null=True, blank=True)
#     cod_tax_status = models.CharField(max_length=4, null=True, blank=True)
#     cod_country_resident = models.CharField(max_length=4, null=True, blank=True)

#     bin_cust_sign = models.CharField(max_length=255, null=True, blank=True)
#     bin_cust_photo = models.CharField(max_length=255, null=True, blank=True)

#     flg_address_onsite = models.CharField(max_length=1, choices=YES_NO, default='N')
#     num_years_curr_address = models.SmallIntegerField(null=True, blank=True)

#     txt_email_id = models.CharField(max_length=96, null=True, blank=True)
#     txt_email_id_encr = models.CharField(max_length=1024, null=True, blank=True)

#     amt_monthly_income = models.FloatField(null=True, blank=True)
#     cod_occupation = models.CharField(max_length=4, null=True, blank=True)
#     cod_income_src = models.CharField(max_length=4, null=True, blank=True)
#     amt_prim_src_income = models.FloatField(null=True, blank=True)

#     txt_inc_proof_docnum = models.CharField(max_length=48, null=True, blank=True)
#     cod_inc_proof_doctyp = models.CharField(max_length=4, null=True, blank=True)
#     txt_inc_proof_issuer = models.CharField(max_length=96, null=True, blank=True)
#     dat_inc_proof_issue = models.DateField(null=True, blank=True)
#     bin_inc_proof = models.CharField(max_length=255, null=True, blank=True)

#     txt_father_name = models.CharField(max_length=96, null=True, blank=True)
#     txt_spouse_name = models.CharField(max_length=96, null=True, blank=True)
#     num_dependents = models.SmallIntegerField(null=True, blank=True)

#     cod_socio_econ_class = models.CharField(max_length=4, null=True, blank=True)
#     cod_max_education = models.CharField(max_length=4, null=True, blank=True)
#     txt_edu_specialization = models.CharField(max_length=96, null=True, blank=True)
#     txt_edu_university = models.CharField(max_length=96, null=True, blank=True)
#     num_edu_yr_graduated = models.SmallIntegerField(null=True, blank=True)

#     flg_defence_personnel = models.CharField(max_length=1, choices=YES_NO, null=True, blank=True)
#     enu_wing = models.CharField(max_length=6, choices=WING_CHOICES, null=True, blank=True)
#     cod_rank = models.CharField(max_length=4, null=True, blank=True)
#     flg_retired = models.CharField(max_length=1, choices=YES_NO, null=True, blank=True)

#     txt_employer_name = models.CharField(max_length=96, null=True, blank=True)
#     txt_employee_num = models.CharField(max_length=48, null=True, blank=True)
#     txt_designation = models.CharField(max_length=96, null=True, blank=True)
#     num_mths_in_curr_job = models.SmallIntegerField(null=True, blank=True)

#     enu_residence_type = models.CharField(max_length=1, choices=RESIDENCE_TYPE_CHOICES, null=True, blank=True)

#     cod_priority_sector = models.CharField(max_length=4, null=True, blank=True)
#     cod_religion = models.CharField(max_length=4, null=True, blank=True)
#     cod_ethnicity = models.CharField(max_length=4, null=True, blank=True)
#     cod_disability = models.CharField(max_length=4, null=True, blank=True)
#     dat_disability_registered = models.DateField(null=True, blank=True)
#     bin_disability_certificate = models.CharField(max_length=255, null=True, blank=True)

#     cod_org_typ = models.CharField(max_length=4, null=True, blank=True)
#     num_employees = models.IntegerField(null=True, blank=True)
#     cod_industry = models.CharField(max_length=4, null=True, blank=True)
#     txt_org_url = models.CharField(max_length=96, null=True, blank=True)
#     amt_annual_turnover = models.FloatField(null=True, blank=True)
#     num_office_locations = models.SmallIntegerField(null=True, blank=True)

#     amt_mthly_expenses = models.FloatField(null=True, blank=True)

#     txt_relationship_manager_id = models.CharField(max_length=48, null=True, blank=True)
#     txt_enrolled_by_id = models.CharField(max_length=48, null=True, blank=True)

#     txt_facebook_id = models.CharField(max_length=96, null=True, blank=True)
#     txt_linkedin_id = models.CharField(max_length=96, null=True, blank=True)
#     txt_twitter_handle = models.CharField(max_length=96, null=True, blank=True)

#     cod_language = models.CharField(max_length=4, null=True, blank=True)

#     flg_ok_to_call = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_ok_to_sms = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_ok_to_mail = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_ok_to_email = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_ok_affiliate_sharing = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_ok_third_party_sharing = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)

#     flg_insincere_client = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
#     flg_inactive_client = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')

#     dat_last_reg_fee_paid = models.DateField(null=True, blank=True)

#     flg_kyc_valid = models.CharField(max_length=1, choices=YES_NO, null=True, blank=True)
#     dat_kyc_valid_till = models.DateField(null=True, blank=True)
#     enu_kyc_risk_class = models.CharField(max_length=1, choices=KYC_RISK_CHOICES, default='L')

#     flg_high_value = models.CharField(max_length=1, choices=YES_NO, default='N')
#     flg_public_figure = models.CharField(max_length=1, choices=YES_NO, default='N')
#     flg_sensitive_client = models.CharField(max_length=1, choices=YES_NO, default='N')
#     flg_employee = models.CharField(max_length=1, choices=YES_NO, default='N')

#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)
#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)

#     class Meta:
#         db_table = 'cus_master'
#         unique_together = ('id_customer', 'cod_rec_status')
#         indexes = [
#             models.Index(fields=['cod_home_branch']),
#             models.Index(fields=['enu_cust_typ']),
#         ]

#     def __str__(self):
#         return str(self.id_customer)

# class CusPhoneHist(models.Model):
#     id = models.BigAutoField(primary_key=True)

#     id_customer = models.BigIntegerField(null=True, blank=True)
#     enu_phone_typ = models.CharField(max_length=1, choices=PHONE_TYPE_CHOICES)
#     dat_phone_valid_till = models.DateField()
#     txt_phone_num = models.CharField(max_length=48)

#     txt_phone_num_encr = models.CharField(max_length=1024, null=True, blank=True)

#     txt_last_maker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_maker = models.DateField(null=True, blank=True)

#     txt_last_checker_id = models.CharField(max_length=48, null=True, blank=True)
#     dat_last_checker = models.DateField(null=True, blank=True)

#     class Meta:
#         db_table = "cus_phone_hist"
#         unique_together = (
#             'id_customer',
#             'enu_phone_typ',
#             'dat_phone_valid_till',
#             'txt_phone_num',
#         )
#         verbose_name = "Customer Phone History"
#         verbose_name_plural = "Customer Phone History"

#     def __str__(self):
#         return f"{self.id_customer} - {self.enu_phone_typ} - {self.txt_phone_num}"
    
# class CusMiscDocs(models.Model):
#     id = models.BigAutoField(primary_key=True)

#     id_customer = models.BigIntegerField()
#     cod_doctyp = models.CharField(max_length=4)
#     enu_doc_purpose = models.CharField(max_length=1, choices=DOC_PURPOSE_CHOICES)

#     txt_docnum = models.CharField(max_length=48)
#     txt_doc_description = models.CharField(max_length=96, null=True, blank=True)

#     id_issuer = models.BigIntegerField(null=True, blank=True)
#     txt_issuer_name = models.CharField(max_length=96, null=True, blank=True)

#     dat_doc_issue = models.DateField(null=True, blank=True)
#     dat_doc_expire = models.DateField(null=True, blank=True)

#     bin_doc_copy = models.CharField(max_length=255, null=True, blank=True)

#     flg_original_documents_seen = models.CharField(
#         max_length=1, choices=YES_NO_CHOICES, null=True, blank=True
#     )

#     cod_doc_storage_location = models.CharField(max_length=4, null=True, blank=True)
#     txt_doc_storage_location = models.CharField(max_length=96, null=True, blank=True)

#     dat_doc_collected = models.DateField(null=True, blank=True)
#     txt_doc_collected_by_id = models.CharField(max_length=48, null=True, blank=True)

#     flg_originals_retained = models.CharField(
#         max_length=1, choices=YES_NO_CHOICES, null=True, blank=True
#     )

#     dat_doc_released = models.DateField(null=True, blank=True)
#     txt_doc_released_by_id = models.CharField(max_length=48, null=True, blank=True)

#     class Meta:
#         db_table = "cus_misc_docs"
#         unique_together = (
#             'id_customer',
#             'cod_doctyp',
#             'enu_doc_purpose',
#             'txt_docnum',
#         )
#         verbose_name = "Customer Misc Document"
#         verbose_name_plural = "Customer Misc Documents"

#     def __str__(self):
#         return f"{self.id_customer} | {self.cod_doctyp} | {self.txt_docnum}"

class MstPinCodes(models.Model):
    cod_pin_code = models.CharField(max_length=8)
    cod_country = models.ForeignKey(MstCountryCodes,on_delete=models.CASCADE,null=True,blank=True,related_name='pincodes')
    cod_state_code = models.ForeignKey(MstStateCodes,on_delete=models.CASCADE,null=True,blank=True,related_name='pincodes')
    cod_district = models.ForeignKey(MstDistrictCodes,on_delete=models.CASCADE,null=True,blank=True,related_name='pincodes')

    txt_district_name = models.CharField(max_length=48, null=True, blank=True)
    txt_city_name = models.CharField(max_length=48, null=True, blank=True)
    txt_post_office_name = models.CharField(max_length=48, null=True, blank=True)

    num_longitude = models.FloatField(null=True, blank=True)
    num_latitude = models.FloatField(null=True, blank=True)

    flg_default_value = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')

    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'mst_pin_codes'
        unique_together = (
            'cod_pin_code',
            'cod_country',
            'cod_rec_status',
        )
        verbose_name = 'PIN Code'
        verbose_name_plural = 'PIN Codes'

    def __str__(self):
        return f"{self.cod_pin_code} - {self.txt_city_name}"

class MstTimeZone(models.Model):
    cod_time_zone = models.CharField(max_length=4)
    txt_time_zone_name = models.CharField(max_length=48, null=True, blank=True)
    num_hours_gmt_offset = models.FloatField(null=True, blank=True)
    flg_daylight_savings = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "mst_time_zones"
        verbose_name = "Time Zone"
        verbose_name_plural = "Time Zones"
        unique_together = ("cod_time_zone", "cod_rec_status")

    def __str__(self):
        return f"{self.cod_time_zone} - {self.txt_time_zone_name}"
    
class SysCssTheme(models.Model):
    cod_theme = models.CharField(max_length=4)
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')

    txt_theme_name = models.CharField(max_length=48, null=True, blank=True)
    txt_theme_desc = models.CharField(max_length=96, null=True, blank=True)

    # Stores STATIC css path, NOT file content
    txt_css_file = models.CharField(max_length=255, null=True, blank=True)

    flg_default = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'sys_css_themes'
        unique_together = ('cod_theme', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_theme} ({self.cod_rec_status})"
    
class SysEmailTemplates(models.Model):

    cod_email_template = models.CharField(max_length=4)
    txt_template_name = models.CharField(max_length=96, null=True, blank=True)
    txt_sender_email_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='sent_email_template')
    txt_send_replies_to_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='replies_from_template')

    flg_public = models.CharField(max_length=1, choices=YES_NO, default='N')
    flg_request_read_receipt = models.CharField(max_length=1, choices=YES_NO, default='Y')
    flg_request_delivery_receipt = models.CharField(max_length=1, choices=YES_NO, default='Y')

    num_hours_1st_reminder = models.SmallIntegerField(default=72)
    num_hours_2nd_reminder = models.SmallIntegerField(default=168)

    txt_deeplink_url = models.CharField(max_length=255, null=True, blank=True)
    txt_deeplink_params = models.CharField(max_length=255, null=True, blank=True)
    txt_stored_proc_name = models.ForeignKey('campaign.MstQAReviewProcedure',on_delete=models.CASCADE,null=True,blank=True,related_name='email_template_proc')

    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS)

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    class Meta:
        db_table = "sys_email_templates"
        unique_together = ('cod_email_template', 'cod_rec_status')
        verbose_name = "Email Template"

    def __str__(self):
        return f"{self.cod_email_template} - {self.txt_template_name}"
    
class SysUserMessage(models.Model):
    
    id = models.AutoField(primary_key=True)
    num_message = models.SmallIntegerField()
    cod_language = models.ForeignKey('masters.MstLanguages',null=True,blank=True,on_delete=models.DO_NOTHING,related_name='user_message_language')
    txt_user_message = models.CharField(max_length=255,null=True,blank=True)
    enu_msg_type = models.CharField(max_length=1,choices=MSG_TYPE_CHOICES,default='I')
    flg_use_as_alert = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    txt_btn_ok = models.CharField(max_length=48, null=True, blank=True)
    txt_btn_cancel = models.CharField(max_length=48, null=True, blank=True)
    txt_btn_other_1 = models.CharField(max_length=48, null=True, blank=True)
    txt_btn_other_2 = models.CharField(max_length=48, null=True, blank=True)
    txt_btn_other_3 = models.CharField(max_length=48, null=True, blank=True)

    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES)

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    class Meta:
        db_table = "sys_user_messages"
        unique_together = (
            "num_message",
            "cod_language",
            "cod_rec_status"
        )
        verbose_name = "System User Message"
        verbose_name_plural = "System User Messages"

    def __str__(self):
        return f"{self.num_message} - {self.cod_language}"
    
class SysInstallModule(models.Model):

    cod_module = models.CharField(max_length=4)
    txt_module_name = models.CharField(max_length=48)
    txt_module_home_page = models.CharField(max_length=96,null=True,blank=True)
    txt_module_logo_file = models.CharField(max_length=255)
    txt_bank_name = models.CharField(max_length=96)
    id_licensee_third_party = models.BigIntegerField(default=0,null=True,blank=True)
    dat_license_start = models.DateField(null=True,blank=True)
    dat_license_expire = models.DateField(null=True,blank=True)
    txt_module_param_1 = models.CharField(max_length=96,null=True,blank=True)
    txt_module_param_2 = models.CharField(max_length=96,null=True,blank=True)
    txt_module_param_3 = models.CharField(max_length=96,null=True,blank=True)
    txt_module_key = models.CharField(max_length=255,null=True,blank=True)
    txt_selfserv_t_and_c_url = models.CharField(max_length=255,null=True,blank=True)
    flg_default_value = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')

    class Meta:
        db_table = "sys_install_modules"
        verbose_name = "Installed Module"
        verbose_name_plural = "Installed Modules"

    def __str__(self):
        return f"{self.cod_module} - {self.txt_module_name}"
    
class SubLicence(models.Model):
    id = models.AutoField(primary_key=True)

    # Composite key fields
    cod_licence_package = models.CharField(max_length=4)
    id_third_party = models.ForeignKey('campaign.MstThirdParties',null=True,blank=True,on_delete=models.SET_NULL,related_name='sub_licence_thirdparty')
    dat_licence_from = models.DateField()

    # Other fields
    dat_licence_to = models.DateField(null=True, blank=True)

    txt_licence_key = models.CharField(max_length=255,null=True,blank=True)

    cod_default_role = models.ForeignKey('roles.SecUserRoles',null=True,blank=True,on_delete=models.SET_NULL,related_name='sub_licence_role')

    num_max_users = models.SmallIntegerField(null=True, blank=True)
    num_max_locations = models.SmallIntegerField(null=True, blank=True)
    num_tier = models.SmallIntegerField(null=True, blank=True)

    id_questionnaire = models.ForeignKey('questionnaries.CmpQuestionnaire',null=True,blank=True,on_delete=models.SET_NULL,related_name='sub_licence_questionnaire')
    id_campaign = models.ForeignKey('campaign.CmpCampaigns',null=True,blank=True,on_delete=models.SET_NULL,related_name='sub_licence_campaign')

    dat_licence_applied = models.DateField(null=True, blank=True)
    txt_licence_applied_by_id = models.CharField(max_length=48, null=True, blank=True)

    dat_licence_ratified = models.DateField(null=True, blank=True)
    txt_licence_ratified_by_id = models.CharField(max_length=48, null=True, blank=True)

    flg_licence_ratified = models.CharField(max_length=1,choices=YES_NO,null=True,blank=True)

    cod_currency = models.ForeignKey(MstCurrency,null=True,blank=True,on_delete=models.SET_NULL,related_name='sub_licence_currency')


    amt_rack_rate = models.FloatField(null=True, blank=True)
    amt_charged_rate = models.FloatField(null=True, blank=True)

    enu_billing_frequency = models.CharField(max_length=1,choices=BILLING_FREQUENCY,null=True,blank=True)

    txt_sale_closed_by_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_sale_closed')
    txt_sale_approved_by_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_sale_approved')

    dat_sale_closed = models.DateField(null=True, blank=True)
    dat_sale_approved = models.DateField(null=True, blank=True)

    dat_cancel_requested = models.DateField(null=True, blank=True)
    txt_cancel_requested_by = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_cancel_request')

    dat_cancel_effective = models.DateField(null=True, blank=True)

    cod_cancel_reason = models.CharField(max_length=4, null=True, blank=True)
    txt_cancel_reason = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "sub_licences"
        unique_together = (
            "cod_licence_package",
            "id_third_party",
            "dat_licence_from",
        )

    def __str__(self):
        return f"{self.cod_licence_package} - {self.id_third_party}"
    
class SubPackageRoles(models.Model):
    id = models.AutoField(primary_key=True)
    # ---- Composite key fields ----
    cod_licence_package = models.CharField(max_length=4)

    cod_user_role = models.ForeignKey('roles.SecUserRoles',on_delete=models.SET_NULL,null=True,blank=True,
        related_name='licence_package_roles')
    
    dat_effective_from = models.DateField(null=True, blank=True)
    dat_effective_to = models.DateField(null=True, blank=True)
    flg_default_value = models.CharField(max_length=1,choices=YES_NO,default='N')
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS)
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_updated')

    class Meta:
        db_table = "sub_package_roles"
        unique_together = (
            "cod_licence_package",
            "cod_user_role",
        )

    def __str__(self):
        return f"{self.cod_licence_package} - {self.cod_user_role}"
    
class SubLicencesHist(models.Model):

    id = models.AutoField(primary_key=True)

    # ----- Composite key fields -----
    cod_licence_package = models.CharField(max_length=4)

    id_third_party = models.ForeignKey('campaign.MstThirdParties', null=True,blank=True,on_delete=models.SET_NULL,
        related_name='licence_history_thirdparty'
    )

    dat_licence_from = models.DateField()
    dat_time_change = models.DateTimeField()

    # ----- Audit -----
    txt_change_made_by = models.ForeignKey(
        'user.SecUserMaster',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='licence_history_changes'
    )

    # ----- Licence Details -----
    dat_licence_to = models.DateField(null=True, blank=True)

    txt_licence_key = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    cod_default_role = models.ForeignKey(
        'roles.SecUserRoles',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='licence_history_default_role'
    )

    num_max_users = models.SmallIntegerField(null=True, blank=True)
    num_max_locations = models.SmallIntegerField(null=True, blank=True)
    num_tier = models.SmallIntegerField(null=True, blank=True)

    id_questionnaire = models.ForeignKey(
        'questionnaries.CmpQuestionnaire',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='licence_history_questionnaire'
    )

    id_campaign = models.ForeignKey(
        'campaign.CmpCampaigns',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='licence_history_campaign'
    )

    dat_licence_applied = models.DateField(null=True, blank=True)
    txt_licence_applied_by_id = models.ForeignKey(
        'user.SecUserMaster',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='licence_history_licence_applied'
    )

    dat_licence_ratified = models.DateField(null=True, blank=True)
    txt_licence_ratified_by_id = models.ForeignKey(
        'user.SecUserMaster',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='licence_history_licence_ratified'
    )

    flg_licence_ratified = models.CharField(
        max_length=1,
        choices=YES_NO,
        null=True,
        blank=True
    )

    cod_currency = models.ForeignKey(
        'masters.MstCurrency',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='licence_history_currency'
    )

    amt_rack_rate = models.FloatField(null=True, blank=True)
    amt_charged_rate = models.FloatField(null=True, blank=True)

    enu_billing_frequency = models.CharField(
        max_length=1,
        choices=BILLING_FREQUENCY,
        null=True,
        blank=True
    )

    txt_sale_closed_by_id = models.ForeignKey(
        'user.SecUserMaster',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='licence_history_sale_closed'
    )

    txt_sale_approved_by_id = models.ForeignKey(
        'user.SecUserMaster',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='licence_history_sale_approved'
    )

    dat_sale_closed = models.DateField(null=True, blank=True)
    dat_sale_approved = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "sub_licences_hist"
        unique_together = (
            "cod_licence_package",
            "id_third_party",
            "dat_licence_from",
            "dat_time_change",
        )

    def __str__(self):
        return f"{self.cod_licence_package} - {self.id_third_party} ({self.dat_time_change})"

class SysOrgChart(models.Model):

    cod_org_unit = models.CharField(max_length=8)
    txt_org_unit_name = models.CharField(max_length=48, null=True, blank=True)
    parent_org_unit = models.ForeignKey("self",on_delete=models.SET_NULL,db_column="parent_org_unit",
        null=True,blank=True,related_name="children")
    
    flg_backoffice = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)
    flg_rollup_unit = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)

    id_parent_company = models.ForeignKey('campaign.MstThirdParties',db_column="id_parent_company",null=True,blank=True,related_name="%(class)s",on_delete=models.DO_NOTHING)

    flg_accept_selfserv_appl = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='Y')
    cod_service_branch = models.CharField(max_length=8, null=True, blank=True)
    txt_ifsc_code = models.CharField(max_length=48, null=True, blank=True)
    txt_addr_line1 = models.CharField(max_length=96, null=True, blank=True)
    txt_addr_line2 = models.CharField(max_length=96, null=True, blank=True)
    txt_addr_line3 = models.CharField(max_length=96, null=True, blank=True)

    txt_addr_city = models.ForeignKey('masters.MstCityClasses',db_column="txt_addr_city",null=True,blank=True,related_name="%(class)s_city",on_delete=models.DO_NOTHING)

    txt_addr_pin = models.ForeignKey('masters.MstPinCodes',db_column="txt_addr_pin",null=True,blank=True,related_name="%(class)s_pincodes",on_delete=models.DO_NOTHING)

    cod_address_state = models.ForeignKey('masters.MstStateCodes',db_column="cod_address_state",null=True,blank=True,related_name="%(class)s_state",on_delete=models.DO_NOTHING)

    cod_addr_country = models.ForeignKey('masters.MstCountryCodes',db_column="cod_addr_country",null=True,blank=True,related_name="%(class)s_country",on_delete=models.DO_NOTHING)

    txt_org_unit_email = models.EmailField(max_length=96, null=True, blank=True)

    txt_org_unit_phone = models.CharField(max_length=16, null=True, blank=True)

    txt_org_manager_id = models.ForeignKey('user.SecUserMaster',db_column="txt_org_manager_id",null=True,blank=True,related_name="%(class)s_manager",on_delete=models.DO_NOTHING)

    txt_credit_officer_id = models.ForeignKey('user.SecUserMaster',db_column="txt_credit_officer_id",null=True,blank=True,related_name="%(class)s_credit_officer",on_delete=models.DO_NOTHING)

    num_clearing_house_gl = models.BigIntegerField(null=True, blank=True)

    cod_storage_location = models.CharField(max_length=4, blank=True, default="")

    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker',db_column='txt_last_maker_id')

    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker',db_column='txt_last_checker_id')

    dat_last_checker = models.DateField(null=True, blank=True)

    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_created')

    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_updated')

    class Meta:
        db_table = "sys_org_chart"
        unique_together = ("cod_org_unit", "cod_rec_status")

    def __str__(self):
        return f"{self.cod_org_unit} - {self.txt_org_unit_name}"