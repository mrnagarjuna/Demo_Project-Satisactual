from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import MstDepartmentSupportTeam
from ..serializers.mstdepartmentsupportteam_serializer import MstDepartmentSupportTeamSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstDepartmentSupportTeamViewSet(BaseModelViewSet):
    menu_id = 53
    queryset = MstDepartmentSupportTeam.objects.all()
    serializer_class = MstDepartmentSupportTeamSerializer
    # permission_classes = [IsAuthenticated]

    # lookup_field = 'txt_login_id'  # primary key placeholder

    # def get_object(self):
    #     cod_department = self.kwargs.get('cod_department')
    #     txt_login_id = self.kwargs.get('txt_login_id')
    #     cod_rec_status = self.kwargs.get('cod_rec_status')
    #     id_third_party = self.kwargs.get('id_third_party')

    #     return get_object_or_404(
    #         MstDepartmentSupportTeam,
    #         cod_department=cod_department,
    #         txt_login_id=txt_login_id,
    #         cod_rec_status=cod_rec_status,
    #         id_third_party=id_third_party
    #     )