from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets, permissions
from .models import SecUserMaster,SecUserPswdHist
from .serializer import SecUserMasterSerializer,SecUserPswdHistCreateSerializer,SecUserPswdHistSerializer,SecActiveUserMasterSerializer,ChangePasswordSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from rest_framework import status, viewsets
from utils.services.responses import success_response, error_response
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.decorators import action
from utils.services.responses import error_response,success_response





class SecUserMasterViewSet(BaseModelViewSet):
    menu_id = 61
    """
    API endpoint for SecUserMaster.
    Password (txt_user_signature) is write-only and won't be visible in GET responses.
    """

    def get_serializer_class(self):
        if self.action == 'Active':
            return SecActiveUserMasterSerializer
        return SecUserMasterSerializer
    queryset = SecUserMaster.objects.select_related("id_parent_company_3rdparty")
    serializer_class = SecUserMasterSerializer

    @action(detail=False, methods=['get'], url_path='active-user')
    def active_user(self, request):
        try:
            active_users = SecUserMaster.objects.filter(cod_rec_status='A')
            serializer = SecActiveUserMasterSerializer(active_users, many=True)
            return success_response("active users retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


    #permission_classes = [permissions.IsAuthenticated]  # or customize as needed

    # Optional: filter/queryset customization
    # def get_queryset(self):
    #     return SecUserMaster.objects.filter(is_active=True)
    

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import SecUserPreferences,SecUserAccessLog
from .serializer import SecUserPreferencesSerializer,SecUserAccessLogSerializer
from rest_framework.views import APIView


class SecUserPreferencesViewSet(BaseModelViewSet):
    queryset = SecUserPreferences.objects.select_related('txt_login_id')
    serializer_class = SecUserPreferencesSerializer
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        consumes=["application/json", "multipart/form-data"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        consumes=["application/json", "multipart/form-data"],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        consumes=["application/json", "multipart/form-data"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

class SecUserAccessLogListView(BaseModelViewSet):
    queryset = SecUserAccessLog.objects.all().order_by('-dat_time_login')
    serializer_class = SecUserAccessLogSerializer

class SecUserPswdHistViewSet(BaseModelViewSet):
    queryset = SecUserPswdHist.objects.all()
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return SecUserPswdHistCreateSerializer
        return SecUserPswdHistSerializer

class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Change user password",
        request_body=ChangePasswordSerializer,
        tags=["Authentication"],
        responses={
            200: "Password changed successfully",
            400: "Validation error",
            401: "Unauthorized"
        }
    )

    def post(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.validated_data["old_password"]
            new_password = serializer.validated_data["new_password"]
            confirm_password = serializer.validated_data["confirm_password"]

            if not user.check_password(old_password):
                return error_response(
                    message="Old password is incorrect",
                    status_code=status.HTTP_400_BAD_REQUEST
                )

            if new_password != confirm_password:
                return error_response(
                    message="New passwords do not match",
                    status_code=status.HTTP_400_BAD_REQUEST
                )
            
            if old_password == new_password:
                return error_response(message="New password must be different", status_code=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()

            return success_response(
                message="Password changed successfully",
                status_code=status.HTTP_200_OK
            )

        return error_response(
            message="Invalid data",
            errors=serializer.errors,
            status_code=status.HTTP_400_BAD_REQUEST
        )
