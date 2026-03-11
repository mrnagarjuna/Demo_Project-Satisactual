# api/user/urls.py
from django.urls import path
from .views import JWTLoginView, JWTLogoutView

urlpatterns = [
    path("login/", JWTLoginView.as_view(), name="jwt-login"),
    path("logout/", JWTLogoutView.as_view(), name="jwt-logout"),
]
