from rest_framework.permissions import BasePermission
from ..roles.models import SecUserRoleMenus




# class RoleBasedMenuPermission(BasePermission):

#     def has_permission(self, request, view):

#         if not request.user.is_authenticated:
#             print('authenticated')
#             return False

#         if request.user.is_superuser:
#             print('superuser')
#             return True

#         view_menu_id = getattr(view, "menu_id", None)
#         if not view_menu_id:
#             return False

#         menu_permissions = request.auth.get("menu_permissions", [])

#         menu = next(
#             (m for m in menu_permissions if m["cod_menu_option_id"] == view_menu_id),
#             None
#         )

#         if not menu:
#             return False

#         action = view.action

#         # Standard CRUD
#         if action in ["list", "retrieve"]:
#             return menu["flg_get"] == "Y"

#         if action == "create":
#             return menu["flg_post"] == "Y"

#         if action in ["update", "partial_update"]:
#             return menu["flg_put"] == "Y"

#         if action == "destroy":
#             return menu["flg_delete"] == "Y"

#         # Custom actions
#         if action == "activeCities":
#             return menu["flg_get"] == "Y"

#         if action == "toggle_status":
#             return menu["flg_put"] == "Y"

#         return False

from rest_framework.permissions import BasePermission


class RoleBasedMenuPermission(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        role_ids = request.auth.get("role_ids", [])
        if not role_ids:
            return False

        view_menu_id = getattr(view, "menu_id", None)
        if not view_menu_id:
            return False

        # 🔹 Fetch from DB
        role_menus = SecUserRoleMenus.objects.filter(
            cod_user_role_id__in=role_ids,
            cod_menu_option_id=view_menu_id,
            cod_rec_status='A'
        )

        if not role_menus.exists():
            return False

        # 🔹 Merge permissions (union)
        can_get = False
        can_post = False
        can_put = False
        can_delete = False

        for rm in role_menus:
            if rm.flg_get == "Y":
                can_get = True
            if rm.flg_post == "Y":
                can_post = True
            if rm.flg_put == "Y":
                can_put = True
            if rm.flg_delete == "Y":
                can_delete = True

        action = view.action

        if action in ["list", "retrieve"]:
            return can_get

        if action == "create":
            return can_post

        if action in ["update", "partial_update"]:
            return can_put

        if action == "destroy":
            return can_delete

        # Custom actions
        if action == "activeCities":
            return can_get

        if action == "toggle_status":
            return can_put

        return False