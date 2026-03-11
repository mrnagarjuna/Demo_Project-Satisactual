from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import MstAddrTypes
from ..serializers.mstaddrtypes_serializer import MstAddrTypesSerializer,MstActiveAddrTypesSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status


class MstAddrTypesViewSet(BaseModelViewSet):
    menu_id=27
    queryset = MstAddrTypes.objects.all()
    serializer_class = MstAddrTypesSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-addrs")
    def activeAddr(self,request):
        try:
          queryset=MstAddrTypes.objects.filter(cod_rec_status='A')
          serializer=MstActiveAddrTypesSerializer(queryset,many=True)
          return success_response("active addr retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstAddrTypesSerializer(obj, data=request.data)
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
        

    # Disable standard pk lookup since we have composite keys
    # lookup_field = 'cod_addr_type'
    # lookup_url_kwarg = 'cod_addr_type'
    # lookup_value_regex = '[^/]+'

    # def get_object(self):
    #     cod_addr_type = self.kwargs.get('cod_addr_type')
    #     # cod_rec_status = self.kwargs.get('cod_rec_status')

    #     return get_object_or_404(
    #         MstAddrTypes,
    #         cod_addr_type=cod_addr_type,
    #         # cod_rec_status=cod_rec_status
    #     )
    

