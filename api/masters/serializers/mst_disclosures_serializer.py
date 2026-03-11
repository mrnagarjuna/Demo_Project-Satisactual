from rest_framework import serializers
from ..models import MstDisclosures

class MstDisclosuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstDisclosures
        fields = '__all__'
class MstActiveDisclosuresSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstDisclosures
         fields=['id','cod_disclosure',"txt_disclosure_desc"]
         read_only_fields = ['id','cod_disclosure',"txt_disclosure_desc"]