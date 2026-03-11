from rest_framework import viewsets
from ..models import MstCityClasses
from ..serializers.mst_cityclasses_serializer import MstCityClassesSerializer,MstactiveCityClassesSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status
from ...auth.permissions import RoleBasedMenuPermission

class MstCityClassesViewSet(BaseModelViewSet):
    menu_id = 26
    queryset = MstCityClasses.objects.all()
    serializer_class = MstCityClassesSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-cities",permission_classes=[RoleBasedMenuPermission])
    def activeCities(self,request):
        try:
          queryset=MstCityClasses.objects.filter(cod_rec_status='A')
          serializer=MstactiveCityClassesSerializer(queryset,many=True)
          return success_response("active cities retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    @action(detail=True,methods=["patch"],url_path="status",permission_classes=[RoleBasedMenuPermission])
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstCityClassesSerializer(obj, data=request.data)
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

