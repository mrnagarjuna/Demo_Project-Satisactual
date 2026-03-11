from rest_framework import serializers
from ..models import SubPackageRoles


class SubPackageRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubPackageRoles
        fields = "__all__"
