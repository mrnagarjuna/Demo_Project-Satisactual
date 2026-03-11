from rest_framework import serializers
from ..models import MstCityClasses

class MstCityClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstCityClasses
        fields = '__all__'

class MstactiveCityClassesSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstCityClasses
         fields=['id',"cod_city_class",'txt_city_class_desc']
         read_only_fields = ['id','cod_city_class','txt_city_class_desc']
