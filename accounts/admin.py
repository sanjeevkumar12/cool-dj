from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AdminUser

from .models import User
class UserAdmin(AdminUser):

    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('firstname', 'lastname', 'user_bio','image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', )}),
        ('Personal info', {'fields': ('firstname', 'lastname','user_bio','image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    list_display = ( 'email', 'firstname', 'lastname', 'is_active', 'is_staff',)
    list_editable = ( 'firstname', 'lastname','is_active',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',)
    search_fields = ('email', 'firstname', 'lastname')
    ordering = ('lastname','firstname',)
# Register your models here.
admin.site.register(User,UserAdmin)