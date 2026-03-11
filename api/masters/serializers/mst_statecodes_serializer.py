# serializers.py
from rest_framework import serializers
from ..models import MstStateCodes


class MstStateCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstStateCodes
        fields = "__all__"

class MstStateCodesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstStateCodes
        fields = "__all__"

    def validate(self, attrs):
        if MstStateCodes.objects.filter(
            cod_state=attrs['cod_state'],
            cod_country=attrs['cod_country'],
            cod_rec_status=attrs['cod_rec_status']
        ).exists():
            raise serializers.ValidationError(
                "State code already exists for given country and record status."
            )
        return attrs
class MstActiveStateCodesSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstStateCodes
         fields=['id','cod_state',"txt_state_name"]
         read_only_fields = ['id','cod_state','txt_state_name']