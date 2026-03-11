from rest_framework import serializers
from ..models import SysUserMessage


class SysUserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysUserMessage
        fields = "__all__"
