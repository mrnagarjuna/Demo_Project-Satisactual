"""
URL configuration for satisactual project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title="Satisactual API",
        default_version='v1',
        description="API documentation for the satisactual project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="manojkumartippani@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[JWTAuthentication],
)


from rest_framework_simplejwt.authentication import JWTAuthentication

SWAGGER_AUTH = [
    {
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'JWT Authorization header using the Bearer scheme. Example: "Bearer <token>"',
        }
    }
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.masters.urls')), 
    path('api/',include('api.campaign.urls')),
    path('api/',include('api.contact.urls')),
    path('api/',include('api.user.urls')),
    path('api/',include('api.auth.urls')),
    path('api/',include('api.roles.urls')),
    path('api/',include('api.product.urls')),
    path('api/',include('api.questionnaries.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   