from rest_framework.routers import DefaultRouter
from .views import MstQuestionClassViewSet,MstQuestionTypeViewSet,CmpQuestionViewSet,CmpQuestionLangViewSet,CmpQuestionnaireViewSet,CmpQuestionListTablesViewSet,CmpQuestionListValuesViewSet,CmpQuestionKeywordsViewSet,CmpQuestionOptionsViewSet,CmpQuestionnaireQuestionLinksViewSet,CmpQuestionnaireQuestionsViewSet,CmpQuestionnaireQuestionGroupViewSet,CmpQuestionnaireQuestionOptionViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'cmp-question-classes',MstQuestionClassViewSet,basename='mst-question-classes')
router.register(r'cmp-question-types',MstQuestionTypeViewSet,basename='mstquestiontypes')
router.register(r'cmp-questions',CmpQuestionViewSet,basename='cmp-question')
router.register(r'cmp-question-lang',CmpQuestionLangViewSet,basename='cmp-question-lang')
router.register(r'cmp-questionnaires',CmpQuestionnaireViewSet,basename='cmp-questionnaire')
router.register(r'cmp-question-list-table',CmpQuestionListTablesViewSet,basename='cmp-question-list-table')
router.register(r'cmp-question-list-values',CmpQuestionListValuesViewSet,basename='cmp-question-list-values')
router.register(r'cmp-question-keywords',CmpQuestionKeywordsViewSet,basename='cmp-question-keywords')
router.register(r'cmp-question-options',CmpQuestionOptionsViewSet,basename='cmp-question-options')
router.register(r'cmp-questionnaire-question-links',CmpQuestionnaireQuestionLinksViewSet,basename='cmp-questionnaire-question-links')
router.register(r'cmp-questionnarie-question',CmpQuestionnaireQuestionsViewSet,basename='cmp-questionnarie-question')
router.register(r'cmp-questionnaire-question-group',CmpQuestionnaireQuestionGroupViewSet,basename='cmp-questionnaire-question-group')
router.register(r'cmp-questionnaire-question-option',CmpQuestionnaireQuestionOptionViewSet,basename='cmp-questionnaire-question-option')


urlpatterns = [
    path('', include(router.urls)),
]
