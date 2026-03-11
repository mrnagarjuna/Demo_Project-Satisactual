from rest_framework import serializers
from ..models import MstCreditOfficerLevels

class MstCreditOfficerLevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstCreditOfficerLevels
        fields = '__all__'

class MstActiveCreditOfficerLevelsSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstCreditOfficerLevels
         fields=['id',"cod_credit_officer_level",'txt_credit_officer_level_desc']
         read_only_fields = ['id',"cod_credit_officer_level",'txt_credit_officer_level_desc']
