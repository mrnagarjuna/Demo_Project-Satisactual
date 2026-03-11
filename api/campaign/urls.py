from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MstCampaignTypesViewSet,MstCampaignTeamRoleViewSet,MstThirdPartyTypesViewSet,MstThirdPartiesViewSet,CmpCampaignsViewSet,CmpCampaignUserGeoCoverageViewSet,CmpWavesViewSet,QAReviewProcedureListView,CmpTeamViewSet,SysPersonalizationTagsViewSet,CmpCampaignScriptsViewSet,CmpCampaignGeoCoverageViewSet,CmpSegmentViewSet,CmpSegmentSizeViewSet,CmpCampaignXChannelsViewSet,CmpCallerCredentialsViewSet,CmpEmailViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

router = DefaultRouter()

router.register(r'mst-campaign-types', MstCampaignTypesViewSet, basename='mstcampaigntypes')
router.register(r'mst-campaign-teamrole',MstCampaignTeamRoleViewSet,basename='mstcampaignteamrole')
router.register(r'mst-third-party-types',MstThirdPartyTypesViewSet,basename='mst-third-party-types')
router.register(r'mst-third-party',MstThirdPartiesViewSet,basename='mst-third-party')
router.register(r'mst-campaign',CmpCampaignsViewSet,basename='mst-campaign')
router.register(r'Cmp-Campaign-User-GeoCoverage',CmpCampaignUserGeoCoverageViewSet,basename='Cmp-Campaign-User-GeoCoverage')
router.register(r'cmp-waves',CmpWavesViewSet,basename='cmp-waves')
router.register(r'cmp-team',CmpTeamViewSet,basename='cmp-team')
router.register(r'sys-personalization-tags',SysPersonalizationTagsViewSet,basename='sys-personalization-tags')
router.register(r'cmp-campaign-scripts',CmpCampaignScriptsViewSet,basename='cmp-campaign-scripts')
router.register(r'cmp-campaign-geo-coverage',CmpCampaignGeoCoverageViewSet,basename='cmp-campaign-geo-coverage')
router.register(r'cmp-segment',CmpSegmentViewSet,basename='cmp-segment')
router.register(r'cmp-segment-size',CmpSegmentSizeViewSet,basename='cmp-segment-size')
router.register(r'cmp-campaign-x-channel',CmpCampaignXChannelsViewSet,basename='cmp-campaign-x-channel')
router.register(r'cmp-caller-credentials',CmpCallerCredentialsViewSet,basename='cmp-caller-credentials')
router.register(r"cmp-email", CmpEmailViewSet, basename="cmp-email")


urlpatterns = [
    path('', include(router.urls)),
    path("qa-review-procedures/",QAReviewProcedureListView.as_view(),name="qa-review-procedure-list"),
]
