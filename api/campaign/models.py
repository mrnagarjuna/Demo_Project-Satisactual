from django.db import models
from utils.constants.choices import REC_STATUS_CHOICES, YES_NO_CHOICES,AUDIT_PERIODICITY_CHOICES,FOREX_CATEGORY,OFFICE_TYPE,CAMPAIGN_STATUS_CHOICES,TAG_TYPE_CHOICES,STATUS_CHOICES,RESPONSE_STATUS_CHOICES,GENDER_CHOICES,RESPONSE_CLASS
from django.utils import timezone
from utils.management.file_rename import upload_to_logo_image,upload_to_third_Party,upload_to_third_Party_poa



class MstCampaignTypes(models.Model):
    cod_campaign_type = models.CharField(max_length=7,null=True,blank=True)
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')
    txt_campaign_type_desc = models.CharField(max_length=96, null=True, blank=True)
    flg_sales_campaign = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_employee_survey = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    num_min_size_for_reporting = models.SmallIntegerField(default=25)
    flg_dnc_scrub_reqd = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_structured = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_response_reqd = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_targetlist_mandatory = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)

    flg_cawi = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_cati = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_capi = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True, related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True, related_name='%(class)s_checker')
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
        db_table = 'mst_campaign_types'
        unique_together = ('cod_campaign_type', 'cod_rec_status')  # composite primary key

class MstCampaignTeamRole(models.Model):
    cod_team_role = models.CharField(max_length=4)
    txt_role_name = models.CharField(max_length=48, null=True, blank=True)
    flg_certification_required = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)
    flg_rating_allowed = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)
    flg_default_value = models.CharField( max_length=1, choices=YES_NO_CHOICES, default='N')
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A' )
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    class Meta:
        db_table = "mst_campaign_team_role"
        unique_together = ('cod_team_role', 'cod_rec_status')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cod_team_role} - {self.txt_role_name}"

class MstThirdPartyTypes(models.Model):
    cod_third_party_type = models.CharField(max_length=4)
    txt_third_party_type_desc = models.CharField(max_length=48, null=True, blank=True)

    flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_credit_bureau = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_vendor_agency = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_builder_developer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_regulator = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_employer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_client_entity = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_authentication_agency = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_distributor_agency = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_auditor = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_lawyer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_clearing_house = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_insurer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_accredited_university = models.CharField(
        max_length=1, choices=YES_NO_CHOICES, null=True, blank=True
    )

    cod_rec_status = models.CharField(
        max_length=1, choices=REC_STATUS_CHOICES, default='A'
    )

    txt_last_maker_id = models.ForeignKey(
        'user.SecUserMaster',
        to_field='txt_login_id',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_maker'
    )
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey(
        'user.SecUserMaster',
        to_field='txt_login_id',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_checker'
    )
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        elif self.txt_last_checker_id:
            
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'mst_third_party_types'
        unique_together = ('cod_third_party_type', 'cod_rec_status')
        verbose_name = 'Third Party Type'
        verbose_name_plural = 'Third Party Types'

    def __str__(self):
        return f"{self.cod_third_party_type} - {self.txt_third_party_type_desc}"
    
