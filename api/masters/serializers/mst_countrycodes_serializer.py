from rest_framework import serializers
from ..models import MstCountryCodes

class MstCountryCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstCountryCodes
        fields = '__all__'

class MstActiveCountryCodesSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstCountryCodes
         fields=['id','cod_country',"txt_country_name"]
         read_only_fields = ['id','cod_country','txt_country_name']