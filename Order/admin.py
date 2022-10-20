from django.contrib import admin

from .models import Order, Menu, Table, Category, Material, Product

admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Table)
admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Product)