from rest_framework import viewsets
from ..models import SubLicence
from ..serializers.sub_licences_serializer import SubLicenceSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet


class SubLicenceViewSet(BaseModelViewSet):
    queryset = SubLicence.objects.all()
    serializer_class = SubLicenceSerializer
    # permission_classes = [IsAuthenticated]
