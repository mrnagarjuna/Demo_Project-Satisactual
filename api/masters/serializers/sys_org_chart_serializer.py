from rest_framework.serializers import ModelSerializer
from ..models import SysOrgChart

class SysOrgChartSerializer(ModelSerializer):

    class Meta:
        model = SysOrgChart
        fields = "__all__"