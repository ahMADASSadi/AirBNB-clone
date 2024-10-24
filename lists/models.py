from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampedModel
# Create your models here.


class List(TimeStampedModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, verbose_name=_('User'))
    room = models.ManyToManyField(
        'rooms.Room', blank=True, related_name='rooms', verbose_name=_('Room'))

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = _('List')
        verbose_name_plural = _('Lists')
