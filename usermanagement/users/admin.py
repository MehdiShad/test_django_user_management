from django.contrib import admin
from usermanagement.users import models
# Register your models here.


@admin.register(models.BaseUser)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'type', 'is_active']
    list_editable = ['type', 'is_active']
    list_display_links = ['id', 'email']
