# # app/views/cus_misc_docs.py
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

# from ..models import CusMiscDocs
# from ..serializers.mst_cus_miscdocs_serializer import (
#     CusMiscDocsSerializer,
#     CusMiscDocsCreateSerializer
# )


# class CusMiscDocsViewSet(ModelViewSet):
#     queryset = CusMiscDocs.objects.all()
#     permission_classes = [IsAuthenticated]

#     def get_serializer_class(self):
#         if self.request.method in ['POST', 'PUT', 'PATCH']:
#             return CusMiscDocsCreateSerializer
#         return CusMiscDocsSerializer
