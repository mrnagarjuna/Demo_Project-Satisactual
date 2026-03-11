from .views import MstProdCodesViewset,MstProdDisclosuresViewSet,MstProdDocsViewSet,MstPromoCodesViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'mst-prod-codes',MstProdCodesViewset,basename='mst-prod-codes')
router.register(r'mst-prod-disclosure',MstProdDisclosuresViewSet,basename='mst-prod-disclosure')
router.register(r'mst-prod-docs',MstProdDocsViewSet,basename='mst-prod-docs')
router.register(r'mst-promo-codes',MstPromoCodesViewSet,basename='mst-promo-codes')

urlpatterns = [
    path('', include(router.urls)),
]
