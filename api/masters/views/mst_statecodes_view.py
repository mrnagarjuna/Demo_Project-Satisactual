from rest_framework import serializers
from ..models import MstStateCodes
from ..serializers.mst_statecodes_serializer import MstStateCodesSerializer,MstStateCodesCreateSerializer,MstActiveStateCodesSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status


class MstStateCodesViewSet(BaseModelViewSet):
    menu_id = 10
    queryset = MstStateCodes.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class=MstStateCodesSerializer
    
    
    @action(detail=False,methods=["get"],url_path="active-states")
    def activeStateCodes(self,request):
        try:
          queryset=MstStateCodes.objects.filter(cod_rec_status='A')
          serializer=MstActiveStateCodesSerializer(queryset,many=True)
          return success_response("active statecodes retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstStateCodesCreateSerializer(obj, data=request.data)
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

