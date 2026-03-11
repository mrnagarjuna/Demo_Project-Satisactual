from rest_framework import viewsets
from ..models import SysUserMessage
from ..serializers.sys_user_message_serializer import SysUserMessageSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet


class SysUserMessageViewSet(BaseModelViewSet):
    queryset = SysUserMessage.objects.all()
    serializer_class = SysUserMessageSerializer
    # permission_classes=[IsAuthenticated]
    


