from django.contrib import admin
from . import models
# Register your models here.


from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from datetime import date


class InProgressFilter(admin.SimpleListFilter):
    title = _('In Progress')
    parameter_name = 'in_progress'

    def lookups(self, request, model_admin):
        return (
            ('Yes', _('Yes')),
            ('No', _('No')),
        )

    def queryset(self, request, queryset):
        today = date.today()
        if self.value() == 'Yes':
            return queryset.filter(check_in__lte=today, check_out__gte=today)
        if self.value() == 'No':
            return queryset.exclude(check_in__lte=today, check_out__gte=today)


class IsAvailableFilter(admin.SimpleListFilter):
    title = _('Is Available')
    parameter_name = 'is_available'

    def lookups(self, request, model_admin):
        return (
            ('Yes', _('Yes')),
            ('No', _('No')),
        )

    def queryset(self, request, queryset):
        today = date.today()
        if self.value() == 'Yes':
            return queryset.filter(check_in__gt=today) | queryset.filter(check_out__lt=today)
        if self.value() == 'No':
            return queryset.filter(check_in__lte=today, check_out__gte=today)


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['room__name', 'guest', 'status',
                    'check_in', 'check_out', 'in_progress', 'is_available']

    list_filter = ["status", InProgressFilter, IsAvailableFilter]
