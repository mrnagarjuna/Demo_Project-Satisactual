from django.db import models
from utils.constants.choices import REC_STATUS_CHOICES,YES_NO_CHOICES,REPORT_FORMAT_CHOICES,AV_RECORDING_CHOICES,DISPLAY_TYPE_CHOICES,BASE_QUESTION_TYPE_CHOICES,LINK_TYPE_CHOICES
from django.utils import timezone

class MstQuestionClass(models.Model):
    cod_question_class = models.CharField(max_length=4,)
    txt_question_class_desc = models.CharField(max_length=48,null=True,blank=True)
    num_display_sequence = models.SmallIntegerField(default=1)
    flg_default_value = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES)
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
        db_table = "mst_question_classes"
        verbose_name = "Question Class"
        verbose_name_plural = "Question Classes"
        unique_together=('cod_question_class', 'cod_rec_status')

    def __str__(self):
        return f"{self.cod_question_class} - {self.txt_question_class_desc}"

class MstQuestionType(models.Model):
    cod_question_type = models.CharField(max_length=4)
    enu_base_question_type = models.CharField(max_length=1,choices=BASE_QUESTION_TYPE_CHOICES,default='N')
    txt_question_type_desc = models.CharField(max_length=48,null=True,blank=True)
    enu_display_type = models.CharField(max_length=10,choices=DISPLAY_TYPE_CHOICES,null=True,blank=True)
    num_display_order = models.SmallIntegerField(null=True,blank=True)
    cod_question_class = models.ForeignKey(MstQuestionClass,on_delete=models.CASCADE,null=True,blank=True,related_name='question_types')
    num_max_chars_response = models.SmallIntegerField(default=255)
    txt_response_format = models.CharField(max_length=255,null=True,blank=True)
    flg_rating_base_zero = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    flg_rating_one_highest = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)
    txt_high_rating_label = models.CharField(max_length=48,null=True,blank=True)
    txt_low_rating_label = models.CharField(max_length=48,null=True,blank=True)
    num_rating_levels = models.SmallIntegerField(default=5)
    enu_report_format = models.CharField(max_length=10,choices=REPORT_FORMAT_CHOICES,null=True,blank=True)
    flg_av_recording_reqd = models.CharField(max_length=1,choices=AV_RECORDING_CHOICES,default='N')
    flg_simple_question = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    bin_question_icon = models.TextField(null=True,blank=True)
    flg_default_value = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
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
        db_table = "mst_question_types"
        unique_together=('cod_question_type','enu_base_question_type','cod_rec_status')
        

    def __str__(self):
        return f"{self.cod_question_type} - {self.txt_question_type_desc}"

class CmpQuestion(models.Model):
    
    id_question = models.BigAutoField(auto_created=True,primary_key=True)
    txt_question_text = models.TextField(null=True, blank=True)
    txt_question_helptext = models.CharField(max_length=255, default='', blank=True)
    txt_telecaller_prompt = models.CharField(max_length=1024, null=True, blank=True)
    txt_addl_comments_prompt = models.CharField(max_length=255, default='', blank=True)
    cod_question_type = models.ForeignKey(MstQuestionType,null=True,blank=True,related_name='questions',on_delete=models.SET_NULL)
    cod_question_class = models.ForeignKey(MstQuestionClass,null=True,blank=True,related_name='questions',on_delete=models.SET_NULL)
    enu_display_type = models.CharField(max_length=10,choices=DISPLAY_TYPE_CHOICES,default='A')

    num_rating_levels = models.SmallIntegerField(default=5)
    flg_rating_base_zero = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')
    flg_rating_one_highest = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)

    txt_high_rating_label = models.CharField(max_length=48, null=True, blank=True)
    txt_low_rating_label = models.CharField(max_length=48, null=True, blank=True)

    num_max_chars_response = models.SmallIntegerField(default=255)
    txt_response_format = models.CharField(max_length=255, null=True, blank=True)

    num_days_earliest = models.SmallIntegerField(default=-30000)
    num_days_latest = models.SmallIntegerField(default=30000)

    num_value_min = models.FloatField(default=-100000000000)
    num_value_max = models.FloatField(default=100000000000)

    flg_include_in_verbatim = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)

    flg_question_bank = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')

    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A',db_index=True)

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
        db_table = 'cmp_questions'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

