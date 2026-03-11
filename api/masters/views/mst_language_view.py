from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from ..models import MstLanguages
from ..serializers.mst_language_serializer import MstLanguagesSerializer,MstActiveLanguagesSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status



class MstLanguagesViewSet(BaseModelViewSet):
    menu_id = 7
    queryset = MstLanguages.objects.all()
    serializer_class = MstLanguagesSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-languages")
    def activeLanguages(self,request):
        try:
          queryset=MstLanguages.objects.filter(cod_rec_status='A')
          serializer=MstActiveLanguagesSerializer(queryset,many=True)
          return success_response("active languages retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstLanguagesSerializer(obj, data=request.data)
            if serializer.is_valid():
                is_active = serializer.validated_data['cod_rec_status']
                obj.cod_rec_status = is_active
                obj.save()
                if is_active=='A':
                    return success_response("actived")
                elif is_active=='C':
                    return success_response("deactivated")
                else:
                    return error_response("enter correct status, A-->Active,C-->Inactive")
            return error_response("error occured", errors=serializer.errors)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
