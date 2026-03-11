from rest_framework import serializers
from ..models import MstDistrictCodes

class MstDistrictCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstDistrictCodes
        fields = "__all__"

class MstActiveDistrictCodesSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstDistrictCodes
         fields=['id','cod_district',"txt_district_name"]
         read_only_fields = ['id','cod_district','txt_district_name']
         