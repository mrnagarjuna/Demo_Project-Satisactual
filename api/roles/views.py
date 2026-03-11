from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SecUserRoles,SecUserXRoles,SecUserRoleMenus,SecUserRoleDisclosures
from .serializer import SecUserRolesSerializer,SecUserXRolesSerializer,SecUserRoleMenusSerializer,SecUserRoleDisclosuresSerializer,SecUserActiveRolesSerializer
from utils.services.baseviewset import BaseModelViewSet
from rest_framework.decorators import action
from utils.services.responses import success_response,error_response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db import transaction


class SecUserRolesViewSet(BaseModelViewSet):
    menu_id = 60
    queryset = SecUserRoles.objects.all()
    serializer_class = SecUserRolesSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=False,methods=["get"],url_path="active-roles")
    def activeRoles(self,request):
        try:
          queryset=SecUserRoles.objects.filter(cod_rec_status='A')
          serializer=SecUserActiveRolesSerializer(queryset,many=True)
          return success_response("active roles retrieved successfully", data=serializer.data)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=True,methods=["patch"],url_path="status")
    def toggle_status(self, request, pk=None):
        try:
            obj = self.get_object()
            serializer = SecUserRolesSerializer(obj, data=request.data)
            if serializer.is_valid():
                is_active = serializer.validated_data['cod_rec_status']
                obj.cod_rec_status = is_active
                obj.save()
                if is_active=='A':
                    return success_response("actived")
                elif is_active=='C':
                    return success_response("deactivated")
                else:
                    return error_response("enter correct status, A-->Active,C-->Inactive")
            return error_response("error occured", errors=serializer.errors)
        except Exception as e:
            return error_response("internal server error", errors=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)



