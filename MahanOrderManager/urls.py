from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Mahan orders API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Order.urls')),
    path('personnel/', include('Personnel.urls')),
    path('cost/', include('Cost.urls')),
    path('swagger/', schema_view),
]
