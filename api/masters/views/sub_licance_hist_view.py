from rest_framework import viewsets
from ..models import SubLicencesHist
from ..serializers.sub_licence_hist_serializer import SubLicencesHistSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet


class SubLicencesHistViewSet(BaseModelViewSet):
    queryset = SubLicencesHist.objects.all()
    serializer_class = SubLicencesHistSerializer
    # permission_classes=[IsAuthenticated]
