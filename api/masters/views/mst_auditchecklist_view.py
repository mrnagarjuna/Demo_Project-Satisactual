from rest_framework import viewsets
from ..models import MstAuditChecklist
from ..serializers.mst_auditchecklist_serializer import MstAuditChecklistSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstAuditChecklistViewSet(BaseModelViewSet):
    menu_id = 31
    queryset = MstAuditChecklist.objects.all()
    serializer_class = MstAuditChecklistSerializer
    # permission_classes = [IsAuthenticated]
