from rest_framework import serializers
from ..models import MstAuditTypes

class MstAuditTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstAuditTypes
        fields = "__all__"
