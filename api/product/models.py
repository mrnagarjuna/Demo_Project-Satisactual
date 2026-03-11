from django.db import models
from utils.constants.choices import YES_NO_CHOICES,PRODUCT_TYPE_CHOICES,REC_STATUS_CHOICES,DOC_PURPOSE_CHOICES,REVIEW_FREQ_CHOICES
from django.utils import timezone
from django.db.models import Max


class MstProdCodes(models.Model):
    # Primary Key
    id = models.BigAutoField(primary_key=True)
    # Business Code
    cod_product = models.CharField(max_length=4,unique=True)
    enu_product_type = models.CharField(max_length=3,choices=PRODUCT_TYPE_CHOICES,default='CAS')
    txt_product_name = models.CharField(max_length=48)
    dat_prod_offer_start = models.DateField(null=True, blank=True)
    dat_prod_offer_end = models.DateField(null=True, blank=True)
    cod_currency = models.ForeignKey('masters.MstCurrency',on_delete=models.SET_NULL,null=True,blank=True,
        related_name='prod_codes')
    # Self reference (now uses PK automatically)
    cod_parent_product = models.ForeignKey("self",on_delete=models.SET_NULL,null=True,blank=True,
        related_name="child_product")
    flg_apply_selfserve_mode = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)
    flg_sales_certif_reqd = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    flg_e_stmt_avlbl = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    bin_product_brochure = models.CharField(max_length=255, null=True, blank=True)
    bin_product_soc = models.CharField(max_length=255, null=True, blank=True)
    bin_product_mitc = models.CharField(max_length=255, null=True, blank=True)
    txt_mktg_tag_line = models.CharField(max_length=255, null=True, blank=True)
    id_eligibility_questionnaire = models.BigIntegerField(default=0)
    num_eligibility_score_min = models.SmallIntegerField(default=9999)
    txt_gen_appl_num_func = models.CharField(max_length=255, null=True, blank=True)
    txt_gen_acct_num_func = models.CharField(max_length=255, null=True, blank=True)
    flg_default_value = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,
        related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,
        related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',null=True,blank=True,on_delete=models.CASCADE,related_name='%(class)s_updated')

    # Only timestamp logic remains
    def save(self, *args, **kwargs):
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "mst_prod_codes"
        verbose_name = "Product Code"
        verbose_name_plural = "Product Codes"

    def __str__(self):
        return f"{self.cod_product} - {self.txt_product_name}"

    
class MstProdDisclosures(models.Model):
    cod_disclosure = models.CharField(max_length=4)
    cod_product = models.ManyToManyField(MstProdCodes,blank=True,related_name='prod_disclosures')
    num_sequence = models.SmallIntegerField(null=True, blank=True)
    flg_all_applicants_mandatory = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    flg_guarantors_mandatory = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')
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
        db_table = 'mst_prod_disclosures'
        unique_together = ('cod_disclosure', 'cod_rec_status')
        verbose_name = 'Product Disclosure'
        verbose_name_plural = 'Product Disclosures'

    def __str__(self):
        return f"{self.cod_product} - {self.cod_disclosure}"
    
class MstProdDocs(models.Model):

    cod_doc_type = models.CharField(max_length=4)
    cod_product = models.ManyToManyField('product.MstProdCodes',blank=True,related_name='prod_docs')
    enu_doc_purpose = models.CharField(max_length=1,choices=DOC_PURPOSE_CHOICES,default='I')
    flg_acct_opening_doc = models.CharField(max_length=1,choices=YES_NO_CHOICES)
    num_days_from_acct_opening = models.SmallIntegerField(default=-1)
    flg_renewal_doc = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    enu_post_disb_resubmit_freq = models.CharField(max_length=1,choices=REVIEW_FREQ_CHOICES,default='X')
    flg_mandatory = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True ,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,
    related_name='%(class)s_checker')
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
        db_table = 'mst_prod_docs'
        verbose_name = 'Product Document'
        verbose_name_plural = 'Product Documents'

    def __str__(self):
        return f"{self.cod_doc_type}"
    
class MstPromoCodes(models.Model):

    cod_promo = models.CharField(max_length=4)
    txt_promo_code_desc = models.CharField(max_length=96,null=True,blank=True)
    flg_default_value = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N',null=True,blank=True)
    cod_product = models.ForeignKey(MstProdCodes,on_delete=models.SET_NULL,null=True,blank=True,related_name='product',)
    # 👉 Can be converted to FK(MstProdCodes) later if needed
    dat_promo_start = models.DateField(null=True, blank=True)
    dat_promo_end = models.DateField(null=True, blank=True)
    txt_promo_headline = models.CharField(max_length=96,null=True,blank=True)
    txt_promo_tagline = models.CharField(max_length=96,null=True,blank=True)
    txt_promo_offer_desc = models.CharField(max_length=255,null=True,blank=True)
    bin_promo_creative = models.CharField(max_length=255,null=True,blank=True)
    bin_promo_creative_small = models.CharField(max_length=255,null=True,blank=True)
    flg_customer_facing = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='Y',null=True,blank=True)
    num_promo_priority = models.SmallIntegerField(null=True,blank=True)
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True ,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,
    related_name='%(class)s_checker')
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
        db_table = 'mst_promo_codes'
        unique_together = ('cod_promo', 'cod_rec_status')
        verbose_name = 'Promo Code'
        verbose_name_plural = 'Promo Codes'

    def __str__(self):
        return f"{self.cod_promo} ({self.cod_rec_status})"