class MstThirdParties(models.Model):
    id_third_party = models.BigAutoField(primary_key=True)

    cod_third_party_type = models.ForeignKey(MstThirdPartyTypes,on_delete=models.SET_NULL,null=True,blank=True,related_name='third_parties')

    txt_third_party_name = models.CharField(max_length=255, null=True, blank=True)
    txt_third_party_short_name = models.CharField(max_length=48, null=True, blank=True)

    flg_credit_bureau = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_vendor_agency = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_builder_developer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_regulator = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_employer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_client_entity = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_authentication_agency = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_distributor_agency = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_auditor = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_lawyer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_clearing_house = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_insurer = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_accredited_university = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    txt_our_id = models.CharField(max_length=48, null=True, blank=True)

    flg_msg_xchg_available = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    txt_msg_xchg_ip_address = models.CharField(max_length=96, null=True, blank=True)
    txt_msg_xchg_port_num = models.SmallIntegerField(null=True, blank=True)
    txt_msg_xchg_protocol = models.CharField(max_length=48, null=True, blank=True)
    txt_msg_xchg_user_id = models.CharField(max_length=48, null=True, blank=True)
    txt_msg_xchg_signature = models.CharField(max_length=48, null=True, blank=True)

    txt_msg_send_format = models.CharField(max_length=48, null=True, blank=True)
    txt_msg_recv_format = models.CharField(max_length=48, null=True, blank=True)
    txt_file_send_format = models.CharField(max_length=48, null=True, blank=True)
    txt_file_recv_format = models.CharField(max_length=48, null=True, blank=True)
    txt_file_send_folder = models.CharField(max_length=255, null=True, blank=True)
    txt_file_recv_folder = models.CharField(max_length=255, null=True, blank=True)

    num_min_score_possible = models.SmallIntegerField(null=True, blank=True)
    num_max_score_possible = models.SmallIntegerField(null=True, blank=True)

    txt_principal_contact_name = models.CharField(max_length=96, null=True, blank=True)

    txt_addr_line1 = models.CharField(max_length=96, null=True, blank=True)
    txt_addr_line2 = models.CharField(max_length=96, null=True, blank=True)
    txt_addr_line3 = models.CharField(max_length=96, null=True, blank=True)
    txt_addr_city = models.CharField(max_length=96, null=True, blank=True)
    txt_addr_pin = models.CharField(max_length=8, null=True, blank=True)
    cod_address_state = models.ForeignKey('masters.MstStateCodes',on_delete=models.SET_NULL,null=True,blank=True,related_name='third_party_state')
    cod_addr_country = models.ForeignKey('masters.MstCountryCodes',on_delete=models.SET_NULL,null=True,blank=True,related_name='third_party_state')
    dat_addr_effective = models.DateField(null=True, blank=True)

    txt_phone_num = models.CharField(max_length=48, null=True, blank=True)
    txt_email_id = models.CharField(max_length=96, null=True, blank=True)
    txt_org_url = models.CharField(max_length=96, null=True, blank=True)

    txt_escalation_1_name = models.CharField(max_length=96, null=True, blank=True)
    txt_escalation_1_phone = models.CharField(max_length=48, null=True, blank=True)
    txt_escalation_1_email = models.CharField(max_length=96, null=True, blank=True)
    txt_escalation_1_title = models.CharField(max_length=96, null=True, blank=True)

    txt_escalation_2_name = models.CharField(max_length=96, null=True, blank=True)
    txt_escalation_2_phone = models.CharField(max_length=48, null=True, blank=True)
    txt_escalation_2_email = models.CharField(max_length=96, null=True, blank=True)
    txt_escalation_2_title = models.CharField(max_length=96, null=True, blank=True)

    txt_registration_num = models.CharField(max_length=48, null=True, blank=True)
    dat_registration = models.DateField(null=True, blank=True)

    num_gl_acct = models.IntegerField(null=True, blank=True)

    bin_third_party_logo = models.ImageField(upload_to=upload_to_third_Party, null=True, blank=True)
    flg_poa_received = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    bin_poa_doc = models.ImageField(upload_to=upload_to_third_Party_poa, null=True, blank=True)
    cod_id_proof_doctyp = models.CharField(max_length=4, null=True, blank=True)
    txt_id_proof_docnum = models.CharField(max_length=48, null=True, blank=True)
    id_issuer = models.BigIntegerField(null=True, blank=True)
    txt_id_proof_issuer = models.CharField(max_length=96, null=True, blank=True)

    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_last_maker_id = models.ForeignKey(
        'user.SecUserMaster',
        to_field='txt_login_id',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey(
        'user.SecUserMaster',
        to_field='txt_login_id',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_checker')
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
        db_table = 'mst_third_parties'
        unique_together = ('id_third_party', 'cod_rec_status')

class CmpCampaigns(models.Model):
    id = models.BigAutoField(primary_key=True)

    txt_campaign_name = models.CharField(max_length=96, null=True, blank=True)
    txt_campaign_short_code = models.CharField(max_length=48, null=True, blank=True)
    txt_campaign_title = models.CharField(max_length=96, null=True, blank=True)
    txt_campaign_subtitle = models.CharField(max_length=96, null=True, blank=True)
    txt_campaign_desc = models.TextField(null=True, blank=True)

    cod_campaign_type = models.ForeignKey(MstCampaignTypes,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='campaign')

    enu_campaign_status = models.CharField(max_length=1,choices=CAMPAIGN_STATUS_CHOICES,default='D')

    flg_model_campaign = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_targeted_list = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)

    dat_start = models.DateField(null=True, blank=True)
    dat_end = models.DateField(null=True, blank=True)

    txt_camp_mgr_id = models.ForeignKey('user.SecUserMaster',db_column='txt_camp_mgr_id',on_delete=models.SET_NULL,null=True,blank=True,
        related_name='%(class)s_manager')
    
    id_commissioned_by_thirdparty = models.ForeignKey(MstThirdParties,null=True,blank=True,related_name='campaigns',on_delete=models.DO_NOTHING)

    bin_logo_to_display = models.ImageField(upload_to=upload_to_logo_image, null=True, blank=True)

    cod_department = models.ForeignKey('masters.MstDepartments',on_delete=models.DO_NOTHING,null=True,blank=True,related_name='campaign')
    txt_invoice_sent_to_id = models.ForeignKey(
    'user.SecUserMaster',
    #to_field='txt_login_id',
    db_column='txt_invoice_sent_to_id',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='invoice_campaigns',
    # db_constraint=False,
    # db_index=False
    )

    cod_language = models.ForeignKey('masters.MstLanguages',on_delete=models.DO_NOTHING,null=True,blank=True,related_name='campaign')
    cod_promo = models.ForeignKey('product.MstPromoCodes',on_delete=models.DO_NOTHING,null=True,blank=True,related_name='campaign')
    cod_product = models.ForeignKey('product.MstProdCodes',on_delete=models.DO_NOTHING,null=True,blank=True,related_name='campaign')

    flg_voice_recording_consent = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_video_recording_consent = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_nonconsent_terminate = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_anonymize_names = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_anonymous_response_check = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_allow_clarif_contact_check = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_allow_secure_print = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_proof_before_submit = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_invite_bids = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    num_tot_response_reqd = models.IntegerField(null=True, blank=True)
    num_attempts_per_item = models.SmallIntegerField(default=6)
    num_hours_between_attempts = models.SmallIntegerField(default=24)
    num_archival_months = models.SmallIntegerField(default=24)

    num_est_target_population = models.IntegerField(null=True, blank=True)
    num_confidence_level = models.FloatField(default=97)
    num_margin_of_error = models.FloatField(default=5)
    num_z_score_calc = models.FloatField(null=True, blank=True)
    num_sample_size = models.IntegerField(null=True, blank=True)
    num_est_contact_pct = models.SmallIntegerField(null=True, blank=True)
    num_est_response_pct = models.FloatField(null=True, blank=True)
    num_est_apply_pct = models.FloatField(null=True, blank=True)
    num_est_purchase_pct = models.SmallIntegerField(null=True, blank=True)
    amt_est_rev_per_purchase = models.FloatField(null=True, blank=True)

    txt_created_by_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,
        related_name='%(class)s_created')
    
    dat_created = models.DateField(null=True, blank=True)

    id_qa_review_proc = models.ForeignKey('campaign.MstQAReviewProcedure',on_delete=models.SET_NULL,null=True,blank=True,related_name="qa_reviews",db_column="id_qa_review_proc")

    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_createdd')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "cmp_campaigns"
        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"

    def __str__(self):
        return f"{self.id} - {self.txt_campaign_name}"

