from rest_framework import serializers
from ..models import MstDepartmentSupportTeam

class MstDepartmentSupportTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstDepartmentSupportTeam
        fields = '__all__'
