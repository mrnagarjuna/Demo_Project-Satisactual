from rest_framework.routers import DefaultRouter
from .views import SecUserRolesViewSet,SecUserXRolesViewSet,SecUserRoleMenusListView,SecUserRoleDisclosuresListView,MyMenusView
from django.urls import path, include

router = DefaultRouter()
router.register(r"mst-user-roles", SecUserRolesViewSet, basename="mstuserroles")
router.register(r"mst-user-x-roles",SecUserXRolesViewSet,basename="mstuserxroles")
router.register(r'mst-user-role-menus',SecUserRoleMenusListView,basename='mstuserrolemenus')
router.register(r'mst-user-role-disclosures',SecUserRoleDisclosuresListView,basename="mstuserroledisclosures")


urlpatterns = [
    path('', include(router.urls)),
    path("my-menus/", MyMenusView.as_view(), name="my-menus")
]