class CmpCampaignUserGeoCoverage(models.Model):
    txt_login_id = models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.DO_NOTHING,related_name='campaign_geo_coverage')
    id_campaign = models.ForeignKey(CmpCampaigns,null=True,blank=True,on_delete=models.DO_NOTHING,related_name='campaign_geo_coverage')
    cod_country = models.ForeignKey('masters.MstCountryCodes',null=True,blank=True,on_delete=models.DO_NOTHING,related_name='campaign_geo_coverage')
    cod_state = models.ForeignKey('masters.MstStateCodes',null=True,blank=True,on_delete=models.DO_NOTHING,related_name='campaign_geo_coverage')
    cod_district = models.ForeignKey('masters.MstDistrictCodes',null=True,blank=True,on_delete=models.DO_NOTHING,related_name='campaign_geo_coverage')
    txt_city_name = models.CharField(max_length=96, default='')
    cod_pin_code = models.ForeignKey('masters.MstPinCodes',null=True,blank=True,on_delete=models.DO_NOTHING,related_name='campaign_geo_coverage')

    num_priority_sequence = models.SmallIntegerField(default=1)
    num_allocated = models.SmallIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "cmp_campaign_user_geo_coverage"
        verbose_name = "Campaign User Geo Coverage"
        verbose_name_plural = "Campaign User Geo Coverage"
        unique_together = (
            "txt_login_id",
            "cod_country",
            "cod_state",
            "cod_district",
            "txt_city_name",
            "cod_pin_code",
            "id_campaign",
        )

    def __str__(self):
        return f"{self.txt_login_id} | Campaign {self.id_campaign}"
    
