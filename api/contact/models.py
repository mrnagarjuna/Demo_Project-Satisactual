from django.db import models
from utils.constants.choices import REC_STATUS_CHOICES, YES_NO_CHOICES,AUDIT_PERIODICITY_CHOICES,FOREX_CATEGORY,OFFICE_TYPE,AUDIT_FREQ_CHOICES,BASE_COLL_TYPE_CHOICES,DEPR_METHOD_CHOICES,REVIEW_FREQ_CHOICES,BASE_CHANNEL_CHOICES,MAIL_PROTOCOL_CHOICES,COL_DISPLAY_TYPE_CHOICES
from django.utils import timezone

class MstContactChannel(models.Model):
    cod_channel = models.CharField(max_length=4)
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_channel_desc = models.CharField(max_length=48, null=True, blank=True)

    flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    enu_base_channel = models.CharField(max_length=4, choices=BASE_CHANNEL_CHOICES, null=True)

    flg_email_supported = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True)
    flg_SMS_supported = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True)
    flg_auto_dialer_supported = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True)

    cod_auto_dialer = models.CharField(max_length=4, null=True, blank=True)

    enu_mail_protocol = models.CharField(max_length=1, choices=MAIL_PROTOCOL_CHOICES, default='S')
    txt_email_id_for_send = models.CharField(max_length=48, null=True, blank=True)
    txt_email_signature = models.TextField(null=True, blank=True)
    txt_email_signature_2fa = models.TextField(null=True, blank=True)
    txt_smtp_client = models.CharField(max_length=255, null=True, blank=True)

    flg_enable_ssl = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True)
    num_smtp_port = models.SmallIntegerField(default=25)

    txt_pop3_username = models.CharField(max_length=48, null=True, blank=True)
    txt_pop3_client = models.CharField(max_length=255, null=True, blank=True)
    num_pop3_port = models.SmallIntegerField(default=995)
    txt_pop3_encryption = models.CharField(max_length=4, null=True, blank=True)

    txt_imap_username = models.CharField(max_length=48, null=True, blank=True)
    txt_imap_client = models.CharField(max_length=255, null=True, blank=True)
    num_imap_port = models.SmallIntegerField(default=993)
    txt_imap_encryption = models.CharField(max_length=4, null=True, blank=True)

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
        db_table = "mst_contact_channel"
        unique_together = ('cod_channel', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_channel} - {self.txt_channel_desc}"
    
class MstContactOutcome(models.Model):
    cod_contact_outcome = models.CharField(max_length=4)
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

    txt_contact_outcome_desc = models.CharField(max_length=96, null=True, blank=True)
    cod_parent_outcome = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True,related_name='child_contact_outcome')

    enu_base_channel_type = models.CharField(max_length=4, choices=BASE_CHANNEL_CHOICES, null=True)

    flg_valid_outcome = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_retry = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_use_for_followup = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='Y')
    flg_outbound = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

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
        db_table = "mst_contact_outcome"
        unique_together = ('cod_contact_outcome', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_contact_outcome} - {self.txt_contact_outcome_desc}"
    
# class MstContractEvents(models.Model):
#     cod_event = models.CharField(max_length=4)
#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

#     txt_event_desc = models.CharField(max_length=48)

#     flg_owners_alerts = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
#     flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

#     txt_last_maker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
#     dat_last_maker = models.DateField(null=True, blank=True)
#     txt_last_checker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.pk:  
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table = "mst_contract_events"
#         unique_together = ('cod_event', 'cod_rec_status')

#     def __str__(self):
#         return f"{self.cod_event} - {self.txt_event_desc}"
    
# class MstContractTypes(models.Model):
#     cod_contract_type = models.CharField(max_length=4)
#     cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')

#     txt_contract_type_desc = models.CharField(max_length=48, null=True, blank=True)
#     flg_default_value = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

#     txt_last_maker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
#     dat_last_maker = models.DateField(null=True, blank=True)
#     txt_last_checker_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
#     dat_last_checker = models.DateField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.pk:  
#             self.dat_last_maker = timezone.now().date()
#         else:
#             self.dat_last_checker = timezone.now().date()
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table = "mst_contract_types"
#         unique_together = ('cod_contract_type', 'cod_rec_status')

#     def __str__(self):
#         return f"{self.cod_contract_type} - {self.txt_contract_type_desc}"

