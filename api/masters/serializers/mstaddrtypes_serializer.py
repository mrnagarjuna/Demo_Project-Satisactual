from rest_framework import serializers
from ..models import MstAddrTypes

class MstAddrTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstAddrTypes
        fields = '__all__'
class MstActiveAddrTypesSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstAddrTypes
         fields=['id',"cod_addr_type",'txt_addr_type_desc']
         read_only_fields = ['id',"cod_addr_type",'txt_addr_type_desc']