from django.contrib import admin
from usermanagement.users import models
# Register your models here.


@admin.register(models.BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'type', 'is_staff', 'is_active']
    list_editable = ['type', 'is_active']
    list_display_links = ['id', 'email']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['email'].disabled = True
            form.base_fields['is_superuser'].disabled = True
            form.base_fields['user_permissions'].disabled = True
            form.base_fields['groups'].disabled = True
        return form
