from rest_framework import viewsets
from ..models import MstAuditTypes
from ..serializers.mst_audittypes_serializer import MstAuditTypesSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstAuditTypesViewSet(BaseModelViewSet):
    menu_id = 32
    queryset = MstAuditTypes.objects.all()
    serializer_class = MstAuditTypesSerializer
    # permission_classes = [IsAuthenticated]