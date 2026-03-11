from django.shortcuts import render

# Create your views here.
# api/user/views.py
from drf_yasg.utils import swagger_auto_schema
from collections import defaultdict
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from utils.services.responses import error_response, success_response
from ..roles.models import SecUserXRoles,SecUserRoleMenus


# class JWTLoginView(APIView):
#     permission_classes = [AllowAny]

#     @swagger_auto_schema(
#         operation_summary="User Login",
#         operation_description="Login using txt_login_id and password to get JWT tokens",
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             required=["txt_login_id", "password"],
#             properties={
#                 "txt_login_id": openapi.Schema(
#                     type=openapi.TYPE_STRING,
#                     description="User Login ID"
#                 ),
#                 "password": openapi.Schema(
#                     type=openapi.TYPE_STRING,
#                     format="password",
#                     description="User Password"
#                 ),
#             },
#         ),
#         responses={
#             200: openapi.Response(
#                 description="Login successful",
#                 schema=openapi.Schema(
#                     type=openapi.TYPE_OBJECT,
#                     properties={
#                         "message": openapi.Schema(type=openapi.TYPE_STRING),
#                         "data": openapi.Schema(
#                             type=openapi.TYPE_OBJECT,
#                             properties={
#                                 "login_details": openapi.Schema(
#                                     type=openapi.TYPE_OBJECT,
#                                     properties={
#                                         "is_pass_changed": openapi.Schema(type=openapi.TYPE_BOOLEAN),
#                                         "is_2fa": openapi.Schema(type=openapi.TYPE_BOOLEAN),
#                                     },
#                                 ),
#                                 "tokens": openapi.Schema(
#                                     type=openapi.TYPE_OBJECT,
#                                     properties={
#                                         "refresh_token": openapi.Schema(type=openapi.TYPE_STRING),
#                                         "access_token": openapi.Schema(type=openapi.TYPE_STRING),
#                                     },
#                                 ),
#                             },
#                         ),
#                     },
#                 ),
#             ),
#             400: openapi.Response(
#                 description="Invalid login ID or password"
#             ),
#         },
#         tags=["Authentication"],
#         security=[],  # 🔴 VERY IMPORTANT: disables Bearer token for login
#     )
   


#     def post(self, request):

#     login_id = request.data.get("txt_login_id")
#     password = request.data.get("password")

#     user = authenticate(request, username=login_id, password=password)

#     if user is None:
#         return error_response(
#             message="Invalid login ID or password",
#             status_code=status.HTTP_400_BAD_REQUEST
#         )

#     # 🔹 Step 1 — Get Active Roles
#     user_roles = SecUserXRoles.objects.filter(
#         txt_login_id=user,
#         cod_rec_status='A'
#     )

#     role_ids = list(
#         user_roles.values_list("cod_user_role_id", flat=True)
#     )

#     # 🔹 Step 2 — Get Role-Menu Permissions
#     role_menus = SecUserRoleMenus.objects.filter(
#         cod_user_role_id__in=role_ids,
#         cod_rec_status='A'
#     ).values(
#         "cod_menu_option_id",
#         "flg_get",
#         "flg_post",
#         "flg_put",
#         "flg_delete"
#     )

#     # 🔹 Step 3 — Merge Permissions (Union Logic)
#     merged_permissions = defaultdict(
#         lambda: {
#             "flg_get": "N",
#             "flg_post": "N",
#             "flg_put": "N",
#             "flg_delete": "N"
#         }
#     )

#     for rm in role_menus:
#         menu_id = rm["cod_menu_option_id"]

#         if rm["flg_get"] == "Y":
#             merged_permissions[menu_id]["flg_get"] = "Y"

#         if rm["flg_post"] == "Y":
#             merged_permissions[menu_id]["flg_post"] = "Y"

#         if rm["flg_put"] == "Y":
#             merged_permissions[menu_id]["flg_put"] = "Y"

#         if rm["flg_delete"] == "Y":
#             merged_permissions[menu_id]["flg_delete"] = "Y"

#     # 🔹 Step 4 — Convert to JWT Format
#     final_permissions = [
#         {
#             "cod_menu_option_id": menu_id,
#             **perms
#         }
#         for menu_id, perms in merged_permissions.items()
#     ]

