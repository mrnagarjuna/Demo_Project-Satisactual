# from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated
# from ..models import CusMaster
# from utils.services.baseviewset import BaseModelViewSet
# from ..serializers.mst_customer_serializer import (
#     CusMasterSerializer,
#     CusMasterCreateSerializer
# )


# class CusMasterViewSet(BaseModelViewSet):
#     queryset = CusMaster.objects.all()
#     permission_classes = [IsAuthenticated]
#     serializer_class = CusMasterSerializer  # default

#     def get_serializer_class(self):
#         if self.request.method in ['POST', 'PUT', 'PATCH']:
#             return CusMasterCreateSerializer
#         return self.serializer_class
