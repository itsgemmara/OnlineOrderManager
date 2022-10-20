from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import *
from .views import CreateOrderView

table_router = DefaultRouter()
table_router.register(r'table-view-set', TableViewSet, basename='tables')

order_router = DefaultRouter()
order_router.register(r'order-view-set', OrderViewSet, basename='orders')

pay_router = DefaultRouter()
pay_router.register(r'pay-view-set', PayViewSet, basename='pays')

urlpatterns = [
    path('', include(table_router.urls)),
    path('order/', include(order_router.urls)),
    path('create-order/', CreateOrderView.as_view()),
    path('pay/', include(pay_router.urls)),
]
