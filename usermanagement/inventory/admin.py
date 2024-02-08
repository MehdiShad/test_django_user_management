from django.contrib import admin
from usermanagement.inventory import models
from django.contrib.auth.admin import UserAdmin
from usermanagement.users.models import BaseUser
from django.contrib.auth.models import Group

# admin.site.unregister(Group)


class ReadOnlyAdminMixin:

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.has_perm('inventory.change_product'):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True



@admin.register(models.Product)
class ProductAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'slug',]
    # list_editable = ['type', 'is_active']
    list_display_links = ['id', 'name']
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['name'].disabled = True

        return form


