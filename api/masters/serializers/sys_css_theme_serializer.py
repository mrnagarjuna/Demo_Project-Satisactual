from rest_framework import serializers
from ..models import SysCssTheme

class SysCssThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysCssTheme
        fields = '__all__'

class ActiveSysCssThemeSerializer(serializers.ModelSerializer):
    class Meta:
         model = SysCssTheme
         fields=['id','cod_theme',"txt_theme_name"]
         read_only_fields = ['id','cod_theme',"txt_theme_name"]
