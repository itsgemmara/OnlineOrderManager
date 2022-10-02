from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import *

personnel_router = DefaultRouter()
personnel_router.register(r'personnel-view-set', PersonnelViewSet, basename='personnel')

urlpatterns = [
    path('', include(personnel_router.urls)),
]
