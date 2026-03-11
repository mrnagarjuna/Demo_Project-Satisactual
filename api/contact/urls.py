from rest_framework import routers
from django.urls import path, include
from .views import MstContactChannelViewSet,MstContactOutcomeViewSet,CmpContactListColumnsViewSet,CmpContactListViewSet,CmpContactListFilesViewSet,CmpContactsAssignedViewSet

router = routers.DefaultRouter()
router.register(r'mst-contact-channels', MstContactChannelViewSet,basename='contactchannels')
router.register(r'mst-contact-outcomes', MstContactOutcomeViewSet,basename='mstcontactoutcome')
# router.register(r'mstcontract-events', MstContractEventsViewSet,basename='mstcontractevent')
# router.register(r'mst-contract-types', MstContractTypesViewSet,basename='mstcontracttypes')
router.register(r'cmp-contact-list-columns',CmpContactListColumnsViewSet,basename='contact-list-columns')
router.register(r'cmp-contact-lists', CmpContactListViewSet, basename='contact-list')
#router.register(r"cmp-contact-list-entries",CmpContactListEntriesViewSet,basename="cmp-contact-list-entries")
router.register(r'cmp-contact-files-list',CmpContactListFilesViewSet,basename='cmp-contact-files-list')
router.register(r'cmp-contacts-assigned',CmpContactsAssignedViewSet,basename='cmp-contacts-assigned')

urlpatterns = [
    path('', include(router.urls)),
]
