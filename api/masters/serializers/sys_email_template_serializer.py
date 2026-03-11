from rest_framework import serializers
from ...masters.models import SysEmailTemplates

class SysEmailTemplatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SysEmailTemplates
        fields = "__all__"

class SysEmailTemplatesActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model=SysEmailTemplates
        fields=['id','cod_email_template','txt_template_name']