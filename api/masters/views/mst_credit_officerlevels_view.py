from rest_framework import viewsets
from ..models import MstCreditOfficerLevels
from ..serializers.mst_credit_officerlevels_serializer import MstCreditOfficerLevelsSerializer,MstActiveCreditOfficerLevelsSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status

class MstCreditOfficerLevelsViewSet(BaseModelViewSet):
    menu_id = 34
    queryset = MstCreditOfficerLevels.objects.all()
    serializer_class = MstCreditOfficerLevelsSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-Credit-Officer-Levels")
    def activeCreditOfficerLevels(self,request):
        try:
          queryset=MstCreditOfficerLevels.objects.filter(cod_rec_status='A')
          serializer=MstActiveCreditOfficerLevelsSerializer(queryset,many=True)
          return success_response("active credit-officer-levels retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
