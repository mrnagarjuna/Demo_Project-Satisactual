from rest_framework import serializers
from ..models import MstAuditChecklist

class MstAuditChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstAuditChecklist
        fields = "__all__"