#     # 🔹 Step 5 — Create JWT
#     refresh = RefreshToken.for_user(user)
#     refresh["role_ids"] = role_ids
#     refresh["menu_permissions"] = final_permissions

#     data = {
#         "login_details": {
#             "is_pass_changed": user.is_pass_changed,
#             "is_2fa": user.is_2fa
#         },
#         "tokens": {
#             "refresh_token": str(refresh),
#             "access_token": str(refresh.access_token)
#         }
#     }

#     return success_response(
#         message="Login Successful",
#         data=data,
#         status_code=status.HTTP_200_OK
#     )
    # def post(self, request):
    #     login_id = request.data.get("txt_login_id")
    #     password = request.data.get("password")

    #     user = authenticate(request, username=login_id, password=password)

    #     if user is None:
    #         return error_response(
    #             message="Invalid login ID or password",
    #             status_code=status.HTTP_400_BAD_REQUEST
    #         )

    #     # ✅ Get active roles
    #     user_roles = SecUserXRoles.objects.filter(
    #         txt_login_id=user,
    #         cod_rec_status='A'
    #     )
        

    #     role_ids = list(
    #         user_roles.values_list("cod_user_role_id", flat=True)
    #     )
    #     print(role_ids)

    #     # ✅ Get menus linked to those roles
    #     role_menus = SecUserRoleMenus.objects.filter(
    #         cod_user_role_id__in=role_ids,
    #         cod_rec_status='A'
    #     )

    #     menu_ids = list(
    #         role_menus.values_list("cod_menu_option_id", flat=True)
    #     )
    #     print(menu_ids)

    #     # ✅ Create JWT
    #     refresh = RefreshToken.for_user(user)
    #     refresh["role_ids"] = role_ids
    #     refresh["menu_ids"] = menu_ids
    #     print(refresh)

    #     data = {
    #         "login_details": {
    #             "is_pass_changed": user.is_pass_changed,
    #             "is_2fa": user.is_2fa
    #         },
    #         "tokens": {
    #             "refresh_token": str(refresh),
    #             "access_token": str(refresh.access_token)
    #         }
    #     }

    #     return success_response(
    #         message="Login Successful",
    #         data=data,
    #         status_code=status.HTTP_200_OK
    #     )

class JWTLoginView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="User Login",
        operation_description="Login using txt_login_id and password to get JWT tokens",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["txt_login_id", "password"],
            properties={
                "txt_login_id": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="User Login ID"
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format="password",
                    description="User Password"
                ),
            },
        ),
        responses={
            200: openapi.Response(
                description="Login successful",
            ),
            400: openapi.Response(
                description="Invalid login ID or password"
            ),
        },
        tags=["Authentication"],
        security=[],
    )

    def post(self, request):

        login_id = request.data.get("txt_login_id")
        password = request.data.get("password")

        user = authenticate(request, username=login_id, password=password)

        if user is None:
            return error_response(
                message="Invalid login ID or password",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        # 🔹 Get Active Roles
        user_roles = SecUserXRoles.objects.filter(
            txt_login_id=user,
            cod_rec_status='A'
        )

        role_ids = list(
            user_roles.values_list("cod_user_role_id", flat=True)
        )

        # 🔹 Create JWT (ONLY role_ids)
        refresh = RefreshToken.for_user(user)
        refresh["role_ids"] = role_ids

        data = {
            "login_details": {
                "is_pass_changed": user.is_pass_changed,
                "is_2fa": user.is_2fa
            },
            "tokens": {
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token)
            }
        }

        return success_response(
            message="Login Successful",
            data=data,
            status_code=status.HTTP_200_OK
        )

# class JWTLoginView(APIView):
#     permission_classes = [AllowAny]

