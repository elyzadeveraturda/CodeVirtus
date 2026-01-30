from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccidentReportViewSet

router = DefaultRouter()
router.register(r'reports', AccidentReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]