class SecUserXRolesViewSet(BaseModelViewSet):
    queryset = SecUserXRoles.objects.all()
    serializer_class = SecUserXRolesSerializer

    @swagger_auto_schema(
        method="get",
        operation_summary="Fetch SecUserXRoles by Login ID",
        operation_description="Returns SecUserXRoles records using integer txt_login_id.",
        manual_parameters=[
            openapi.Parameter(
                name="txt_login_id",
                in_=openapi.IN_PATH,
                description="Login ID (integer)",
                type=openapi.TYPE_INTEGER,
                required=True,
                example=5
            )
        ],
        responses={
            200: SecUserXRolesSerializer(many=True),
            404: "No records found"
        },
        tags=["SecUserXRoles"]
    )
    @action(methods=["get"],permission_classes=[IsAuthenticated],detail=False,url_path=r"fetch-by-login-id/(?P<txt_login_id>\d+)")
    def fetch_by_login_id(self, request, txt_login_id=None):

        try:
            queryset = SecUserXRoles.objects.filter(
                txt_login_id=txt_login_id,
                cod_rec_status="A"
            )

            if not queryset.exists():
                return error_response(
                    "No records found for this login id",
                    status_code=status.HTTP_404_NOT_FOUND
                )

            serializer = self.get_serializer(queryset, many=True)

            return success_response(
                message="Records fetched successfully",
                data=serializer.data,
                status_code=status.HTTP_200_OK
            )

        except Exception as e:
            return error_response(
                "Internal server error",
                errors=str(e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



class SecUserRoleMenusListView(BaseModelViewSet):
    queryset = SecUserRoleMenus.objects.all().order_by(
        "cod_user_role",
        "num_display_order"
    )
    serializer_class = SecUserRoleMenusSerializer

    # =========================
    # FETCH BY ROLE ID
    # =========================
    @swagger_auto_schema(
        method="get",
        operation_summary="Fetch SecUserRoleMenus by role ID",
        operation_description="Returns SecUserRoleMenus records using integer cod_user_role.",
        manual_parameters=[
            openapi.Parameter(
                name="cod_user_role",
                in_=openapi.IN_PATH,
                description="Role ID (integer)",
                type=openapi.TYPE_INTEGER,
                required=True,
                example=5
            )
        ],
        responses={
            200: SecUserRoleMenusSerializer(many=True),
            404: "No records found"
        },
        tags=["SecUserRoleMenus"]
    )
    @action(
        methods=["get"],
        detail=False,
        permission_classes=[IsAuthenticated],
        url_path=r"fetch-by-role-id/(?P<cod_user_role>\d+)"
    )
    def fetch_by_role_id(self, request, cod_user_role=None):

        try:
            queryset = SecUserRoleMenus.objects.filter(
                cod_user_role=cod_user_role,
                cod_rec_status="A"
            )

            if not queryset.exists():
                return error_response(
                    "No records found for this role id",
                    status_code=status.HTTP_404_NOT_FOUND
                )

            serializer = self.get_serializer(queryset, many=True)

            return success_response(
                message="Records fetched successfully",
                data=serializer.data,
                status_code=status.HTTP_200_OK
            )

        except Exception as e:
            return error_response(
                "Internal server error",
                errors=str(e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # =========================
    # ASSIGN MULTIPLE MENUS
    # =========================
    @swagger_auto_schema(
        method="post",
        operation_summary="Assign Multiple Menus to Role",
        operation_description="Insert multiple menus for a single role.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["cod_user_role", "menus"],
            properties={
                "cod_user_role": openapi.Schema(type=openapi.TYPE_INTEGER, example=3),
                "menus": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "cod_menu_option": openapi.Schema(type=openapi.TYPE_INTEGER),
                            "flg_get": openapi.Schema(type=openapi.TYPE_STRING, example="Y"),
                            "flg_post": openapi.Schema(type=openapi.TYPE_STRING, example="N"),
                            "flg_put": openapi.Schema(type=openapi.TYPE_STRING, example="N"),
                            "flg_delete": openapi.Schema(type=openapi.TYPE_STRING, example="N"),
                            "num_display_order": openapi.Schema(type=openapi.TYPE_INTEGER),
                            "cod_rec_status": openapi.Schema(type=openapi.TYPE_STRING, example="A"),
                        }
                    )
                )
            }
        ),
        tags=["SecUserRoleMenus"]
    )
    # @action(
    #     methods=["post"],
    #     detail=False,
    #     permission_classes=[IsAuthenticated],
    #     url_path="assign-menus"
    # )
    # def assign_menus(self, request):

    #     try:
    #         role_id = request.data.get("cod_user_role")
    #         menus = request.data.get("menus", [])

    #         if not role_id or not menus:
    #             return error_response("Role ID and menus are required")

    #         with transaction.atomic():

    #             # Remove existing menus for this role (update behavior)
    #             SecUserRoleMenus.objects.filter(
    #                 cod_user_role=role_id
    #             ).delete()

    #             bulk_objects = []

    #             for menu in menus:
    #                 bulk_objects.append(
    #                     SecUserRoleMenus(
    #                         cod_user_role_id=role_id,
    #                         cod_menu_option_id=menu.get("cod_menu_option"),
    #                         flg_get=menu.get("flg_get", "N"),
    #                         flg_post=menu.get("flg_post", "N"),
    #                         flg_put=menu.get("flg_put", "N"),
    #                         flg_delete=menu.get("flg_delete", "N"),
    #                         num_display_order=menu.get("num_display_order"),
    #                         cod_rec_status=menu.get("cod_rec_status", "A"),
    #                         created_by=request.user,
    #                         updated_by=request.user,
    #                     )
    #                 )

    #             SecUserRoleMenus.objects.bulk_create(bulk_objects)

    #         return success_response(
    #             message="Menus assigned successfully",
    #             status_code=status.HTTP_201_CREATED
    #         )

    #     except Exception as e:
    #         return error_response(
    #             "Internal server error",
    #             errors=str(e),
    #             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    #         )
    @action(methods=["post"],detail=False,permission_classes=[IsAuthenticated],url_path="assign-menus")
    def assign_menus(self, request):

     try:
        role_id = request.data.get("cod_user_role")
        menus = request.data.get("menus", [])

        if not role_id or not menus:
            return error_response("Role ID and menus are required")

        with transaction.atomic():

            # Fetch existing menus for role
            existing_qs = SecUserRoleMenus.objects.filter(
                cod_user_role=role_id
            )

            existing_menu_map = {
                obj.cod_menu_option_id: obj
                for obj in existing_qs
            }

            for menu in menus:
                menu_id = menu.get("cod_menu_option")

                if not menu_id:
                    continue

                if menu_id in existing_menu_map:
                    # 🔄 UPDATE existing record
                    obj = existing_menu_map[menu_id]
                    obj.flg_get = menu.get("flg_get", "N")
                    obj.flg_post = menu.get("flg_post", "N")
                    obj.flg_put = menu.get("flg_put", "N")
                    obj.flg_delete = menu.get("flg_delete", "N")
                    obj.num_display_order = menu.get("num_display_order")
                    obj.cod_rec_status = menu.get("cod_rec_status", "A")
                    obj.updated_by = request.user
                    obj.save()

                else:
                    # ➕ CREATE new record
                    SecUserRoleMenus.objects.create(
                        cod_user_role_id=role_id,
                        cod_menu_option_id=menu_id,
                        flg_get=menu.get("flg_get", "N"),
                        flg_post=menu.get("flg_post", "N"),
                        flg_put=menu.get("flg_put", "N"),
                        flg_delete=menu.get("flg_delete", "N"),
                        num_display_order=menu.get("num_display_order"),
                        cod_rec_status=menu.get("cod_rec_status", "A"),
                        created_by=request.user,
                        updated_by=request.user,
                    )

        return success_response(
            message="Menus processed successfully",
            status_code=status.HTTP_200_OK
        )

     except Exception as e:
        return error_response(
            "Internal server error",
            errors=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

class SecUserRoleDisclosuresListView(BaseModelViewSet):
    queryset = SecUserRoleDisclosures.objects.all().order_by(
        "cod_user_role",
        "num_sequence"
    )
    serializer_class = SecUserRoleDisclosuresSerializer



from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status


class MyMenusView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Get Logged-in User Menus",
        operation_description=(
            "Returns merged menu list for the logged-in user "
            "based on assigned roles. Used by frontend to render sidebar."
        ),
        responses={
            200: openapi.Response(
                description="Menus fetched successfully",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "status": openapi.Schema(type=openapi.TYPE_STRING, example="success"),
                        "message": openapi.Schema(type=openapi.TYPE_STRING, example="Menus fetched successfully"),
                        "status_code": openapi.Schema(type=openapi.TYPE_INTEGER, example=200),
                        "data": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=5),
                                    "cod_menu_option": openapi.Schema(type=openapi.TYPE_STRING, example="CMP1"),
                                    "txt_menu_desc": openapi.Schema(type=openapi.TYPE_STRING, example="Campaigns"),
                                    "url": openapi.Schema(type=openapi.TYPE_STRING, example="/campaigns"),
                                    "icon": openapi.Schema(type=openapi.TYPE_STRING, example="campaign-icon"),
                                    "parent_id": openapi.Schema(type=openapi.TYPE_INTEGER, example=None),
                                    "display_order": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                                    "flg_get": openapi.Schema(type=openapi.TYPE_STRING, example="Y"),
                                    "flg_post": openapi.Schema(type=openapi.TYPE_STRING, example="N"),
                                    "flg_put": openapi.Schema(type=openapi.TYPE_STRING, example="Y"),
                                    "flg_delete": openapi.Schema(type=openapi.TYPE_STRING, example="N"),
                                }
                            )
                        )
                    }
                )
            ),
            401: openapi.Response(
                description="Unauthorized - Invalid or missing token"
            )
        },
        tags=["Menu"],
        security=[{"Bearer": []}]
    )
    def get(self, request):

        # ✅ Get roles from JWT
        role_ids = request.auth.get("role_ids", [])

        if not role_ids:
            return success_response(
                message="No roles assigned",
                data=[],
                status_code=status.HTTP_200_OK
            )

        # ✅ Fetch active role-menu mappings
        role_menus = SecUserRoleMenus.objects.filter(
            cod_user_role_id__in=role_ids,
            cod_rec_status='A'
        ).select_related("cod_menu_option")

        merged_menus = {}

        for rm in role_menus:
            menu = rm.cod_menu_option

            # 🔐 Skip if menu is NULL (important fix)
            if not menu:
                continue

            # ✅ Create entry if not already added
            if menu.id not in merged_menus:
                merged_menus[menu.id] = {
                    "id": menu.id,
                    "cod_menu_option": menu.cod_menu_option,
                    "txt_menu_desc": menu.txt_menu_desc,
                    "url": menu.url,
                    "icon": menu.bin_menu_icon,
                    "parent_id": menu.cod_parent_menu_option_id,
                    "display_order": rm.num_display_order or 0,
                    "flg_get": "N",
                    "flg_post": "N",
                    "flg_put": "N",
                    "flg_delete": "N"
                }


            # ✅ Merge permissions (Y overrides N)
            if rm.flg_get == "Y":
                merged_menus[menu.id]["flg_get"] = "Y"

            if rm.flg_post == "Y":
                merged_menus[menu.id]["flg_post"] = "Y"

            if rm.flg_put == "Y":
                merged_menus[menu.id]["flg_put"] = "Y"

            if rm.flg_delete == "Y":
                merged_menus[menu.id]["flg_delete"] = "Y"

        # ✅ Convert to list
        menu_list = list(merged_menus.values())

        menu_list = [
            m for m in menu_list
            if "Y" in (m["flg_get"], m["flg_post"], m["flg_put"], m["flg_delete"])
        ]

        # ✅ Sort by display order
        menu_list.sort(key=lambda x: x["display_order"])

        # ✅ If no valid menus found
        if not menu_list:
            return success_response(
                message="No menus assigned",
                data=[],
                status_code=status.HTTP_200_OK
            )

        return success_response(
            message="Menus fetched successfully",
            data=menu_list,
            status_code=status.HTTP_200_OK
        )