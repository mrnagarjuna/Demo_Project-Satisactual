from utils.services.baseviewset import BaseModelViewSet
from ..models import MstPinCodes
from ..serializers.mst_pincodes_serializer import  MstPinCodesSerializer,MstActivePinCodesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status

class MstPinCodesViewSet(BaseModelViewSet):
    menu_id = 29
    queryset = MstPinCodes.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class=MstPinCodesSerializer
    
    @action(detail=False,methods=["get"],url_path="active-pincodes")
    def activePinCodes(self,request):
        try:
          queryset=MstPinCodes.objects.filter(cod_rec_status='A')
          serializer=MstActivePinCodesSerializer(queryset,many=True)
          return success_response("active pincodes retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstPinCodesSerializer(obj, data=request.data)
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