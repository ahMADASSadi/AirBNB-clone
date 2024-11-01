from django.views.generic import TemplateView
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from .models import Amenity, Facility, Room, RoomType


class HomeView(ListView):
    model = Room
    # template_name = 'rooms/home.html'
    paginate_by = 10
    ordering = '-created'
    page_kwarg = 'page'
    paginate_orphans = 5


class RoomDetailView(DetailView):
    model = Room
    pk_url_kwarg = "id"
    template_name = 'rooms/details.html'


def search(request):

    room_types = RoomType.objects.all()
    city = str(request.GET.get('city')).capitalize()
    country = request.GET.get('country')
    price = int(request.GET.get('price', 0))
    room_type = int(request.GET.get('type', 0))
    guests = int(request.GET.get('guests', 0))
    beds = int(request.GET.get('beds', 0))
    baths = int(request.GET.get('baths', 0))
    bedrooms = int(request.GET.get('price', 0))
    selected_amenities = request.GET.getlist('amenities')
    selected_facilities = request.GET.getlist('facilities')
    amenities = Amenity.objects.all()
    facilities = Facility.objects.all()
    instant = request.GET.get('instant', False)
    superhost = request.GET.get('superhost', False)

    form = {'city': city, 'selected_room_types': room_type, 'selected_country': country,
            "price": price,
            "beds": beds,
            "baths": baths,
            "bedrooms": bedrooms, "guests": guests,
            "selected_amenities": selected_amenities,
            "selected_facilities": selected_facilities,
            "instant": instant,
            "superhost": superhost,
            }

    choices = {
        'countries': countries, 'room_types': room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    # Apply search filters
    query = Q()
    if city:
        query &= Q(city__icontains=city)
    if country:
        query &= Q(country=country)
    if price > 0:
        query &= Q(price__lte=price)
    if room_type > 0:
        query &= Q(room_type__id=room_type)
    if guests > 0:
        query &= Q(guests__gte=guests)
    if beds > 0:
        query &= Q(bed__gte=beds)
    if baths > 0:
        query &= Q(bath__gte=baths)
    if bedrooms > 0:
        query &= Q(bedroom__gte=bedrooms)
    if selected_amenities:
        query &= Q(amenities__pk__in=selected_amenities)
    if selected_facilities:
        query &= Q(facilities__pk__in=selected_facilities)
    if instant:
        query &= Q(instant_book=True)
    if superhost:
        query &= Q(host__superhost=True)

    # Filter rooms and prefetch related models
    rooms = Room.objects.filter(query).select_related(
        'room_type').prefetch_related('room_amenity', 'room_facility')

    return render(request, 'rooms/search.html', {**form, **choices, 'rooms': rooms})


# class SearchView(TemplateView):
#     template_name = "rooms/search.html"

#     def get_search_params(self):
#         """Extract search parameters from request."""
#         return {
#             'city': str(self.request.GET.get('city', '')).capitalize(),
#             'country': self.request.GET.get('country'),
#             'price': int(self.request.GET.get('price', 0)),
#             'room_type': int(self.request.GET.get('type', 0)),
#             'guests': int(self.request.GET.get('guests', 0)),
#             'beds': int(self.request.GET.get('beds', 0)),
#             'baths': int(self.request.GET.get('baths', 0)),
#             'bedrooms': int(self.request.GET.get('bedrooms', 0)),
#             'selected_amenities': self.request.GET.getlist('amenities'),
#             'selected_facilities': self.request.GET.getlist('facilities'),
#             'instant': self.request.GET.get('instant', '') == 'on',
#             'superhost': self.request.GET.get('superhost', '') == 'on'
#         }

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # Retrieve data from models
#         room_types = RoomType.objects.all()
#         amenities = Amenity.objects.all()
#         facilities = Facility.objects.all()

#         # Search parameters
#         search_params = self.get_search_params()

#         # Update context for the form and filters
#         context.update({
#             'form': search_params,
#             'countries': countries,  # Define `countries` as per your project requirements
#             'room_types': room_types,
#             'amenities': amenities,
#             'facilities': facilities,
#         })

#         return context

#     def get(self, request, *args, **kwargs):
#         # Prepare context data and render
#         context = self.get_context_data()
#         return self.render_to_response(context)
