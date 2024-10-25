from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.db.models import Count
from . import models
# Register your models here.


@admin.register(models.RoomType, models.RoomFacility, models.RoomAmenity, models.RoomRule)
class ItemAdmin(admin.ModelAdmin):
    verbose_name = _('Item Admin')
    list_display = ('name', 'used_by')

    def used_by(self, obj):
        return obj.rooms.count()


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
        "images",
        "total_rating",
    ]
    list_filter = ['city', 'country', 'instant_book']
    search_fields = ['city', 'host__username']
    filter_horizontal = ['room_amenity', "house_rule",
                         "room_facility",]
    inlines = [RoomImageInline]

    @admin.display(ordering='amenities')
    def amenities(self, room: models.Room):
        if room.room_amenity.exists():
            amenity = room.room_amenity.all()
            return ', '.join([str(a) for a in amenity])
        return 0

    @admin.display(ordering='images')
    def images(self, room: models.Room):
        if room.images.exists():
            return room.images.count()
        return 0

    @admin.display(ordering='price')
    def price(self, room: models.Room):
        return f"{room.price:,}"


@admin.register(models.RoomImage)
class RoomPhotoAdmin(admin.ModelAdmin):
    pass
