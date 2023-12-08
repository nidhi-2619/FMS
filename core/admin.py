"""
Django admin customization
"""


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _("Permissions"),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),

    ]


class FileAdmin(admin.ModelAdmin):
    """Customising recipe admin  to display other fields"""
    list_display = ('file', 'user', 'created_at', 'size')

    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True




admin.site.register(models.User, UserAdmin)
admin.site.register(models.File, FileAdmin)
