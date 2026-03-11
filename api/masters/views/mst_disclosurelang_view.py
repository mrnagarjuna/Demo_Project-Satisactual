from rest_framework import viewsets
from ..models import MstDisclosureLang
from ..serializers.mst_disclosurelang_serializer import MstDisclosureLangSerializer
from rest_framework.permissions import IsAuthenticated
from utils.services.baseviewset import BaseModelViewSet

class MstDisclosureLangViewSet(BaseModelViewSet):
    menu_id = 13
    queryset = MstDisclosureLang.objects.all()
    serializer_class = MstDisclosureLangSerializer
    # permission_classes = [IsAuthenticated]

    # lookup_field = 'cod_disclosure'

    # def get_queryset(self):
    #     cod_disclosure = self.kwargs.get("cod_disclosure")
    #     cod_language = self.kwargs.get("cod_language")
    #     cod_rec_status = self.kwargs.get("cod_rec_status")

    #     qs = MstDisclosureLang.objects.all()

    #     if cod_disclosure:
    #         qs = qs.filter(cod_disclosure=cod_disclosure)
    #     if cod_language:
    #         qs = qs.filter(cod_language=cod_language)
    #     if cod_rec_status:
    #         qs = qs.filter(cod_rec_status=cod_rec_status)

    #     return qs
