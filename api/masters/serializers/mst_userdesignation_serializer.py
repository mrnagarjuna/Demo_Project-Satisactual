# serializers.py
from rest_framework import serializers
from ..models import MstUserDesignation


class MstUserDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstUserDesignation
        fields = "__all__"
class MstActiveUserDesignationsSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstUserDesignation
         fields=['id','cod_designation',"txt_designation_desc"]
         read_only_fields = ['id','cod_designation',"txt_designation_desc"]