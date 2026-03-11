from rest_framework import serializers
from ..models import MstDisclosureLang

class MstDisclosureLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstDisclosureLang
        fields = '__all__'
