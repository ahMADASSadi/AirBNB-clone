from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Room


def all_rooms(request):
    # Get the page number from the request, defaulting to 1
    page_number = request.GET.get('page', 1)
    page_number = int(page_number)

    # Use Django's Paginator to handle pagination
    rooms = Room.objects.all()
    paginator = Paginator(rooms, 10)  # 10 rooms per page

    # Get the requested page, defaulting to the first page
    rooms_page = paginator.get_page(page_number)

    page_range = range(1, rooms_page.paginator.num_pages + 1)

    return render(request, 'rooms/home.html', {
        'rooms': rooms_page,
        'page': rooms_page.number,
        'page_count': paginator.num_pages,
        'page_range': page_range,
    })
