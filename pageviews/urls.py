from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PageViewViewSet

router = DefaultRouter()
router.register(r'pageviews', PageViewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
