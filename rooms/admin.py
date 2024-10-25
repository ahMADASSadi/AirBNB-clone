from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.db.models import Count
from . import models
# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.Rule)
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
    readonly_fields = ['get_thumbnail']
    verbose_name = _('Room Image')
    verbose_name_plural = _('Room Images')

    def get_thumbnail(self, images: models.RoomImage):
        # Customize thumbnail size and wrap in a container for potential slider styling
        return format_html(
            f'<div class="slider"><img src="{
                images.image.url}" class="thumbnail" style=" width:200px; height:200px; object-fit: cover;" /></div>'
        )
    get_thumbnail.short_description = 'Thumbnail'

    class Media:
        css = {
            # Custom CSS for styling the slider
            'all': ('room/css/style.css',),
        }
        js = ('room/js/slider.js',)


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
                'room_amenity', "house_rule", "room_facility", 'room_type')}),
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

    raw_id_fields = ['host']

    @admin.display(ordering='amenities')
    def amenities(self, room: models.Room):
        if room.room_amenity.exists():
            amenity = room.room_amenity.all()
            return f"{', '.join([str(a) for a in amenity]):.10}"
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
    list_display = ['__str__', 'get_thumbnail']

    def get_thumbnail(self, images: models.RoomImage):
        # Customize thumbnail size and wrap in a container for potential slider styling
        return format_html(
            f'<div class="slider"><img src="{
                images.image.url}" class="thumbnail"  style=" width:200px; height:200px; object-fit: cover;"/></div>'
        )
    get_thumbnail.short_description = 'Thumbnail'

    class Media:
        css = {
            # Custom CSS for styling the slider
            'all': ('room/css/style.css',),
        }
        js = ('room/js/slider.js',)
