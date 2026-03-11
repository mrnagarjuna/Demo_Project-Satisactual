# from rest_framework import serializers
# from ..models import CusMaster


# class CusMasterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CusMaster
#         fields = '__all__'


# class CusMasterCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CusMaster
#         fields = '__all__'

#     def validate(self, attrs):
#         if CusMaster.objects.filter(
#             id_customer=attrs.get('id_customer'),
#             cod_rec_status=attrs.get('cod_rec_status')
#         ).exists():
#             raise serializers.ValidationError(
#                 "Customer already exists with this record status."
#             )
#         return attrs
