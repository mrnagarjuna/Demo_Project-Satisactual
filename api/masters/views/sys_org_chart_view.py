from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import SysOrgChart
from ..serializers.sys_org_chart_serializer import SysOrgChartSerializer


class SysOrgChartViewSet(viewsets.ModelViewSet):
    queryset = SysOrgChart.objects.all()
    serializer_class = SysOrgChartSerializer
    