class CmpWaves(models.Model):
    id_campaign = models.OneToOneField(CmpCampaigns,on_delete=models.PROTECT,null=True,blank=True,related_name='wave')
    # id_campaign_wave = models.BigAutoField()
    txt_campaign_wave_name = models.CharField(max_length=96, null=True, blank=True)
    id_contact_list = models.ForeignKey('contact.CmpContactList',on_delete=models.SET_NULL,null=True,blank=True,db_column='id_contact_list',related_name='waves')
    dat_wave_start = models.DateField(null=True, blank=True)
    dat_wave_end = models.DateField(null=True, blank=True)


    txt_wave_delivery_head_id = models.ForeignKey('user.SecUserMaster',on_delete=models.DO_NOTHING,null=True,blank=True,related_name='wave_delivery_head',db_column='txt_wave_delivery_head_id')
    txt_wave_requisitioner_id = models.ForeignKey('user.SecUserMaster',null=True,blank=True,related_name='wave_requisitioner',on_delete=models.DO_NOTHING,db_column='txt_wave_requisitioner_id')

    id_questionnaire = models.ForeignKey('questionnaries.CmpQuestionnaire',on_delete=models.SET_NULL,null=True,
        blank=True,db_column='id_questionnaire',related_name='waves')

    flg_one_question_format = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')

    num_tot_response_reqd = models.IntegerField(null=True, blank=True)

    num_escalation_levels = models.SmallIntegerField(default=0)
    num_hours_to_escalation = models.SmallIntegerField(default=48)

    num_low_rating_below = models.SmallIntegerField(default=6)
    num_high_rating_above = models.SmallIntegerField(default=9)

    cod_css_theme = models.ForeignKey('masters.SysCssTheme',on_delete=models.SET_NULL,null=True,blank=True,
        db_column='cod_css_theme',related_name='waves')

    flg_test_wave = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True, blank=True)
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
        db_table = "cmp_waves"
        verbose_name = "Campaign Wave"
        verbose_name_plural = "Campaign Waves"

        unique_together = (
            "id_campaign",
        )

    def __str__(self):
        return f"Campaign {self.id_campaign} | Wave {self.id_campaign_wave}"

class MstQAReviewProcedure(models.Model):
    id_proc = models.BigAutoField(primary_key=True)
    txt_proc_name = models.CharField(max_length=96, unique=True)

    class Meta:
        db_table = "mst_qa_review_procedures"

    def __str__(self):
        return self.txt_proc_name


