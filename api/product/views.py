from django.shortcuts import render
from utils.services.baseviewset import BaseModelViewSet
from .models import MstProdCodes,MstProdDisclosures,MstProdDocs,MstPromoCodes
from .serializers import MstProdCodesSerializer,MstProdDisclosuresSerializer,MstProdDocsSerializer,MstPromoCodesSerializer,MstActiveProdCodesSerializer,MstActivePromoCodesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status

class MstProdCodesViewset(BaseModelViewSet):
    menu_id = 22
    queryset=MstProdCodes.objects.all()
    serializer_class=MstProdCodesSerializer
    # permission_classes=[IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-prodcodes")
    def activeProdCodes(self,request):
        try:
          queryset=MstProdCodes.objects.filter(cod_rec_status='A')
          serializer=MstActiveProdCodesSerializer(queryset,many=True)
          return success_response("active prodcodes retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstProdCodesSerializer(obj, data=request.data)
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


class MstProdDisclosuresViewSet(BaseModelViewSet):
    menu_id = 23
    queryset = MstProdDisclosures.objects.all()
    serializer_class = MstProdDisclosuresSerializer
    # permission_classes = [IsAuthenticated]

class MstProdDocsViewSet(BaseModelViewSet):
    menu_id = 24
    
    queryset = MstProdDocs.objects.all()
    serializer_class = MstProdDocsSerializer
    # permission_classes = [IsAuthenticated]

class MstPromoCodesViewSet(BaseModelViewSet):
    menu_id = 21
    queryset = MstPromoCodes.objects.all()
    serializer_class = MstPromoCodesSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-promocodes")
    def activePromoCodes(self,request):
        try:
          queryset=MstPromoCodes.objects.filter(cod_rec_status='A')
          serializer=MstActivePromoCodesSerializer(queryset,many=True)
          return success_response("active promocodes retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstPromoCodesSerializer(obj, data=request.data)
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