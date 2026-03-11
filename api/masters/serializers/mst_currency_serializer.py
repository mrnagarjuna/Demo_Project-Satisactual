from rest_framework import serializers
from ..models import MstCurrency

class MstCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = MstCurrency
        fields = '__all__'

class MstActiveCurrencySerializer(serializers.ModelSerializer):
    class Meta:
         model = MstCurrency
         fields=['id',"cod_currency",'txt_currency_desc']
         read_only_fields = ['id','cod_currency','txt_currency_desc']