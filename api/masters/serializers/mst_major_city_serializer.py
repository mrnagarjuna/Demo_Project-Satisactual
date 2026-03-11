
# serializers.py
from rest_framework import serializers
from ..models import MstMajorCity


class MstMajorCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MstMajorCity
        fields = "__all__"

class MstActiveMajorCitySerializer(serializers.ModelSerializer):
    class Meta:
         model = MstMajorCity
         fields=['id','cod_city',"txt_city_name"]
         read_only_fields = ['id','cod_city','txt_city_name']