class CmpQuestionLang(models.Model):
    id_question = models.ForeignKey(CmpQuestion,on_delete=models.CASCADE,related_name='languages',null=True,blank=True,db_column='id_question')

    cod_language = models.ForeignKey('masters.MstLanguages',on_delete=models.PROTECT,db_column='cod_language',related_name='questions'
    )
    
    txt_question_text = models.TextField(null=True, blank=True)
    txt_question_helptext = models.CharField(max_length=255, default='', blank=True)
    txt_telecaller_prompt = models.CharField(max_length=1024, null=True, blank=True)
    txt_addl_comments_prompt = models.CharField(max_length=255, default='', blank=True)

    txt_high_rating_label = models.CharField(max_length=48, null=True, blank=True)
    txt_low_rating_label = models.CharField(max_length=48, null=True, blank=True)

    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    class Meta:
        db_table = 'cmp_questions_lang'
        unique_together = (
            ('id_question', 'cod_language', 'cod_rec_status'),
        )
        verbose_name = 'Question Language'
        verbose_name_plural = 'Question Languages'

class CmpQuestionnaire(models.Model):
    id_questionnaire = models.BigAutoField(primary_key=True)

    txt_questionnaire_name = models.CharField(max_length=96)
    txt_questionnaire_category = models.CharField(max_length=48, null=True, blank=True)

    txt_target_audience = models.TextField(null=True, blank=True)
    txt_research_objective = models.TextField(null=True, blank=True)

    txt_created_by_id = models.CharField(max_length=48, null=True, blank=True)
    dat_created_on = models.DateField(null=True, blank=True)

    flg_public = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)

    txt_print_format_file = models.CharField(max_length=255, null=True, blank=True)

    flg_assessment = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    num_pass_score = models.SmallIntegerField(null=True, blank=True)
    num_max_minutes_to_respond = models.SmallIntegerField(null=True, blank=True)

    flg_randomize = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_show_score_on_submit = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')

    cod_rec_status = models.CharField(max_length=1,choices=REC_STATUS_CHOICES,default='A')

    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)

    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    class Meta:
        db_table = "cmp_questionnaire"
        unique_together = ("id_questionnaire", "cod_rec_status")

        indexes = [
            models.Index(fields=["id_questionnaire"]),
            models.Index(fields=["cod_rec_status"]),
        ]

    def save(self, *args, **kwargs):
        if not self.pk:
            self.dat_created_on = timezone.now().date()
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id_questionnaire} - {self.txt_questionnaire_name}"
    
class CmpQuestionListTables(models.Model):
    id_question = models.OneToOneField('CmpQuestion',db_column='id_question',on_delete=models.CASCADE,related_name='list_table',null=True,blank=True)

    txt_schema_name = models.CharField(max_length=96, null=True, blank=True)
    txt_table_name = models.CharField(max_length=96, null=True, blank=True)
    txt_code_col_name = models.CharField(max_length=96, null=True, blank=True)
    txt_descr_col_name = models.CharField(max_length=96, null=True, blank=True)

    txt_where_clause = models.TextField(null=True, blank=True)
    txt_order_by_clause = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "cmp_question_list_tables"
        verbose_name = "Question List Table"
        verbose_name_plural = "Question List Tables"

    def __str__(self):
        return f"Question {self.id_question}"
class CmpQuestionListValues(models.Model):
    id_question = models.ForeignKey(CmpQuestion,db_column="id_question",on_delete=models.CASCADE,related_name="list_values",null=True,blank=True)
    cod_value = models.CharField(max_length=4)
    num_seq = models.SmallIntegerField(null=True, blank=True)
    txt_value = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "cmp_question_list_values"
        unique_together = ("id_question", "cod_value")
        verbose_name = "Question List Value"
        verbose_name_plural = "Question List Values"

    def __str__(self):
        return f"{self.id_question} - {self.cod_value}"
    
class CmpQuestionKeywords(models.Model):
    id_question = models.OneToOneField(CmpQuestion,db_column="id_question",on_delete=models.CASCADE,related_name="keywords",null=True,blank=True)
    txt_keywords_tag = models.CharField(max_length=255, null=True, blank=True)
    txt_question_theme = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "cmp_question_keywords"
        verbose_name = "Question Keyword"
        verbose_name_plural = "Question Keywords"

    def __str__(self):
        return f"Keywords for Question {self.id_question}"
    