class CmpTeam(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_campaign = models.ForeignKey(CmpCampaigns,on_delete=models.CASCADE,related_name='team_members',null=True,blank=True)
    txt_login_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.CASCADE,related_name='campaign_teams',null=True,blank=True)

    cod_campaign_role = models.SmallIntegerField(null=True,blank=True)
    txt_campaign_role = models.CharField(max_length=48, null=True, blank=True)

    dat_joined_team = models.DateField(null=True, blank=True)
    dat_left_team = models.DateField(null=True, blank=True)

    flg_campaign_approval_reqd = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_questionnaire_approval_reqd = models.CharField( max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_script_approval_reqd = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_flyer_approval_reqd = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    flg_administrator = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_caller_role = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_allow_response_submit = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    dat_campaign_approval_rqstd = models.DateField(null=True, blank=True)
    dat_questionnaire_approval_rqstd = models.DateField(null=True, blank=True)
    dat_script_approval_rqstd = models.DateField(null=True, blank=True)
    dat_flyer_approval_rqstd = models.DateField(null=True, blank=True)

    dat_campaign_approved = models.DateField(null=True, blank=True)
    dat_questionnaire_approved = models.DateField(null=True, blank=True)
    dat_script_approved = models.DateField(null=True, blank=True)
    dat_flyer_approved = models.DateField(null=True, blank=True)

    cod_preferred_lang = models.ForeignKey('masters.MstLanguages',on_delete=models.SET_NULL,related_name='cam_team_lang',null=True,blank=True)

    num_contacts_capacity = models.SmallIntegerField(null=True, blank=True)
    num_batch_size = models.SmallIntegerField(null=True, blank=True)

    flg_escalation_notice = models.CharField(
        max_length=1, choices=YES_NO_CHOICES, null=True, blank=True
    )
    num_level_escalation = models.SmallIntegerField(null=True, blank=True)

    cod_rec_status = models.CharField(
        max_length=1, choices=REC_STATUS_CHOICES, default='A', db_index=True
    )

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    class Meta:
        db_table = 'cmp_team'
        unique_together = (
            'id_campaign',
            'txt_login_id',
            'cod_rec_status',
        )
        indexes = [
            models.Index(fields=['id_campaign']),
            models.Index(fields=['txt_login_id']),
        ]

    def __str__(self):
        return f"{self.txt_login_id} - {self.id_campaign}"
    
class SysPersonalizationTags(models.Model):
    id = models.BigAutoField(primary_key=True)

    cod_tag = models.CharField(max_length=4)
    txt_tag = models.CharField(max_length=48)
    txt_tag_description = models.CharField(max_length=96, null=True, blank=True)

    enu_tag_type = models.CharField(max_length=1,choices=TAG_TYPE_CHOICES,null=True,blank=True)

    num_display_sequence = models.SmallIntegerField(null=True, blank=True)

    cod_rec_status = models.CharField( max_length=1,choices=REC_STATUS_CHOICES,default='A',db_index=True)

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    class Meta:
        db_table = 'sys_personalization_tags'
        unique_together = (
            'cod_tag',
            'cod_rec_status',
        )
        ordering = ['num_display_sequence', 'cod_tag']

    def __str__(self):
        return f"{self.cod_tag} - {self.txt_tag}"
    
class CmpCampaignScripts(models.Model):
    id = models.BigAutoField(primary_key=True)

    id_campaign = models.ForeignKey('campaign.CmpCampaigns',on_delete=models.CASCADE,related_name='scripts',null=True,blank=True
    )

    id_campaign_wave = models.ForeignKey('campaign.CmpWaves',on_delete=models.CASCADE,related_name='scripts',
        null=True,blank=True 
    )
    # id_campaign_wave=models.SmallIntegerField(null=True,blank=True)
    cod_channel = models.ForeignKey('contact.MstContactChannel',null=True,blank=True,on_delete=models.DO_NOTHING,
        related_name='campaign_scripts')
    

    cod_language = models.ForeignKey('masters.MstLanguages',on_delete=models.DO_NOTHING,null=True,blank=True,related_name='campaign_scripts')

    txt_intro_script = models.TextField(null=True, blank=True)
    txt_ack_script = models.TextField(null=True, blank=True)
    txt_not_qualified_script = models.TextField(null=True, blank=True)

    txt_flyer_file = models.CharField(max_length=255, null=True, blank=True)

    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A',db_index=True)

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    class Meta:
        db_table = 'cmp_campaign_scripts'
        unique_together = (
            'id_campaign',
            'cod_channel',
            'cod_language',
            'cod_rec_status',
        )
        indexes = [
            models.Index(fields=['id_campaign']),
            models.Index(fields=['cod_channel']),
            models.Index(fields=['cod_language']),
        ]

    def __str__(self):
        return f"{self.id_campaign} | {self.cod_channel} | {self.cod_language}"
    
class CmpCampaignGeoCoverage(models.Model):

    id_campaign = models.ForeignKey(CmpCampaigns,null=True,blank=True,on_delete=models.DO_NOTHING,related_name='geo_coverage')
    cod_country = models.ForeignKey('masters.MstCountryCodes',null=True,blank=True,on_delete=models.DO_NOTHING,related_name='geo_coverage')
    cod_state = models.ForeignKey('masters.MstStateCodes',null=True,blank=True,on_delete=models.DO_NOTHING,related_name='geo_coverage')
    cod_district = models.ForeignKey('masters.MstDistrictCodes',null=True,blank=True,on_delete=models.DO_NOTHING,related_name='geo_coverage')
    txt_city_name = models.CharField(max_length=96,)
    cod_pin_code = models.ForeignKey('masters.MstPinCodes',null=True,blank=True,on_delete=models.DO_NOTHING,related_name='geo_coverage')

    num_responses_reqd = models.PositiveSmallIntegerField(null=True,blank=True)

    class Meta:
        db_table = "cmp_campaign_geo_coverage"

        unique_together = (
            "id_campaign",
            "cod_country",
            "cod_state",
            "cod_district",
            "txt_city_name",
            "cod_pin_code",
        )

    def __str__(self):
        return f"{self.id_campaign} - {self.txt_city_name}"
    
class CmpSegment(models.Model):

    id_campaign = models.ForeignKey(CmpCampaigns,on_delete=models.DO_NOTHING,null=True,blank=True,related_name="cmp_segments",db_column="id_campaign")

    txt_segment_name = models.CharField(max_length=48)

    num_segment_sequence = models.IntegerField(null=True, blank=True)

    id_qualifying_question = models.ForeignKey('questionnaries.CmpQuestion',related_name='cmp_segments',null=True,blank=True,on_delete=models.SET_NULL,db_column="id_qualifying_question")

    num_segment_response_reqd = models.SmallIntegerField(null=True,blank=True)

    num_contact_list_col = models.ForeignKey('contact.CmpContactListColumns',db_column='num_contact_list_col',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_segment')

    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')

    dat_last_maker = models.DateField(null=True, blank=True)
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    class Meta:
        db_table = "cmp_segments"
        unique_together = (
            "id_campaign",
            "cod_rec_status",
            "txt_segment_name"
        )

    def __str__(self):
        return self.txt_segment_name
    
class CmpSegmentSize(models.Model):

    id_campaign = models.ForeignKey(CmpCampaigns,on_delete=models.DO_NOTHING,db_column="id_campaign",related_name="segment_sizes",null=True,blank=True)

    txt_segment_name = models.ForeignKey(CmpSegment,on_delete=models.DO_NOTHING,db_column="txt_segment_name",related_name="segment_sizes",null=True,blank=True)

    cod_option = models.ForeignKey("questionnaries.CmpQuestionOptions",on_delete=models.DO_NOTHING,db_column="cod_option",related_name="segment_sizes",null=True,blank=True)

    num_population_size = models.SmallIntegerField(null=True,blank=True)

    num_segment_response_reqd = models.SmallIntegerField(null=True,blank=True)

    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default="A",)

    txt_last_maker_id = models.ForeignKey("user.SecUserMaster",to_field='txt_login_id',null=True,blank=True,on_delete=models.CASCADE,db_column="txt_last_maker_id",related_name="segment_size_maker")

    txt_last_checker_id = models.ForeignKey("user.SecUserMaster",to_field='txt_login_id',null=True,blank=True,on_delete=models.CASCADE,db_column="txt_last_checker_id",related_name="segment_size_checker")

    dat_last_maker = models.DateField(null=True, blank=True)
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    class Meta:
        db_table = "cmp_segments_sizes"
        unique_together = (
            "id_campaign",
            "txt_segment_name",
            "cod_rec_status",
            "cod_option",
        )

    def __str__(self):
        return f"{self.id_campaign} - {self.txt_segment_name}"
    
class CmpCampaignXChannels(models.Model):
    id_campaign = models.ForeignKey(CmpCampaigns,null=True,blank=True,on_delete=models.CASCADE,   related_name='campaign_x_channel')
    cod_channel = models.ForeignKey('contact.MstContactChannel',null=True,blank=True,on_delete=models.CASCADE,
        related_name='campaign_x_channel')

    dat_start = models.DateField(null=True, blank=True)
    dat_end = models.DateField(null=True, blank=True)

    flg_outbound = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')

    txt_cmp_chnl_manager_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,db_column="txt_cmp_chnl_manager_id",)

    num_channel_response_reqd = models.SmallIntegerField(null=True, blank=True)

    amt_billing_rate_per_contact = models.FloatField(null=True, blank=True)

    cod_channel_redirect_on_fail = models.CharField(max_length=4, null=True, blank=True)
    cod_channel_redirect_on_success = models.CharField(max_length=4, null=True, blank=True)
    cod_channel_redirect_no_response = models.CharField(max_length=4, null=True, blank=True)

    num_hours_no_response_wait = models.SmallIntegerField(null=True, blank=True)

    txt_email_id_for_send = models.EmailField(null=True, blank=True)
    txt_email_signature = models.CharField(max_length=96, null=True, blank=True)
    txt_send_from_name = models.CharField(max_length=96, null=True, blank=True)
    txt_smtp_client = models.CharField(max_length=48, null=True, blank=True)

    flg_enable_ssl = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)

    num_smtp_port = models.SmallIntegerField(null=True, blank=True)

    txt_send_replies_to_id = models.EmailField(null=True, blank=True)
    txt_bounced_email_redirect_to = models.EmailField(null=True, blank=True)

    txt_pop3_username = models.CharField(max_length=48, null=True, blank=True)
    txt_imap_username = models.CharField(max_length=48, null=True, blank=True)

    class Meta:
        db_table = "cmp_campaign_x_channels"
        unique_together = ('id_campaign', 'cod_channel')

    def __str__(self):
        return f"{self.id_campaign} - {self.cod_channel}"

