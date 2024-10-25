from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models
# Register your models here.


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    verbose_name = _('Review')
    verbose_name_plural = _('Reviews')

    list_display = [
        "room__name",
        "room__host",
        "customer",
        "review_text",
        "accuracy",
        "communication",
        "cleanliness",
        "location",
        "check_in",
        "value",
        'get_average'
    ]
