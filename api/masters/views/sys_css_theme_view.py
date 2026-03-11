from rest_framework.viewsets import ModelViewSet
from ..models import SysCssTheme
from ..serializers.sys_css_theme_serializer import SysCssThemeSerializer,ActiveSysCssThemeSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status

class SysCssThemeViewSet(BaseModelViewSet):
    menu_id = 56
    queryset = SysCssTheme.objects.all()
    serializer_class = SysCssThemeSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-css-themes")
    def activeCssTheme(self,request):
        try:
          queryset=SysCssTheme.objects.filter(cod_rec_status='A')
          serializer=ActiveSysCssThemeSerializer(queryset,many=True)
          return success_response("active css-themes retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
