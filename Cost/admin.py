from django.contrib import admin

from .models import PeriodicCost, Cost, PeriodicIncome, Income

admin.site.register(PeriodicCost)
admin.site.register(Cost)
admin.site.register(PeriodicIncome)
admin.site.register(Income)
# admin.site.register('')
# admin.site.register('')
