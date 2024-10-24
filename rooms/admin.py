from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.db.models import Count
from . import models
# Register your models here.


@admin.register(models.RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    verbose_name = _('Room Type')


@admin.register(models.RoomAmenity)
class RoomAmenityAdmin(admin.ModelAdmin):
    verbose_name = _('Room Amenity')


@admin.register(models.RoomFacility)
class RoomFacilityAdmin(admin.ModelAdmin):
    verbose_name = _('Room Facility')


@admin.register(models.RoomRule)
class RoomRuleAdmin(admin.ModelAdmin):
    verbose_name = _('Room Rule')


class RoomImageInline(admin.StackedInline):
    model = models.RoomImage
    extra = 0
    min_num = 1
    max_num = 10
    readonly_fields = ['thumbnail']
    verbose_name = _('Room Image')
    verbose_name_plural = _('Room Images')

    def thumbnail(self, instance):
        print(f"Image URL: {instance.image.url}")
        if instance.image.name != " ":  # Check if the image exists
            return format_html(f'<img src="{instance.image.url}" class=thumbnail />')
        print(_("No image found"))  # Debugging line
        return _("No Image Available")

    thumbnail.short_description = _('Image Thumbnail')


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    verbose_name = _('Room')
    verbose_name_plural = _('Rooms')
    fieldsets = (
        (_('Basic Info'), {
            'fields': (
                'name', 'description', 'country', 'address', 'price')}),
        (_("Times"), {
            'fields': (
                'check_in', 'check_out', 'instant_book')}),
        (_("Spaces"), {
            'fields': (
                'guest', "bed", "bedroom", 'bath')}),
        (_("More About the space"), {
            'fields': (
                'room_amenity', "house_rule", "room_facility")}),
        (_("Last Detail"), {
            'fields': (
                'host',)}),
    )
    list_display = [
        "name",
        "country",
        "city",
        "price",
        "bed",
        "bedroom",
        "guest",
        "check_in",
        "check_out",
        "instant_book",
        "host",
        "amenities",

    ]
    list_filter = ['city', 'country', 'instant_book']
    search_fields = ['city', 'host__username']
    filter_horizontal = ['room_amenity', "house_rule",
                         "room_facility",]
    inlines = [RoomImageInline]

    @admin.display(ordering='amenities')
    def amenities(self, room: models.Room):
        if room.room_amenity.exists():
            return room.room_amenity.all()
        return 0
        # @admin.register(models.RoomPhoto)
        # class RoomPhotoAdmin(admin.ModelAdmin):
        # pass
