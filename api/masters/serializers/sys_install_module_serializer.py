from rest_framework import serializers
from ..models import SysInstallModule


class SysInstallModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysInstallModule
        fields = "__all__"
