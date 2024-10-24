from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ListsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lists'
    verbose_name = _('Lists')
