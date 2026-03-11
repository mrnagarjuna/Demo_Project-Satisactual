from rest_framework import serializers
from .models import MstProdCodes,MstProdDisclosures,MstProdDocs,MstPromoCodes

class MstProdCodesSerializer(serializers.ModelSerializer):
     class Meta:
        model = MstProdCodes
        fields = "__all__"
        read_only_fields=["id"]

class MstActiveProdCodesSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstProdCodes
         fields=['id','cod_product',"txt_product_name"]
         read_only_fields = ['id','cod_product','txt_product_name']

class MstProdDisclosuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstProdDisclosures
        fields = '__all__'
      
class MstProdDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstProdDocs
        fields = '__all__'

class MstPromoCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MstPromoCodes
        fields = '__all__'

class MstActivePromoCodesSerializer(serializers.ModelSerializer):
    class Meta:
         model = MstPromoCodes
         fields=['id',"cod_promo",'txt_promo_code_desc']
         read_only_fields = ['id','cod_promo','txt_promo_code_desc']