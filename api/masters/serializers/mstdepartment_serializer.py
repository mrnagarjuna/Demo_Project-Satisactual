from rest_framework import serializers
from ..models import MstDepartments

class MstDepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstDepartments
        fields = '__all__'

class MstActiveDepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstDepartments
         fields=["id","cod_department","txt_department_name"]
         read_only_fields = ["id","cod_department",'txt_department_name']