class CmpCallerCredentials(models.Model):

    txt_login_id = models.ForeignKey('user.SecUserMaster',on_delete=models.DO_NOTHING,null=True,blank=True,related_name='cmp_caller_credentials')
    num_certification_level = models.SmallIntegerField(default=1)

    txt_caller_authorized_by = models.ForeignKey('user.SecUserMaster',on_delete=models.DO_NOTHING,null=True,blank=True,related_name='cmp_caller_credentials_authorized')
    dat_first_certified = models.DateField(null=True, blank=True)
    dat_certificate_valid_to = models.DateField(null=True, blank=True)

    txt_caller_base_city = models.ForeignKey('masters.MstCityClasses',on_delete=models.DO_NOTHING,null=True,blank=True,related_name='cmp_caller_base_city')

    cod_channel = models.ForeignKey('contact.MstContactChannel',on_delete=models.DO_NOTHING,null=True,blank=True,related_name='cmp_caller_credentials_channel')

    num_total_mthly_call_capacity = models.SmallIntegerField(null=True, blank=True)
    num_mthly_valid_call_target = models.SmallIntegerField(null=True, blank=True)

    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')

    txt_last_maker_id = models.ForeignKey("user.SecUserMaster",to_field='txt_login_id',null=True,blank=True,on_delete=models.CASCADE,db_column="txt_last_maker_id",related_name='%(class)s_maker')

    txt_last_checker_id = models.ForeignKey("user.SecUserMaster",to_field='txt_login_id',null=True,blank=True,on_delete=models.CASCADE,db_column="txt_last_checker_id",related_name="%(class)s_checker")

    dat_last_maker = models.DateField(null=True, blank=True)
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    class Meta:
        db_table = "cmp_caller_credentials"
        unique_together = ('txt_login_id', 'cod_rec_status')
        verbose_name = "Caller Credential"

    def __str__(self):
        return f"{self.txt_login_id} - Level {self.num_certification_level}"

