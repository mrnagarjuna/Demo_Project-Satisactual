from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from ..models import MstDisabilityCodes
from ..serializers.mst_disabilitycodes_serializer import MstDisabilityCodesSerializer,MstActiveDisabilityCodesSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status

class MstDisabilityCodesViewSet(BaseModelViewSet):
    menu_id = 28
    queryset = MstDisabilityCodes.objects.all()
    serializer_class = MstDisabilityCodesSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-disabilitycodes")
    def activeDisabilityCodes(self,request):
        try:
          queryset=MstDisabilityCodes.objects.filter(cod_rec_status='A')
          serializer=MstActiveDisabilityCodesSerializer(queryset,many=True)
          return success_response("active disabilitycodes retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstDisabilityCodesSerializer(obj, data=request.data)
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

    # lookup_field = 'cod_disability'  # placeholder for DRF

    # def get_object(self):
    #     cod_disability = self.kwargs.get('cod_disability')
    #     cod_rec_status = self.kwargs.get('cod_rec_status')

    #     return get_object_or_404(
    #         MstDisabilityCodes,
    #         cod_disability=cod_disability,
    #         cod_rec_status=cod_rec_status
    #     )
