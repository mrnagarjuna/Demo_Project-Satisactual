from rest_framework import viewsets
from ..models import MstDistrictCodes
from ..serializers.mst_districtcode_serializer import MstDistrictCodesSerializer,MstActiveDistrictCodesSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status

class MstDistrictCodesViewSet(BaseModelViewSet):
    menu_id = 11
    queryset = MstDistrictCodes.objects.all()
    serializer_class = MstDistrictCodesSerializer
    # permission_classes = [IsAuthenticated]
    # lookup_field = 'cod_district'
    @action(detail=False,methods=["get"],url_path="active-districts")
    def activeDistricts(self,request):
        try:
          queryset=MstDistrictCodes.objects.filter(cod_rec_status='A')
          serializer=MstActiveDistrictCodesSerializer(queryset,many=True)
          return success_response("active districts retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstDistrictCodesSerializer(obj, data=request.data)
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

