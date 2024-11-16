from django.contrib import admin
from .models import Department, Position, Employee

class DepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields if field.name != 'id']  # Display all fields except 'id' in the list view
    fields = [field.name for field in Department._meta.fields if field.name not in ['id', 'created_at', 'updated_at']]  # Exclude 'id', 'created_at', 'updated_at' in the detail view

admin.site.register(Department, DepartmentAdmin)

class PositionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Position._meta.fields if field.name != 'id']  # Display all fields except 'id' in the list view
    fields = [field.name for field in Position._meta.fields if field.name not in ['id', 'created_at', 'updated_at']]  # Exclude 'id', 'created_at', 'updated_at' in the detail view

admin.site.register(Position, PositionAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields if field.name != 'id']  # Display all fields except 'id' in the list view
    fields = [field.name for field in Employee._meta.fields if field.name not in ['id', 'created_at', 'updated_at']]  # Exclude 'id', 'created_at', 'updated_at' in the detail view

admin.site.register(Employee, EmployeeAdmin)
