from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RoomsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rooms'
    verbose_name = _('Room')
    verbose_name_plural = _('Rooms')
