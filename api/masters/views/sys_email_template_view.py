from utils.services.baseviewset import BaseModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers.sys_email_template_serializer import SysEmailTemplatesSerializer,SysEmailTemplatesActiveSerializer
from ..models import SysEmailTemplates
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status

class SysEmailTemplatesViewSet(BaseModelViewSet):
    queryset = SysEmailTemplates.objects.all()
    serializer_class = SysEmailTemplatesSerializer
    # permission_classes=[IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-email-templates")
    def activeCssTheme(self,request):
        try:
          queryset=SysEmailTemplates.objects.filter(cod_rec_status='A')
          serializer=SysEmailTemplatesActiveSerializer(queryset,many=True)
          return success_response("active sys-email-templates retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

