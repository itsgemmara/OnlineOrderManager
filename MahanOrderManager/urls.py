from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Order.urls')),
    path('personnel/', include('Personnel.urls')),
    path('cost/', include('Cost.urls'))
]
