# from django.contrib import admin
# from django.db import models
#
# from . models import Departments, Genders
# # Register your models here.
#
# class DeptAdmin(admin.ModelAdmin):
#     list_display = ('dept_id','dept_name')
#     list_per_page = 10
#
#     def has_delete_permission(self, request, obj=None):
#         return True

# class GendAdmin(admin.ModelAdmin):
#     list_display = ('gender_type')
#     list_per_page = 10
#
#     def has_delete_permission(self, request, obj=None):
#         return True

# admin.site.register(Departments, DeptAdmin)
# admin.site.register(Genders)