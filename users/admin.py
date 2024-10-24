from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (_('personal info'), {'fields': ('avatar',
         'gender', 'bio', 'birth_date', 'language', 'superhost')}),

    )
    fieldsets += UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets
