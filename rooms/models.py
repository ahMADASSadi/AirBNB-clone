from typing import Iterable
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from core.models import TimeStampedModel

# Create your models here.


class RoomImage(TimeStampedModel):
    """Photo model Definition"""
    caption = models.CharField(
        max_length=150, null=True, blank=True, verbose_name=_('Caption'))
    image = models.ImageField(
        upload_to='rooms/images', verbose_name=_("Image"))

    room = models.ForeignKey(
        'Room', on_delete=models.CASCADE, verbose_name=_('Room'), related_name='images')

    def __str__(self) -> str:
        return f"{self.caption}"

    class Meta:
        verbose_name = _('Room Image')
        verbose_name_plural = _("Room Images")


class AbstractItem(TimeStampedModel):
    """Abstract Item"""

    name = models.CharField(max_length=100, verbose_name=_('Name'))

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        abstract = True


class RoomType(AbstractItem):
    """Type of The Room"""
    class Meta:
        verbose_name = _('Room Type')
        verbose_name_plural = _("Room Types")


class RoomAmenity(AbstractItem):
    """Amenities of The Room"""

    class Meta:
        verbose_name = _('Room Amenity')
        verbose_name_plural = _("Room Amenities")


class RoomFacility(AbstractItem):
    """ Facility of The Room"""
    class Meta:
        verbose_name = _('Room Facility')
        verbose_name_plural = _("Room Facilities")


class RoomRule(AbstractItem):
    """Rules of The Room"""
    class Meta:
        verbose_name = _('Room Rule')
        verbose_name_plural = _("Room Rules")


class Room(TimeStampedModel):
    """Room model"""
    name = models.CharField(max_length=140, verbose_name=_('Name'))
    description = models.TextField(help_text=_(
        "Enter Your Decription of the Room Here"), verbose_name=_('Descpription'))
    country = CountryField(verbose_name=_('Country'))
    city = models.CharField(max_length=100, verbose_name=_('City'))
    price = models.IntegerField(verbose_name=_("Price"))
    address = models.CharField(max_length=1400, verbose_name=_('Address'))
    bed = models.SmallIntegerField(verbose_name=_('Bed'))
    bedroom = models.SmallIntegerField(verbose_name=_('Bedroom'))
    bath = models.SmallIntegerField(verbose_name=_('Bath'))
    guest = models.SmallIntegerField(verbose_name=_('Guest'))
    check_in = models.TimeField(verbose_name=_('Check In'))
    check_out = models.TimeField(verbose_name=_('Check Out'))
    instant_book = models.BooleanField(
        verbose_name=_('Instant Book'), default=False)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rooms',
                             on_delete=models.CASCADE, verbose_name=_('Host'))
    room_type = models.ForeignKey(
        RoomType, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('Room Type'), related_name='rooms',)

    room_amenity = models.ManyToManyField(
        RoomAmenity, blank=True, verbose_name=_('Room Amenities'), related_name='rooms')

    room_facility = models.ManyToManyField(
        RoomFacility, verbose_name=_("Room Facility"), blank=True, related_name='rooms')

    house_rule = models.ManyToManyField(
        RoomRule, related_name='rooms', verbose_name=_('Room Rule'), blank=True)

    def __str__(self) -> str:
        return f"{self.name} , {self.host.email} , {self.country}"

    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _("Rooms")

    def save(self, *args, **kwargs):
        # self.name = self.name.strip()
        self.city = self.city.capitalize()
        super().save(*args, **kwargs)

    def total_rating(self):
        reviews = self.reviews.all()
        total = 0
        for review in reviews:
            total += review.get_average()
        if total > 0:
            return round(total / len(reviews), 1)
        else:
            return 0
