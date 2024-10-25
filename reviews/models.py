from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampedModel
# Create your models here.


class Review(TimeStampedModel):
    """Review Model Definition"""
    review_text = models.TextField(verbose_name=_('Review Text'))

    accuracy = models.DecimalField(
        max_digits=3, decimal_places=2, verbose_name=_('Accuracy'))
    communication = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)],
                                        max_digits=3, decimal_places=2, verbose_name=_('Communication'))
    cleanliness = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)],
                                      max_digits=3, decimal_places=2, verbose_name=_('Cleanliness'))
    location = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)],
                                   max_digits=3, decimal_places=2, verbose_name=_('Location'))
    check_in = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)],
                                   max_digits=3, decimal_places=2, verbose_name=_('Check In'))
    value = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(5)],
                                max_digits=3, decimal_places=2, verbose_name=_('Value'))

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('Customer'))
    room = models.ForeignKey(
        'rooms.Room', related_name='reviews', on_delete=models.CASCADE, verbose_name=_('Room'))

    def __str__(self) -> str:
        return f"{self.customer.username} {self.room.name} {self.review_text}"

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _("Reviews")

    def get_average(self):
        avg = (self.accuracy + self.communication + self.cleanliness +
               self.location + self.check_in + self.value) / 6
        return round(avg, 1)
    get_average.short_description = _('Average')
