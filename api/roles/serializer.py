from rest_framework import serializers
from .models import SecUserRoles,SecUserXRoles,SecUserRoleMenus,SecUserRoleDisclosures


class SecUserRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecUserRoles
        fields = "__all__"

class SecUserActiveRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model=SecUserRoles
        fields=['id','cod_user_role','txt_user_role_desc']
        read_only_fields = ['id','cod_user_role','txt_user_role_desc']

class SecUserXRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecUserXRoles
        fields = "__all__"

class SecUserRoleMenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecUserRoleMenus
        fields = "__all__"

class SecUserRoleDisclosuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecUserRoleDisclosures
        fields = "__all__"