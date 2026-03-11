from rest_framework import serializers
from ..models import SecMenuOptions

class SecMenuOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecMenuOptions
        fields = '__all__'
class MstActiveSecMenuOptionsSerializer(serializers.ModelSerializer):
    class Meta:
         model = SecMenuOptions
         fields=['id','cod_menu_option',"txt_menu_desc"]
         read_only_fields = ['id','cod_menu_option',"txt_menu_desc"]