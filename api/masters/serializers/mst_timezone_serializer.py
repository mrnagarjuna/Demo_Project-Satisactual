from rest_framework import serializers
from ..models import MstTimeZone


class MstTimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstTimeZone
        fields = "__all__"

class MstActiveTimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstTimeZone
         fields=['id','cod_time_zone',"txt_time_zone_name"]
         read_only_fields = ['id','cod_time_zone','txt_time_zone_name']