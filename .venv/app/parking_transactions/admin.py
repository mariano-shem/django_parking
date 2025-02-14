from django.contrib import admin
import nested_admin
from django.db import models

from . models import Employees, Vehicles, Transactions, DepartmentPositions, Genders

# Register your models here.

class TxnModelInline(nested_admin.NestedTabularInline):
    model = Transactions
    extra = 0
    raw_id_fields = ('txn_plate',)
    autocomplete_fields = ['txn_plate']

class VehiModelInline(nested_admin.NestedTabularInline):
    model = Vehicles
    extra = 0
    raw_id_fields = ('vehicle_emp',)
    autocomplete_fields = ['vehicle_emp']
    inlines = [TxnModelInline]

class EmpAdmin(nested_admin.NestedModelAdmin):
    list_display = ('employee_name', 'employee_gender', 'employee_post', 'employee_dept')
    search_fields = ['employee_name', 'employee_post', 'employee_dept']
    inlines = [VehiModelInline]
    list_per_page = 10

    def has_delete_permission(self, request, obj=None):
        return True

class VehiAdmin(nested_admin.NestedModelAdmin):
    list_display = ('vehicle_id', 'vehicle_plate', 'vehicle_type', 'vehicle_emp')
    search_fields = ['vehicle_plate']
    inlines = [TxnModelInline]
    list_per_page = 10
    def has_delete_permission(self, request, obj=None):
        return True

class TxnAdmin(admin.ModelAdmin):
    list_display = ('txn_id', 'txn_plate', 'txn_state', 'txn_date', 'txn_created', 'txn_updated')
    search_fields = ['txn_plate', 'txn_state']
    list_per_page = 10

    def has_delete_permission(self, request, obj=None):
        return True

# class DeptPostAdmin(admin.ModelAdmin):
#     list_display = ('dept_post_id', 'dept_post', 'dept_name')
#     list_per_page = 10
#
#     def has_delete_permission(self, request, obj=None):
#         return True

admin.site.register(Employees, EmpAdmin)
admin.site.register(Vehicles, VehiAdmin)
admin.site.register(Transactions, TxnAdmin)
# admin.site.register(DepartmentPositions, DeptPostAdmin)