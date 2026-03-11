from rest_framework import viewsets
from ..models import SysInstallModule
from ..serializers.sys_install_module_serializer import SysInstallModuleSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet


class SysInstallModuleViewSet(BaseModelViewSet):
    queryset = SysInstallModule.objects.all()
    serializer_class = SysInstallModuleSerializer
    # permission_classes=[IsAuthenticated]