class CmpEmail(models.Model):
    id_campaign = models.ForeignKey(CmpCampaigns,on_delete=models.CASCADE,db_column="id_campaign",null=True,blank=True,related_name='%(class)s')
    id_campaign_wave = models.ForeignKey(CmpWaves,on_delete=models.CASCADE,db_column="id_campaign_wave",null=True,blank=True,related_name='%(class)s')
    cod_language = models.ForeignKey("masters.MstLanguages",on_delete=models.PROTECT,db_column="cod_language",null=True,blank=True,related_name='%(class)s')
    cod_channel = models.ForeignKey("contact.MstContactChannel",on_delete=models.PROTECT,db_column="cod_channel",null=True,blank=True,related_name='%(class)s')
    enu_status = models.CharField(max_length=1,choices=STATUS_CHOICES,null=True,blank=True)
    txt_subject_line = models.CharField(max_length=96, null=True, blank=True)
    txt_email = models.TextField(null=True, blank=True)
    txt_signature_line = models.TextField(null=True, blank=True)
    flg_attach_flyer = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)
    txt_addl_detail_url = models.CharField(max_length=255, null=True, blank=True)
    txt_bkgrd_img_url = models.CharField(max_length=255, null=True, blank=True)
    txt_sender_email_id = models.CharField(max_length=48, null=True, blank=True)
    txt_send_replies_to_id = models.CharField(max_length=48, null=True, blank=True)
    dat_time_delay_until = models.DateTimeField(null=True, blank=True)
    dat_time_expires_after = models.DateTimeField(null=True, blank=True)
    flg_include_unsubscribe_link = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)
    txt_unsubscribe_url = models.CharField(max_length=255, null=True, blank=True)
    txt_unsubscribe = models.CharField(max_length=255, null=True, blank=True)
    flg_include_no_replies = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)
    txt_noreplies = models.CharField(max_length=255, null=True, blank=True)
    flg_request_read_receipt = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='Y')
    flg_request_delivery_receipt = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='Y')
    txt_composed_by_id = models.ForeignKey('user.SecUserMaster',db_column="txt_composed_by_id",on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_composed')
    dat_composed = models.DateField(null=True, blank=True)
    txt_approved_by_id = models.ForeignKey('user.SecUserMaster',db_column="txt_approved_by_id",on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_approved')
    dat_approved = models.DateField(null=True, blank=True)
    num_hours_1st_reminder = models.SmallIntegerField(default=72)
    num_hours_2nd_reminder = models.SmallIntegerField(default=168)
    num_reminders = models.SmallIntegerField(default=2)
    flg_include_password = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    id_key_question = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = "cmp_email"
        unique_together = (
            "id_campaign",
            "id_campaign_wave",
            "cod_language",
            "cod_channel",
        )

    def __str__(self):
        return f"{self.id_campaign} - {self.cod_channel}"
    
# from django.db import models


# class CmpResponse(models.Model):
#     campaign_wave = models.ForeignKey(
#         "CmpWaves",
#         on_delete=models.CASCADE,
#         db_constraint=False,   # because composite FK
#         related_name="responses"
#     )

#     id_campaign = models.BigIntegerField()
#     id_campaign_wave = models.BigIntegerField()

#     id_response = models.BigIntegerField()

#     enu_response_status = models.CharField(
#         max_length=1,
#         choices=RESPONSE_STATUS_CHOICES,
#         null=True,
#         blank=True
#     )

#     flg_inbound_origin = models.CharField(
#         max_length=1,
#         choices=YES_NO_CHOICES,
#         default='N'
#     )

#     id_contact_list = models.BigIntegerField(null=True, blank=True)
#     num_list_item = models.BigIntegerField(null=True, blank=True)
#     num_contact_sequence = models.IntegerField(default=0)

#     cod_location = models.CharField(max_length=8, null=True, blank=True)

#     txt_survey_conducted_by = models.CharField(max_length=48)

#     txt_email_id = models.EmailField(max_length=96, null=True, blank=True)
#     txt_phone_number_contacted = models.CharField(max_length=48, null=True, blank=True)

#     dat_time_survey_start = models.DateTimeField(null=True, blank=True)
#     dat_time_survey_end = models.DateTimeField(null=True, blank=True)

#     num_latitude_start = models.FloatField(null=True, blank=True)
#     num_longitude_start = models.FloatField(null=True, blank=True)
#     num_latitude_end = models.FloatField(null=True, blank=True)
#     num_longitude_end = models.FloatField(null=True, blank=True)

#     cod_channel = models.CharField(max_length=4, null=True, blank=True)
#     cod_language = models.CharField(max_length=4, null=True, blank=True)

#     txt_device_id = models.CharField(max_length=96, null=True, blank=True)
#     txt_ip_address = models.CharField(max_length=48, null=True, blank=True)
#     txt_browser_used = models.CharField(max_length=48, null=True, blank=True)
#     txt_os_used = models.CharField(max_length=48, null=True, blank=True)
#     txt_user_agent_string = models.TextField(null=True, blank=True)

#     txt_responder_name = models.CharField(max_length=96, null=True, blank=True)
#     num_responder_age = models.SmallIntegerField(null=True, blank=True)
#     enu_responder_gender = models.CharField(
#         max_length=3,
#         choices=GENDER_CHOICES,
#         null=True,
#         blank=True
#     )

#     flg_email_delivered = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_email_opened = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
#     flg_email_clicked = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)

#     dat_time_msg_sent = models.DateTimeField(null=True, blank=True)
#     txt_bounce_reason = models.CharField(max_length=255, null=True, blank=True)

#     enu_response_class = models.CharField(
#         max_length=1,
#         choices=RESPONSE_CLASS,
#         default='M'
#     )
#     num_response_score = models.SmallIntegerField(null=True, blank=True)
#     num_sentiment_score = models.FloatField(null=True, blank=True)

#     dat_qa_review = models.DateField(null=True, blank=True)
#     txt_qa_review_by_id = models.CharField(max_length=48, null=True, blank=True)

#     txt_survey_token = models.CharField(max_length=48, null=True, blank=True)


#     class Meta:
#         db_table = "cmp_response"
#         unique_together = (
#             "id_campaign",
#             "id_campaign_wave",
#             "id_response",
#         )

#     def __str__(self):
#         return f"{self.id_campaign}-{self.id_campaign_wave}-{self.id_response}"