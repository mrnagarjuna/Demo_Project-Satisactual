from rest_framework import serializers
from ..models import SubLicencesHist


class SubLicencesHistSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubLicencesHist
        fields = "__all__"