class CmpContactListColumns(models.Model):
    # id_contact_list = models.BigIntegerField()
    num_column = models.SmallIntegerField()

    num_col_starts_at = models.SmallIntegerField(null=True, blank=True)
    num_col_ends_at = models.SmallIntegerField(null=True, blank=True)

    txt_col_header = models.CharField(max_length=96, null=True, blank=True)

    enu_col_display_type = models.CharField(max_length=1,choices=COL_DISPLAY_TYPE_CHOICES,null=True,blank=True)

    flg_segment_identifier = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)

    flg_high_priority = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)

    class Meta:
        db_table = "cmp_contact_list_columns"
        verbose_name = "Contact List Column"
        verbose_name_plural = "Contact List Columns"
        unique_together = ( 'num_column',)

    def __str__(self):
        return f"{self.num_column}"
    
from django.db import models


class CmpContactList(models.Model):
   
    id_contact_list = models.BigAutoField(primary_key=True)

    txt_contact_list_name = models.CharField(max_length=48, null=True, blank=True)

    flg_first_row_headers = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    num_import_from_row = models.SmallIntegerField(default=1)

    flg_delimited = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_tab_delimited = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_pipe_delimited = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_colon_delimited = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_semicolon_delimited = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)

    txt_other_delimters = models.CharField(max_length=48, null=True, blank=True)
    flg_consecutive_delimiters_as_one = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)

    txt_qualifier_char = models.CharField(max_length=4, null=True, blank=True)
    

    num_days_use_by = models.SmallIntegerField(default=0)
    num_days_use_after = models.SmallIntegerField(default=0)

    num_uniq_customer_id_col = models.SmallIntegerField(null=True, blank=True)
    txt_360_view_url = models.CharField(max_length=255, null=True, blank=True)

    # Customer / activity related columns
    num_customer_segment_col = models.SmallIntegerField(null=True, blank=True)
    num_recent_actvty_desc_col = models.SmallIntegerField(null=True, blank=True)
    num_recent_actvty_date_col = models.SmallIntegerField(null=True, blank=True)
    num_recent_actvty_location_col = models.SmallIntegerField(null=True, blank=True)
    num_recent_actvty_channel_col = models.SmallIntegerField(null=True, blank=True)
    num_recent_actvty_prod_col = models.SmallIntegerField(null=True, blank=True)

    num_offer_prod_col = models.SmallIntegerField(null=True, blank=True)
    num_offer_value_col = models.SmallIntegerField(null=True, blank=True)
    num_offer_valid_till_col = models.SmallIntegerField(null=True, blank=True)
    num_offer_price_col = models.SmallIntegerField(null=True, blank=True)
    num_offer_discount_col = models.SmallIntegerField(null=True, blank=True)

    # Personal details
    num_first_name_col = models.SmallIntegerField(null=True, blank=True)
    num_last_name_col = models.SmallIntegerField(null=True, blank=True)
    num_salutation_col = models.SmallIntegerField(null=True, blank=True)
    num_primary_phone_col = models.SmallIntegerField(null=True, blank=True)
    num_alternative_phone_col = models.SmallIntegerField(null=True, blank=True)
    num_email_col = models.SmallIntegerField(null=True, blank=True)

    # Address
    num_addr_line1_col = models.SmallIntegerField(null=True, blank=True)
    num_addr_line2_col = models.SmallIntegerField(null=True, blank=True)
    num_addr_line3_col = models.SmallIntegerField(null=True, blank=True)
    num_city_col = models.SmallIntegerField(null=True, blank=True)
    num_pincode_col = models.SmallIntegerField(null=True, blank=True)
    num_addr_country_col = models.SmallIntegerField(null=True, blank=True)

    # Relationship manager
    num_rel_manager_name_col = models.SmallIntegerField(null=True, blank=True)
    num_rel_manager_email_col = models.SmallIntegerField(null=True, blank=True)
    num_rel_manager_phone_col = models.SmallIntegerField(null=True, blank=True)

    # Employee / misc
    num_preferred_lang_col = models.SmallIntegerField(null=True, blank=True)
    num_emp_designation_col = models.SmallIntegerField(null=True, blank=True)
    num_emp_department_col = models.SmallIntegerField(null=True, blank=True)
    num_emp_reporting_mgr_col = models.SmallIntegerField(null=True, blank=True)
    num_rel_since_date_col = models.SmallIntegerField(null=True, blank=True)

    num_facebookid_col = models.SmallIntegerField(null=True, blank=True)
    num_twitterid_col = models.SmallIntegerField(null=True, blank=True)
    num_dnc_col = models.SmallIntegerField(null=True, blank=True)
    num_pref_time_to_call_col = models.SmallIntegerField(null=True, blank=True)

    num_addl_detail_url_col = models.SmallIntegerField(null=True, blank=True)
    num_bkgrd_img_url_col = models.SmallIntegerField(null=True, blank=True)

    num_columns_in_file = models.SmallIntegerField(null=True, blank=True)

    flg_saved_template = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    txt_template_name = models.CharField(max_length=96, null=True, blank=True)

    dat_time_list_created = models.DateTimeField(null=True, blank=True)
    txt_list_created_by_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_created')

    dat_time_list_reviewed = models.DateTimeField(null=True, blank=True)
    txt_list_reviewed_by_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_reviewed')

    txt_list_owner_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_owned')
    txt_file_source = models.CharField(max_length=48, null=True, blank=True)

    class Meta:
        db_table = "cmp_contact_list"
        verbose_name = "Contact List"
        verbose_name_plural = "Contact Lists"

    def __str__(self):
        return self.txt_contact_list_name or str(self.id_contact_list)




