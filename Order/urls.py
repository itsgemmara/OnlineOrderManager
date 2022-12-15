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

material_router = DefaultRouter()
material_router.register(r'material-view-set', MaterialViewSet, basename='materials')

products_router = DefaultRouter()
products_router.register(r'products-view-set', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(table_router.urls)),
    path('create-order/', CreateOrderView.as_view()),
    path('pay/', include(pay_router.urls)),
    path('material/', include(material_router.urls)),
    path('product/', include(products_router.urls)),
]
