from django.contrib import admin

from .models import PeriodicCost, Cost, PeriodicIncome, Income, Material, OrderCost

admin.site.register(PeriodicCost)
admin.site.register(Cost)
admin.site.register(PeriodicIncome)
admin.site.register(Income)
admin.site.register(Material)
admin.site.register(OrderCost)
# admin.site.register('')
# admin.site.register('')
