from django.contrib import admin
from django.db import models

from . models import Employees, Vehicles, Transactions, Departments, Genders

# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'employee_dept', 'employee_post', 'employee_gender')
    list_per_page = 10

    def has_delete_permission(self, request, obj=None):
        return True

class VehiAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id', 'vehicle_plate', 'vehicle_type', 'vehicle_emp')
    list_per_page = 10

    def has_delete_permission(self, request, obj=None):
        return True

class TxnAdmin(admin.ModelAdmin):
    list_display = ('txn_id', 'txn_plate', 'txn_state', 'txn_date', 'txn_created', 'txn_updated')
    list_per_page = 10

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(Employees, EmpAdmin)
admin.site.register(Vehicles, VehiAdmin)
admin.site.register(Transactions, TxnAdmin)