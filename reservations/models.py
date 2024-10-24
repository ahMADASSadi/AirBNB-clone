from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from core.models import TimeStampedModel
# Create your models here.


class Reservation(TimeStampedModel):
    """Reservation Model Definition"""

    STATUS_PENDING = _('Pending')
    STATUS_CONFIRM = _('Confirmed')
    STATUS_CANCELED = _('Canceled')

    STATUS_CHOICES = (
        (STATUS_PENDING, _('Pending')),
        (STATUS_CONFIRM, _('Confirmed')),
        (STATUS_CANCELED, _('Canceled')),
    )

    status = models.CharField(max_length=12, choices=STATUS_CHOICES,
                              default=STATUS_PENDING, verbose_name=_('Status'))
    guest = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, verbose_name=_('Guest'))
    room = models.ForeignKey(
        'rooms.Room', on_delete=models.CASCADE, verbose_name=_("Room"))
    check_in = models.DateField(verbose_name=_('Check In'))
    check_out = models.DateField(verbose_name=_('Check Out'))

    def __str__(self) -> str:
        return f"({self.status}) {self.room} :{self.check_in} -> {self.check_out}"

    class Meta:
        verbose_name = _("Reservation")
        verbose_name_plural = _("Reservations")
