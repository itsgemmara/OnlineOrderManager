from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import *

cost_router = DefaultRouter()
cost_router.register(r'cost-view-set', CostViewSet, basename='cost')

periodic_cost_router = DefaultRouter()
periodic_cost_router.register(r'periodic_cost-view-set', PeriodicCostViewSet, basename='periodic_cost')

urlpatterns = [
    path('cost/', include(cost_router.urls)),
    path('periodic_cost/', include(periodic_cost_router.urls)),
]
