from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from core.models import TimeStampedModel

# Create your models here.


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
    desciption = models.TextField(help_text=_(
        "Enter Your Decription of the Room Here"), verbose_name=_('Descpription'))
    country = CountryField(verbose_name=_('Country'))
    city = models.CharField(max_length=100, verbose_name=_('City'))
    price = models.IntegerField(verbose_name=_("Price"))
    address = models.CharField(max_length=1400, verbose_name=_('Address'))
    bed = models.SmallIntegerField(verbose_name=_('Bed'))
    bedroom = models.SmallIntegerField(verbose_name=_('Bedroom'))
    guest = models.SmallIntegerField(verbose_name=_('Guest'))
    check_in = models.TimeField(verbose_name=_('Check In'))
    check_out = models.TimeField(verbose_name=_('Check Out'))
    instant_book = models.BooleanField(
        verbose_name=_('Instant Book'), default=False)
    host = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, verbose_name=_('Host'))
    room_type = models.ForeignKey(
        RoomType, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('Room Type'))

    room_amenity = models.ManyToManyField(
        RoomAmenity, blank=True, verbose_name=_('Room Amenities'))

    room_facility = models.ForeignKey(
        RoomFacility, on_delete=models.SET_NULL, verbose_name=_("Room Facility"), null=True)

    room_rule = models.ManyToManyField(
        RoomRule, related_name='room_rules', verbose_name=_('Room Rule'), blank=True)

    def __str__(self) -> str:
        return f"{self.name} , {self.host.email} , {self.country}"

    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _("Rooms")
