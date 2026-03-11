from rest_framework import serializers
from .models import MstQuestionClass,MstQuestionType,CmpQuestion,CmpQuestionLang,CmpQuestionnaire,CmpQuestionListTables,CmpQuestionListValues,CmpQuestionKeywords,CmpQuestionOptions,CmpQuestionnaireQuestionLinks,CmpQuestionnaireQuestions,CmpQuestionnaireQuestionGroup,CmpQuestionnaireQuestionOptions


class MstQuestionClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstQuestionClass
        fields = "__all__"

class MstActiveQuestionClassSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstQuestionClass
         fields=['id',"cod_question_class",'txt_question_class_desc']
         read_only_fields = ['id','cod_question_class','txt_question_class_desc']

class MstQuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstQuestionType
        fields = "__all__"

class MstActiveQuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstQuestionType
         fields=['id',"cod_question_type",'txt_question_type_desc']
         read_only_fields = ['id','cod_question_type','txt_question_type_desc']

class CmpQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=CmpQuestion
        fields="__all__"

class MstActiveQuestionSerializer(serializers.ModelSerializer):
    class Meta:
         model = CmpQuestion
         fields=['id_question','txt_question_text',"txt_question_helptext"]
         read_only_fields = ['id_question','txt_question_text','txt_question_helptext']

class CmpQuestionLangSerializer(serializers.ModelSerializer):
    class Meta:
        model=CmpQuestionLang
        fields="__all__"

class CmpQuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmpQuestionnaire
        fields = "__all__"

class MstActiveQuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
         model = CmpQuestionnaire
         fields=['id_questionnaire',"txt_questionnaire_name",'txt_questionnaire_category']
         read_only_fields = ['id_questionnaire','txt_questionnaire_name','txt_questionnaire_category']

class CmpQuestionListTablesSerializer(serializers.ModelSerializer):
    class Meta:
        model=CmpQuestionListTables
        fields = "__all__"

class CmpQuestionListValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmpQuestionListValues
        fields = "__all__"
    
class CmpQuestionKeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmpQuestionKeywords
        fields = "__all__"

class CmpQuestionOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmpQuestionOptions
        fields = "__all__"

class CmpQuestionnaireQuestionLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmpQuestionnaireQuestionLinks
        fields = "__all__"
# class CmpQuestionOptionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CmpQuestionOptions
#         fields = "__all__"
class CmpQuestionnaireQuestionsSerializer(serializers.ModelSerializer):

    # prerequisite_options = serializers.PrimaryKeyRelatedField(
    #     queryset=CmpQuestionOptions.objects.all(),
    #     many=True,
    #     required=False
    # )

    # prerequisite_options_details = CmpQuestionOptionsSerializer(
    #     source='prerequisite_options',
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = CmpQuestionnaireQuestions
        fields = '__all__'

    def validate(self, attrs):
        prerequisite_question = attrs.get('id_prerequisite_question')
        prerequisite_options = attrs.get('prerequisite_options', [])

        if prerequisite_options and not prerequisite_question:
            raise serializers.ValidationError(
                "id_prerequisite_question is required when prerequisite_options are provided."
            )

        for option in prerequisite_options:
            if option.id_question_id != prerequisite_question.id_question:
                raise serializers.ValidationError(
                    f"Option {option.cod_option} does not belong to prerequisite question."
                )

        return attrs

class CmpQuestionnaireQuestionGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = CmpQuestionnaireQuestionGroup
        fields = '__all__'

class CmpQuestionnaireQuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmpQuestionnaireQuestionOptions
        fields = '__all__'