class CmpQuestionOptions(models.Model):
    id_question = models.ForeignKey(CmpQuestion,on_delete=models.CASCADE,db_column='id_question',related_name='master_options',null=True,blank=True)

    cod_option = models.CharField(max_length=4)

    txt_option_text = models.CharField(max_length=255,null=True,blank=True)

    num_display_sequence = models.SmallIntegerField(null=True,blank=True)

    flg_capture_addl_text = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)

    txt_additional_text_prompt = models.CharField(max_length=255,null=True,blank=True)

    # 👉 Parent Question (skip logic)
    id_parent_question = models.ForeignKey(CmpQuestion,on_delete=models.SET_NULL,null=True,blank=True,db_column='id_parent_question',related_name='child_question_options')

    # 👉 Self-referencing parent option
    cod_parent_question_option = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True,
    db_column='cod_parent_question_option',related_name='child_options')

    class Meta:
        db_table = 'cmp_question_options'
        verbose_name = 'Question Option'
        verbose_name_plural = 'Question Options'
        unique_together = (
            ('id_question', 'cod_option'),
        )
       

    def __str__(self):
        return f"{self.id_question_id} - {self.cod_option}"
    
class CmpQuestionnaireQuestionLinks(models.Model):

    id_questionnaire = models.ForeignKey('CmpQuestionnaire',on_delete=models.CASCADE,db_column='id_questionnaire',related_name='question_links',null=True,blank=True)
    # Source question
    id_question = models.ForeignKey('CmpQuestion',on_delete=models.CASCADE,db_column='id_question',related_name='outgoing_links',null=True,blank=True)
    # Selected option of the source question
    cod_option = models.ForeignKey('CmpQuestionOptions',on_delete=models.CASCADE,db_column='cod_option',related_name='option_links',null=True,blank=True)
    # Target / linked question
    id_linked_question = models.BigAutoField(primary_key=True)

    enu_link_type = models.CharField(max_length=4,choices=LINK_TYPE_CHOICES,default='SHOW')

    class Meta:
        db_table = 'cmp_questionnaire_question_links'
        verbose_name = 'Questionnaire Question Link'
        verbose_name_plural = 'Questionnaire Question Links'

        unique_together = (
            'id_questionnaire',
            'id_question',
            'cod_option',
            'id_linked_question',
            'enu_link_type',
        )


    def __str__(self):
        return (
            f"Qnr:{self.id_questionnaire} | "
            f"Q:{self.id_question} | "
            f"Opt:{self.cod_option} → "
            f"{self.enu_link_type} Q:{self.id_linked_question}"
        )
    
