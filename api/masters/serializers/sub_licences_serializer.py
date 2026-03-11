from rest_framework import serializers
from ..models import SubLicence


class SubLicenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubLicence
        fields = "__all__"
