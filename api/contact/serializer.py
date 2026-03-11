from rest_framework import serializers
from .models import MstContactChannel,MstContactOutcome,CmpContactListColumns,CmpContactList,CmpContactListFiles,CmpContactsAssigned

class MstContactChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstContactChannel
        fields = "__all__"

class MstContactOutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstContactOutcome
        fields = "__all__"

# class MstContractEventsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MstContractEvents
#         fields = "__all__"

# class MstContractTypesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MstContractTypes
#         fields = "__all__"
class CmpContactListColumnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmpContactListColumns
        fields = "__all__"

class CmpContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmpContactList
        fields = "__all__"
# class CmpContactListEntriesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CmpContactListEntries
#         fields = "__all__"

class CmpContactListFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CmpContactListFiles
        fields = "__all__"

class CmpContactsAssignedSerializer(serializers.ModelSerializer):

    class Meta:
        model = CmpContactsAssigned
        fields = "__all__"