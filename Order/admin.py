from django.contrib import admin

from .models import Order, Menu, Table, Category

admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Table)
admin.site.register(Category)