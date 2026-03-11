from rest_framework import viewsets
from ..models import MstDisclosures
from ..serializers.mst_disclosures_serializer import MstDisclosuresSerializer,MstActiveDisclosuresSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response
from rest_framework import status

class MstDisclosuresViewSet(BaseModelViewSet):
    menu_id = 12
    queryset = MstDisclosures.objects.all()
    serializer_class = MstDisclosuresSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-disclosure")
    def activeDisclosures(self,request):
        try:
          queryset=MstDisclosures.objects.filter(cod_rec_status='A')
          serializer=MstActiveDisclosuresSerializer(queryset,many=True)
          return success_response("active disclosure retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # def get_queryset(self):
    #     qs = MstDisclosures.objects.all()
    #     cod_disclosure = self.kwargs.get("cod_disclosure")
    #     cod_rec_status = self.kwargs.get("cod_rec_status")

    #     if cod_disclosure:
    #         qs = qs.filter(cod_disclosure=cod_disclosure)

    #     if cod_rec_status:
    #         qs = qs.filter(cod_rec_status=cod_rec_status)

    #     return qs
