from rest_framework import serializers
from ..models import MstLanguages


class MstLanguagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = MstLanguages
        fields = '__all__'

class MstActiveLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstLanguages
         fields=["id","cod_language","txt_language_name"]
         read_only_fields = ["id","cod_language",'txt_language_name']