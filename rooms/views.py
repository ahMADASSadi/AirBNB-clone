from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import render
from django_countries import countries

from .forms import SearchForm
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


class SearchView(FormView):
    form_class = SearchForm
    template_name = 'rooms/search.html'
    paginate_by = 10  # Number of rooms per page

    def get_form(self, form_class=None):
        form_class = form_class or self.get_form_class()
        return form_class(self.request.GET)

    def get_queryset(self):
        queryset = Room.objects.all()
        form = self.get_form()

        if form.is_valid():
            # Retrieve form values and filter queryset as in your original code
            filters = {
                'city__icontains': form.cleaned_data.get('city'),
                'country': form.cleaned_data.get('country'),
                'price__lte': form.cleaned_data.get('price'),
                'room_type__id': form.cleaned_data.get('type'),
                'guests__gte': form.cleaned_data.get('guests'),
                'beds__gte': form.cleaned_data.get('beds'),
                'baths__gte': form.cleaned_data.get('baths'),
                'bedrooms__gte': form.cleaned_data.get('bedrooms'),
                'instant_book': form.cleaned_data.get('instant'),
                'host__superhost': form.cleaned_data.get('superhost'),
            }
            filters = {k: v for k, v in filters.items() if v is not None}
            queryset = queryset.filter(**filters)

            amenities = form.cleaned_data.get('amenities')
            facilities = form.cleaned_data.get('facilities')
            if amenities:
                queryset = queryset.filter(amenities__in=amenities)
            if facilities:
                queryset = queryset.filter(facilities__in=facilities)

            queryset = queryset.distinct()

        return queryset

    def paginate_queryset(self, queryset, page_size):
        paginator = Paginator(queryset, page_size)
        page = self.request.GET.get('page')

        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)

        return paginated_queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        queryset = self.get_queryset()
        paginated_rooms = self.paginate_queryset(queryset, self.paginate_by)

        context['rooms'] = paginated_rooms
        context['is_paginated'] = paginated_rooms.has_other_pages()
        return context
