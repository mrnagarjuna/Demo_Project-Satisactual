from rest_framework import serializers
from ..models import MstDisabilityCodes

class MstDisabilityCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstDisabilityCodes
        fields = '__all__'

class MstActiveDisabilityCodesSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstDisabilityCodes
         fields=['id',"cod_disability",'txt_disability_desc']
         read_only_fields = ['id',"cod_disability",'txt_disability_desc']
