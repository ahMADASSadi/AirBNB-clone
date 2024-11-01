from django import forms
from django_countries.fields import CountryField
from rooms.models import Amenity, Facility, RoomType


class SearchForm(forms.Form):

    city = forms.CharField(max_length=100, label='City',
                           help_text='Enter City', required=False)

    country = CountryField(default='IR').formfield(
        label='Country', blank_label='Select Country')

    room_type = forms.ModelChoiceField(
        empty_label='Any Type',
        queryset=RoomType.objects.all(),
        label='Room Type',
        required=False,)

    price = forms.IntegerField(label='Price', min_value=0, required=False)
    guest = forms.IntegerField(label='Guest', min_value=0, required=False)
    bed = forms.IntegerField(label='Bed', min_value=0, required=False)
    bath = forms.IntegerField(label='Bath', min_value=0, required=False)
    bedroom = forms.IntegerField(label='Bedroom', min_value=0, required=False)

    instant_book = forms.BooleanField(required=False, label='Instant Book')
    superhost = forms.BooleanField(required=False, label='Superhost')
    amentities = forms.ModelMultipleChoiceField(
        queryset=Amenity.objects.all(),
        required=False,
        label='Amenities',
        widget=forms.CheckboxSelectMultiple,)
    facilities = forms.ModelMultipleChoiceField(
        queryset=Facility.objects.all(),
        required=False,
        label='Facilities',
        widget=forms.CheckboxSelectMultiple,)
