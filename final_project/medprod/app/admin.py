from django.contrib import admin
from .models import Product, Application, Consumer, Consumption, Supplier, Material, Material_costs_1000units, Employee

admin.site.register(Product)
admin.site.register(Application)
admin.site.register(Consumer)
admin.site.register(Consumption)
admin.site.register(Supplier)
admin.site.register(Material)
admin.site.register(Material_costs_1000units)
admin.site.register(Employee)