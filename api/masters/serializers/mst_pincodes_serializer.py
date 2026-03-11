from rest_framework import serializers
from ..models import MstPinCodes

class MstPinCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstPinCodes
        fields = '__all__'

class MstActivePinCodesSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstPinCodes
         fields=['id',"cod_pin_code"]
         read_only_fields = ['id','cod_pin_code']