# class CmpContactListEntries(models.Model):
#     id_contact_list = models.ForeignKey(CmpContactList,db_column="id_contact_list",on_delete=models.CASCADE,related_name="entries",null=True,blank=True)
#     num_list_item = models.BigIntegerField()

#     dat_time_uploaded = models.DateTimeField(null=True, blank=True)
#     txt_exclusion_reason = models.CharField(max_length=1024, null=True, blank=True)

#     # TEXT columns (1–32)
#     txt_value_col1 = models.TextField(null=True, blank=True)
#     txt_value_col2 = models.TextField(null=True, blank=True)
#     txt_value_col3 = models.TextField(null=True, blank=True)
#     txt_value_col4 = models.TextField(null=True, blank=True)
#     txt_value_col5 = models.TextField(null=True, blank=True)
#     txt_value_col6 = models.TextField(null=True, blank=True)
#     txt_value_col7 = models.TextField(null=True, blank=True)
#     txt_value_col8 = models.TextField(null=True, blank=True)
#     txt_value_col9 = models.TextField(null=True, blank=True)
#     txt_value_col10 = models.TextField(null=True, blank=True)
#     txt_value_col11 = models.TextField(null=True, blank=True)
#     txt_value_col12 = models.TextField(null=True, blank=True)
#     txt_value_col13 = models.TextField(null=True, blank=True)
#     txt_value_col14 = models.TextField(null=True, blank=True)
#     txt_value_col15 = models.TextField(null=True, blank=True)
#     txt_value_col16 = models.TextField(null=True, blank=True)
#     txt_value_col17 = models.TextField(null=True, blank=True)
#     txt_value_col18 = models.TextField(null=True, blank=True)
#     txt_value_col19 = models.TextField(null=True, blank=True)
#     txt_value_col20 = models.TextField(null=True, blank=True)
#     txt_value_col21 = models.TextField(null=True, blank=True)
#     txt_value_col22 = models.TextField(null=True, blank=True)
#     txt_value_col23 = models.TextField(null=True, blank=True)
#     txt_value_col24 = models.TextField(null=True, blank=True)
#     txt_value_col25 = models.TextField(null=True, blank=True)
#     txt_value_col26 = models.TextField(null=True, blank=True)
#     txt_value_col27 = models.TextField(null=True, blank=True)
#     txt_value_col28 = models.TextField(null=True, blank=True)
#     txt_value_col29 = models.TextField(null=True, blank=True)
#     txt_value_col30 = models.TextField(null=True, blank=True)
#     txt_value_col31 = models.TextField(null=True, blank=True)
#     txt_value_col32 = models.TextField(null=True, blank=True)

#     # cols 33–128 (tinytext → CharField)
#     for i in range(33, 129):
#         locals()[f"txt_value_col{i}"] = models.CharField(max_length=255, null=True, blank=True)

#     # cols 129–250 (varchar(16))
#     for i in range(129, 251):
#         locals()[f"txt_value_col{i}"] = models.CharField(max_length=16, null=True, blank=True)

#     class Meta:
#         db_table = "cmp_contact_list_entries"
#         unique_together = ("id_contact_list", "num_list_item")
        
#         verbose_name = "Contact List Entry"
#         verbose_name_plural = "Contact List Entries"

#     def __str__(self):
#         return f"List {self.id_contact_list_id} - Item {self.num_list_item}"

from django.db import models


