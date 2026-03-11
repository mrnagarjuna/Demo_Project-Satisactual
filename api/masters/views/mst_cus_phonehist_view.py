# # app/views/cus_phone_hist.py
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

# from ..models import CusPhoneHist
# from ..serializers.mst_cus_phonehist_serializer import (
#     CusPhoneHistSerializer,
#     CusPhoneHistCreateSerializer
# )


# class CusPhoneHistViewSet(ModelViewSet):
#     queryset = CusPhoneHist.objects.all()
#     permission_classes = [IsAuthenticated]

#     def get_serializer_class(self):
#         if self.request.method in ['POST', 'PUT', 'PATCH']:
#             return CusPhoneHistCreateSerializer
#         return CusPhoneHistSerializer
