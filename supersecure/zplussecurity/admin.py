from django.contrib import admin
from .models import KeyRequest

@admin.register(KeyRequest)
class KeyRequestAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'employee_email', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('employee_id', 'employee_name', 'employee_email')