class CmpContactListFiles(models.Model):

    id = models.BigAutoField(primary_key=True)

    id_contact_list = models.ForeignKey(CmpContactList,on_delete=models.CASCADE,db_column='id_contact_list',related_name='uploaded_files',null=True,blank=True)
           
    txt_upload_file_path = models.CharField(max_length=255)

    txt_upload_file_name = models.CharField(max_length=255)

    txt_file_uploaded_by_id = models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.SET_NULL,related_name='contact_list_file_uploader')

    dat_time_file_upload_start = models.DateTimeField()
    

    dat_time_file_upload_end = models.DateTimeField(null=True, blank=True)

    num_rows_imported = models.IntegerField(null=True, blank=True)

    num_list_item_start = models.IntegerField(null=True, blank=True)

    num_list_item_end = models.IntegerField(null=True, blank=True)

    txt_template_name = models.CharField(max_length=96, null=True, blank=True)

    dat_time_list_reviewed = models.DateTimeField(null=True, blank=True)

    txt_list_reviewed_by_id = models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.SET_NULL,related_name='contact_list_file_reviewer')

    txt_file_source = models.CharField(max_length=48, null=True, blank=True)

    num_errors = models.SmallIntegerField(null=True, blank=True)

    num_name_missing_error = models.SmallIntegerField(null=True, blank=True)

    num_phone_missing_error = models.SmallIntegerField(null=True, blank=True)

    num_email_missing_error = models.SmallIntegerField(null=True, blank=True)

    num_address_missing_error = models.SmallIntegerField(null=True, blank=True)

    num_typ_mismatch_error = models.SmallIntegerField(null=True, blank=True)

    class Meta:
        db_table = "cmp_contact_list_files"
        unique_together = (
            'id_contact_list',
            'txt_upload_file_path',
            'txt_upload_file_name',
            'dat_time_file_upload_start',
            'txt_file_uploaded_by_id'
        )
        verbose_name = "Contact List File"
        verbose_name_plural = "Contact List Files"

    def __str__(self):
        return f"{self.txt_upload_file_name} - {self.id_contact_list}"

class CmpContactsAssigned(models.Model):

    id_campaign = models.ForeignKey('campaign.CmpCampaigns',on_delete=models.PROTECT,null=True,blank=True,related_name='cmp_contact_assigned')
    id_campaign_wave = models.ForeignKey("campaign.CmpWaves",on_delete=models.CASCADE,null=True,blank=True,db_column="cmp_contact_assigned")
    id_contact_list = models.ForeignKey(CmpContactList,on_delete=models.CASCADE,db_column='id_contact_list',related_name='cmp_contact_assigned',null=True,blank=True)
    num_list_item = models.BigIntegerField()

    txt_assigned_to = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_assigned')
    dat_time_assigned = models.DateTimeField()

    dat_scheduled_contact = models.DateField(null=True, blank=True)
    txt_pref_time_to_call = models.CharField(max_length=48, null=True, blank=True)

    dat_do_not_call_after = models.DateField(null=True, blank=True)

    txt_assigned_by = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_assigned_by')
    flg_do_not_call = models.CharField(
        max_length=1,
        choices=YES_NO_CHOICES,
        default='N'
    )

    txt_last_responder_name = models.CharField(max_length=96, null=True, blank=True)
    txt_last_phone_contacted = models.CharField(max_length=48, null=True, blank=True)

    cod_language = models.ForeignKey("masters.MstLanguages",on_delete=models.SET_NULL,null=True,blank=True,db_column="cod_language")
    cod_pref_channel = models.ForeignKey(MstContactChannel,on_delete=models.SET_NULL,null=True,blank=True,db_column="cod_pref_channel",related_name="contact_assignments")

    id_response = models.BigIntegerField(default=0)

    num_follow_up_level = models.SmallIntegerField(default=0)

    dat_time_alert_email_sent = models.DateTimeField(null=True, blank=True)
    txt_mime_message_id = models.CharField(max_length=255, null=True, blank=True)

    num_hours_gmt_offset = models.FloatField(null=True, blank=True)

    flg_deassigned = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    txt_deassigned_by_id = models.ForeignKey('user.SecUserMaster',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_deassigned_by')
    dat_time_deassigned = models.DateTimeField(null=True, blank=True)
    txt_deassign_reason = models.CharField(max_length=96, null=True, blank=True)

    class Meta:
        db_table = "cmp_contacts_assigned"

        unique_together = (
            'id_campaign',
            'id_campaign_wave',
            'id_contact_list',
            'num_list_item',
            'txt_assigned_to',
            'num_follow_up_level',
        )


    def __str__(self):
        return f"{self.txt_assigned_to} - Contact {self.num_list_item}"