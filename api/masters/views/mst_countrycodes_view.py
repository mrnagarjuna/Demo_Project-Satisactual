from rest_framework import viewsets
from ..models import MstCountryCodes
from ..serializers.mst_countrycodes_serializer import MstCountryCodesSerializer,MstActiveCountryCodesSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status

class MstCountryCodesViewSet(BaseModelViewSet):
    menu_id = 9
    queryset = MstCountryCodes.objects.all()
    serializer_class = MstCountryCodesSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-countries")
    def activeCountries(self,request):
        try:
          queryset=MstCountryCodes.objects.filter(cod_rec_status='A')
          serializer=MstActiveCountryCodesSerializer(queryset,many=True)
          return success_response("active countries retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstCountryCodesSerializer(obj, data=request.data)
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
