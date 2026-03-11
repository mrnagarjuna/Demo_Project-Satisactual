from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import MstQuestionClass,MstQuestionType,CmpQuestion,CmpQuestionLang,CmpQuestionnaire, CmpQuestionListTables,CmpQuestionListValues,CmpQuestionKeywords,CmpQuestionOptions,CmpQuestionnaireQuestionLinks,CmpQuestionnaireQuestions,CmpQuestionnaireQuestionGroup,CmpQuestionnaireQuestionOptions
from .serializers import MstQuestionClassSerializer,MstQuestionTypeSerializer,CmpQuestionSerializer,CmpQuestionLangSerializer,CmpQuestionnaireSerializer, CmpQuestionListTablesSerializer,CmpQuestionListValuesSerializer,CmpQuestionKeywordsSerializer,CmpQuestionOptionsSerializer,CmpQuestionnaireQuestionLinksSerializer,CmpQuestionnaireQuestionsSerializer,CmpQuestionnaireQuestionGroupSerializer,CmpQuestionnaireQuestionOptionSerializer,MstActiveQuestionClassSerializer,MstActiveQuestionnaireSerializer,MstActiveQuestionSerializer,MstActiveQuestionTypeSerializer
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status



class MstQuestionClassViewSet(BaseModelViewSet):
    menu_id = 16
    queryset = MstQuestionClass.objects.all()
    serializer_class = MstQuestionClassSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-questionclasses")
    def activeQuestionClass(self,request):
        try:
          queryset=MstQuestionClass.objects.filter(cod_rec_status='A')
          serializer=MstActiveQuestionClassSerializer(queryset,many=True)
          return success_response("active questionclasses retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstQuestionClassSerializer(obj, data=request.data)
            if serializer.is_valid():
                is_active = serializer.validated_data['cod_rec_status']
                obj.cod_rec_status = is_active
                obj.save()
                if is_active=='A':
                    return success_response("actived")
                elif is_active=='C':
                    return success_response("deactivated")
                else:
                    return error_response("enter correct status, A-->Active,C-->Inactive")
            return error_response("error occured", errors=serializer.errors)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MstQuestionTypeViewSet(BaseModelViewSet):
    menu_id = 17
    queryset = MstQuestionType.objects.all()
    serializer_class = MstQuestionTypeSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-questiontypes")
    def activeQuestionType(self,request):
        try:
          queryset=MstQuestionType.objects.filter(cod_rec_status='A')
          serializer=MstActiveQuestionTypeSerializer(queryset,many=True)
          return success_response("active questiontypes retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstQuestionTypeSerializer(obj, data=request.data)
            if serializer.is_valid():
                is_active = serializer.validated_data['cod_rec_status']
                obj.cod_rec_status = is_active
                obj.save()
                if is_active=='A':
                    return success_response("actived")
                elif is_active=='C':
                    return success_response("deactivated")
                else:
                    return error_response("enter correct status, A-->Active,C-->Inactive")
            return error_response("error occured", errors=serializer.errors)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CmpQuestionViewSet(BaseModelViewSet):
    menu_id = 39
    queryset=CmpQuestion.objects.all()
    serializer_class=CmpQuestionSerializer
    # permission_classes=[IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-questions")
    def activeQuestion(self,request):
        try:
          queryset=CmpQuestion.objects.filter(cod_rec_status='A')
          serializer=MstActiveQuestionSerializer(queryset,many=True)
          return success_response("active question retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = CmpQuestionSerializer(obj, data=request.data)
            if serializer.is_valid():
                is_active = serializer.validated_data['cod_rec_status']
                obj.cod_rec_status = is_active
                obj.save()
                if is_active=='A':
                    return success_response("actived")
                elif is_active=='C':
                    return success_response("deactivated")
                else:
                    return error_response("enter correct status, A-->Active,C-->Inactive")
            return error_response("error occured", errors=serializer.errors)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CmpQuestionLangViewSet(BaseModelViewSet):
    menu_id = 40
    queryset=CmpQuestionLang.objects.all()
    serializer_class=CmpQuestionLangSerializer
    # permission_classes=[IsAuthenticated]

class CmpQuestionnaireViewSet(BaseModelViewSet):
    menu_id = 46
    serializer_class = CmpQuestionnaireSerializer
    # permission_classes = [IsAuthenticated]
    queryset=CmpQuestionnaire.objects.all()

    @action(detail=False,methods=["get"],url_path="active-questionnaire")
    def activeQuestionnaire(self,request):
        try:
          queryset=CmpQuestionnaire.objects.filter(cod_rec_status='A')
          serializer=MstActiveQuestionnaireSerializer(queryset,many=True)
          return success_response("active questionnaire retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = CmpQuestionnaireSerializer(obj, data=request.data)
            if serializer.is_valid():
                is_active = serializer.validated_data['cod_rec_status']
                obj.cod_rec_status = is_active
                obj.save()
                if is_active=='A':
                    return success_response("actived")
                elif is_active=='C':
                    return success_response("deactivated")
                else:
                    return error_response("enter correct status, A-->Active,C-->Inactive")
            return error_response("error occured", errors=serializer.errors)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CmpQuestionListTablesViewSet(BaseModelViewSet):
    menu_id = 52
    queryset = CmpQuestionListTables.objects.select_related('id_question')
    serializer_class = CmpQuestionListTablesSerializer
    # permission_classes = [IsAuthenticated]

class CmpQuestionListValuesViewSet(BaseModelViewSet):
    menu_id = 48
    serializer_class = CmpQuestionListValuesSerializer
    # permission_classes = [IsAuthenticated]
    queryset= CmpQuestionListValues.objects.all()

class CmpQuestionKeywordsViewSet(BaseModelViewSet):
    menu_id = 49
    serializer_class = CmpQuestionKeywordsSerializer
    # permission_classes = [IsAuthenticated]
    queryset= queryset = CmpQuestionKeywords.objects.select_related("id_question")

class CmpQuestionOptionsViewSet(BaseModelViewSet):
    menu_id = 50
    queryset = CmpQuestionOptions.objects.select_related(
        'id_question',
        'id_parent_question',
        'cod_parent_question_option'
    ).all()

    serializer_class = CmpQuestionOptionsSerializer
    # permission_classes = [IsAuthenticated]

class CmpQuestionnaireQuestionLinksViewSet(BaseModelViewSet):
    menu_id = 51

    queryset = CmpQuestionnaireQuestionLinks.objects.select_related(
        'id_questionnaire',
        'id_question',
        'cod_option'
    ).all()

    serializer_class = CmpQuestionnaireQuestionLinksSerializer
    # permission_classes = [IsAuthenticated]

from rest_framework.viewsets import ModelViewSet

class CmpQuestionnaireQuestionsViewSet(BaseModelViewSet):
    menu_id = 54

    queryset = CmpQuestionnaireQuestions.objects.select_related(
        'id_questionnaire',
        'id_question',
        'id_prerequisite_question'
    ).prefetch_related(
        'id_prerequisite_options'
    )

    serializer_class = CmpQuestionnaireQuestionsSerializer
    # permission_classes = [IsAuthenticated]

class CmpQuestionnaireQuestionGroupViewSet(BaseModelViewSet):
    menu_id = 57
    serializer_class = CmpQuestionnaireQuestionGroupSerializer

    queryset = (
        CmpQuestionnaireQuestionGroup.objects
        .select_related('id_questionnaire')
    )
    # permission_classes = [IsAuthenticated]

class CmpQuestionnaireQuestionOptionViewSet(BaseModelViewSet):
    menu_id = 55
    serializer_class=CmpQuestionnaireQuestionOptionSerializer
    queryset=CmpQuestionnaireQuestionOptions.objects.all()
    # permission_classes = [IsAuthenticated]
