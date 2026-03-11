from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions
from .models import MstContactChannel,MstContactOutcome,CmpContactListColumns,CmpContactList,CmpContactListFiles,CmpContactsAssigned
from .serializer import MstContactChannelSerializer,MstContactOutcomeSerializer,CmpContactListColumnsSerializer,CmpContactListSerializer,CmpContactListFilesSerializer,CmpContactsAssignedSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstContactChannelViewSet(BaseModelViewSet):
    menu_id = 36
    queryset = MstContactChannel.objects.all()
    serializer_class = MstContactChannelSerializer
    # permission_classes = [IsAuthenticated]

class MstContactOutcomeViewSet(BaseModelViewSet):
    menu_id = 37
    queryset = MstContactOutcome.objects.all()
    serializer_class = MstContactOutcomeSerializer
    # permission_classes = [IsAuthenticated]

# class MstContractEventsViewSet(BaseModelViewSet):
#     queryset = MstContractEvents.objects.all()
#     serializer_class = MstContractEventsSerializer
#     permission_classes = [IsAuthenticated]


# class MstContractTypesViewSet(BaseModelViewSet):
#     queryset = MstContractTypes.objects.all()
#     serializer_class = MstContractTypesSerializer
#     permission_classes = [IsAuthenticated]
class CmpContactListColumnsViewSet(BaseModelViewSet):
    menu_id = 38
    queryset = CmpContactListColumns.objects.all()
    serializer_class = CmpContactListColumnsSerializer
    # permission_classes = [IsAuthenticated]

class CmpContactListViewSet(BaseModelViewSet):
    queryset = CmpContactList.objects.all()
    serializer_class = CmpContactListSerializer
    # permission_classes = [IsAuthenticated]

# class CmpContactListEntriesViewSet(viewsets.ModelViewSet):
#     serializer_class = CmpContactListEntriesSerializer
#     permission_classes = [IsAuthenticated]
#     queryset=CmpContactListEntries.objects.all()

class CmpContactListFilesViewSet(BaseModelViewSet):
    queryset = CmpContactListFiles.objects.all()
    serializer_class=CmpContactListFilesSerializer
    # permission_classes=[IsAuthenticated]

class CmpContactsAssignedViewSet(BaseModelViewSet):
    queryset = CmpContactsAssigned.objects.all()
    serializer_class = CmpContactsAssignedSerializer
    # permission_classes=[IsAuthenticated]