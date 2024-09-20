from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models
# Register your models here.


@admin.register(models.RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    verbose_name = _('Room Type')
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    verbose_name = _('Room')
    list_display = ['name', 'host', 'bed', 'bedroom', 'price']
    list_filter = ['name', 'host', 'price']
    search_fields = ['name']
