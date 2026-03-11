# # app/serializers/cus_misc_docs.py
# from rest_framework import serializers
# from ..models import CusMiscDocs


# class CusMiscDocsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CusMiscDocs
#         fields = "__all__"
# class CusMiscDocsCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CusMiscDocs
#         fields = [
#             'id_customer',
#             'cod_doctyp',
#             'enu_doc_purpose',
#             'txt_docnum',
#             'txt_doc_description',
#             'id_issuer',
#             'txt_issuer_name',
#             'dat_doc_issue',
#             'dat_doc_expire',
#             'bin_doc_copy',
#             'flg_original_documents_seen',
#             'cod_doc_storage_location',
#             'txt_doc_storage_location',
#             'dat_doc_collected',
#             'txt_doc_collected_by_id',
#             'flg_originals_retained',
#             'dat_doc_released',
#             'txt_doc_released_by_id',
#         ]