#     @swagger_auto_schema(
#         operation_summary="User Login",
#         operation_description="Login using txt_login_id and password to get JWT tokens",
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             required=["txt_login_id", "password"],
#             properties={
#                 "txt_login_id": openapi.Schema(
#                     type=openapi.TYPE_STRING,
#                     description="User Login ID"
#                 ),
#                 "password": openapi.Schema(
#                     type=openapi.TYPE_STRING,
#                     format="password",
#                     description="User Password"
#                 ),
#             },
#         ),
#         responses={
#             200: openapi.Response(
#                 description="Login successful",
#             ),
#             400: openapi.Response(
#                 description="Invalid login ID or password"
#             ),
#         },
#         tags=["Authentication"],
#         security=[],
#     )
#     def post(self, request):

#         login_id = request.data.get("txt_login_id")
#         password = request.data.get("password")

#         user = authenticate(request, username=login_id, password=password)

#         if user is None:
#             return error_response(
#                 message="Invalid login ID or password",
#                 status_code=status.HTTP_400_BAD_REQUEST
#             )

#         # 🔹 Step 1 — Get Active Roles
#         user_roles = SecUserXRoles.objects.filter(
#             txt_login_id=user,
#             cod_rec_status='A'
#         )

#         role_ids = list(
#             user_roles.values_list("cod_user_role_id", flat=True)
#         )
#         print(role_ids)

#         # 🔹 Step 2 — Get Role-Menu Permissions
#         role_menus = SecUserRoleMenus.objects.filter(
#             cod_user_role_id__in=role_ids,
#             cod_rec_status='A'
#         ).values(
#             "cod_menu_option_id",
#             "flg_get",
#             "flg_post",
#             "flg_put",
#             "flg_delete"
#         )

#         # 🔹 Step 3 — Merge Permissions (Union Logic)
#         merged_permissions = defaultdict(
#             lambda: {
#                 "flg_get": "N",
#                 "flg_post": "N",
#                 "flg_put": "N",
#                 "flg_delete": "N"
#             }
#         )

#         for rm in role_menus:
#             menu_id = rm["cod_menu_option_id"]

#             if rm["flg_get"] == "Y":
#                 merged_permissions[menu_id]["flg_get"] = "Y"

#             if rm["flg_post"] == "Y":
#                 merged_permissions[menu_id]["flg_post"] = "Y"

#             if rm["flg_put"] == "Y":
#                 merged_permissions[menu_id]["flg_put"] = "Y"

#             if rm["flg_delete"] == "Y":
#                 merged_permissions[menu_id]["flg_delete"] = "Y"

#         # 🔹 Step 4 — Convert to JWT Format
#         final_permissions = [
#             {
#                 "cod_menu_option_id": menu_id,
#                 **perms
#             }
#             for menu_id, perms in merged_permissions.items()
#         ]

#         print(final_permissions)

#         # 🔹 Step 5 — Create JWT
#         refresh = RefreshToken.for_user(user)
#         refresh["role_ids"] = role_ids
#         refresh["menu_permissions"] = final_permissions

#         data = {
#             "login_details": {
#                 "is_pass_changed": user.is_pass_changed,
#                 "is_2fa": user.is_2fa
#             },
#             "tokens": {
#                 "refresh_token": str(refresh),
#                 "access_token": str(refresh.access_token)
#             }
#         }

#         return success_response(
#             message="Login Successful",
#             data=data,
#             status_code=status.HTTP_200_OK
#         )  

# api/user/views.py
from rest_framework.permissions import IsAuthenticated

class JWTLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
    operation_summary="User Logout",
    operation_description="Logout user by blacklisting refresh token",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["refresh"],
        properties={
            "refresh": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Refresh token to blacklist"
            ),
        },
    ),
    responses={
        200: openapi.Response(
            description="Logout successful",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "status": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                }
            ),
        ),
        400: openapi.Response(
            description="Logout failed",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "status": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                    "errors": openapi.Schema(type=openapi.TYPE_STRING),
                }
            ),
        ),
    },
    tags=["Authentication"],
    security=[{"Bearer": []}],
)

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")

            if not refresh_token:
                return error_response(
                    message="Refresh token is required",
                    status_code=status.HTTP_400_BAD_REQUEST
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            return success_response(
                message="Logout successful",
                status_code=status.HTTP_200_OK
            )

        except Exception as e:
            return error_response(
                message="Logout failed",
                errors=str(e),
                status_code=status.HTTP_400_BAD_REQUEST
            )