class CmpQuestionnaireQuestions(models.Model):

    # 🔗 Relations
    id_questionnaire = models.ForeignKey('CmpQuestionnaire',on_delete=models.CASCADE,null=True,blank=True,
        db_column='id_questionnaire',related_name='questionnaire_questions')

    id_question = models.ForeignKey('CmpQuestion',on_delete=models.CASCADE,null=True,blank=True,           db_column='id_question',related_name='questionnaire_mappings')
    
    id_prerequisite_question = models.ForeignKey('CmpQuestion',on_delete=models.SET_NULL,null=True,blank=True,db_column='id_prerequisite_question',related_name='dependent_questions')

    # 📌 Question Layout
    num_question_sequence = models.SmallIntegerField()
    num_question_page = models.SmallIntegerField(null=True, blank=True)
    num_question_group = models.SmallIntegerField(null=True, blank=True)

    txt_question_num = models.CharField(max_length=48, null=True, blank=True)

    # 📌 Validation
    flg_mandatory = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    num_min_options_reqd = models.SmallIntegerField(null=True, blank=True)
    num_max_options_allowed = models.SmallIntegerField(null=True, blank=True)

    # 📌 Prerequisite Options
    id_prerequisite_options = models.ManyToManyField('CmpQuestionOptions',blank=True,related_name='questionnaire_prerequisites')

    # 📌 Qualification / Skip Logic
    flg_qualifying_question = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_hide_question = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='N')
    flg_qualify_if_yes = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)

    id_redirect_if_yes = models.BigIntegerField(null=True, blank=True)
    id_redirect_if_no = models.BigIntegerField(null=True, blank=True)

    # 📌 Rating Logic
    num_rating_escalation_threshold = models.SmallIntegerField(default=6)
    num_rating_addl_text_threshold = models.SmallIntegerField(default=6)

    # 📌 UI Formatting
    flg_bold = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_italic = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    flg_underline = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)

    num_font_size = models.SmallIntegerField(null=True, blank=True)
    txt_font_name = models.CharField(max_length=48, null=True, blank=True)

    # 📌 Reporting
    flg_include_in_report = models.CharField(max_length=1, choices=YES_NO_CHOICES, null=True, blank=True)
    enu_report_format = models.CharField(max_length=5, choices=REPORT_FORMAT_CHOICES, null=True, blank=True)

    txt_keyword_substitutions = models.CharField(max_length=255, null=True, blank=True)
    txt_theme = models.CharField(max_length=96, null=True, blank=True)

    # 📌 Audit
    cod_rec_status = models.CharField(max_length=1, choices=REC_STATUS_CHOICES, default='A')
    txt_last_maker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_maker')
    dat_last_maker = models.DateField(null=True, blank=True)
    txt_last_checker_id = models.ForeignKey('user.SecUserMaster',to_field='txt_login_id',on_delete=models.SET_NULL,null=True,blank=True,related_name='%(class)s_checker')
    dat_last_checker = models.DateField(null=True, blank=True)
    created_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_created')
    updated_by=models.ForeignKey('user.SecUserMaster',on_delete=models.CASCADE,null=True,blank=True,related_name='%(class)s_updated')

    class Meta:
        db_table = 'cmp_questionnaire_questions'
        unique_together = (
            'id_questionnaire',
            'id_question',
            'cod_rec_status',
        )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.dat_last_maker = timezone.now().date()
        else:
            self.dat_last_checker = timezone.now().date()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id_questionnaire} - {self.id_question}"
    
class CmpQuestionnaireQuestionGroup(models.Model):

    # 🔗 Questionnaire (FK)
    id_questionnaire = models.ForeignKey(
        'CmpQuestionnaire',
        on_delete=models.CASCADE,
        db_column='id_questionnaire',
        related_name='question_groups',
        null=True,
        blank=True
    )

    # 📌 Group number (part of composite key)
    num_question_group = models.SmallIntegerField()

    # 📌 Group details
    txt_group_header = models.TextField(null=True, blank=True)
    num_min_response_reqd = models.SmallIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'cmp_questionnaire_question_group'

        unique_together = (
            'id_questionnaire',
            'num_question_group',
        )

    def __str__(self):
        return f"QNR {self.id_questionnaire} | Group {self.num_question_group}"
    
class CmpQuestionnaireQuestionOptions(models.Model):

    id_questionnaire = models.ForeignKey('CmpQuestionnaire',on_delete=models.CASCADE,db_column='id_questionnaire',related_name='question_options',null=True,blank=True)
    id_question = models.ForeignKey('CmpQuestion',on_delete=models.CASCADE,db_column='id_question',related_name='options',null=True,blank=True)
    id_option = models.ForeignKey('CmpQuestionOptions', on_delete=models.CASCADE,db_column='cod_option',related_name='questionnaire_option_links',null=True,blank=True)
    id_skip_to_question = models.ForeignKey('CmpQuestion',on_delete=models.SET_NULL,null=True,blank=True,db_column='id_skip_to_question',related_name='skip_from_options')

    flg_escalation_reqd = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')

    flg_qualifying_response = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)

    num_answer_weight = models.FloatField(default=0)

    flg_default = models.CharField(max_length=1,choices=YES_NO_CHOICES,null=True,blank=True)

    flg_exclude_option = models.CharField(max_length=1,choices=YES_NO_CHOICES,default='N')

    class Meta:
        db_table = 'cmp_questionnaire_question_options'
        unique_together = (
            'id_questionnaire',
            'id_question',
            'id_option'
        )
        verbose_name = 'Question Option'
        verbose_name_plural = 'Question Options'

    def __str__(self):
        return f"{self.id_questionnaire}-{self.id_question}-{self.id_option}"