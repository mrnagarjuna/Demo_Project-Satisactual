from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from ..models import MstDepartments
from ..serializers.mstdepartment_serializer import MstDepartmentsSerializer,MstActiveDepartmentsSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status

class MstDepartmentsViewSet(BaseModelViewSet):
    menu_id = 20
    queryset = MstDepartments.objects.all()
    serializer_class = MstDepartmentsSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-departments")
    def activeDepartments(self,request):
        try:
          queryset=MstDepartments.objects.filter(cod_rec_status='A')
          serializer=MstActiveDepartmentsSerializer(queryset,many=True)
          return success_response("active departments retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = MstDepartmentsSerializer(obj, data=request.data)
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

    # lookup_field = 'cod_department'  # placeholder for DRF

    # def get_object(self):
    #     cod_department = self.kwargs.get('cod_department')
    #     id_third_party = self.kwargs.get('id_third_party')
    #     cod_rec_status = self.kwargs.get('cod_rec_status')

    #     return get_object_or_404(
    #         MstDepartments,
    #         cod_department=cod_department,
    #         id_third_party=id_third_party,
    #         cod_rec_status=cod_rec_status
    #     )
