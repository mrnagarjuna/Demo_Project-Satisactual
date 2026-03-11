from rest_framework import viewsets
from ..models import SubPackageRoles
from ..serializers.sub_package_roles_serializer import SubPackageRolesSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet


class SubPackageRolesViewSet(BaseModelViewSet):
    queryset = SubPackageRoles.objects.all()
    serializer_class = SubPackageRolesSerializer
    # permission_classes=[IsAuthenticated]
