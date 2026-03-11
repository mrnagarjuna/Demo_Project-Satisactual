from rest_framework import viewsets
from ..models import SecMenuOptions
from ..serializers.mst_secmenu_options_serializer import SecMenuOptionsSerializer,MstActiveSecMenuOptionsSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

class SecMenuOptionsViewSet(BaseModelViewSet):
    queryset = SecMenuOptions.objects.all()
    serializer_class = SecMenuOptionsSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-menu-options")
    def activeMenuOptions(self,request):
        try:
          queryset=SecMenuOptions.objects.filter(cod_rec_status='A')
          serializer=MstActiveSecMenuOptionsSerializer(queryset,many=True)
          return success_response("active menu-options retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = SecMenuOptionsSerializer(obj, data=request.data)
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
    # @swagger_auto_schema(
    #     consumes=["application/json", "multipart/form-data"],
    # )
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # @swagger_auto_schema(
    #     consumes=["application/json", "multipart/form-data"],
    # )
    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)

    # @swagger_auto_schema(
    #     consumes=["application/json", "multipart/form-data"],
    # )
    # def partial_update(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)

