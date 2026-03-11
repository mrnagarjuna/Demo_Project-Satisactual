from rest_framework import routers
from django.urls import path, include
from .views import SecUserMasterViewSet,SecUserPreferencesViewSet,SecUserAccessLogListView,SecUserPswdHistViewSet,ChangePassword

router = routers.DefaultRouter()
router.register(r'sec-user-master', SecUserMasterViewSet,basename='userregister')
router.register(r'sec-user-preferences',SecUserPreferencesViewSet,basename='userprofile')
router.register(r'mst-user-log-access',SecUserAccessLogListView,basename='mstuserlog')
router.register(r'sec-user-pswd-hist',SecUserPswdHistViewSet,basename='secuserpswdhist')



urlpatterns = [
    path('', include(router.urls)),
    path("sec-change-password/",ChangePassword.as_view(),name="change-password")
]
