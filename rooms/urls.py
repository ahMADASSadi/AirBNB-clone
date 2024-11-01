from django.urls import path
from . import views


app_name = 'rooms'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:id>/', views.RoomDetailView.as_view(), name='detail'),
    path('search/', views.search, name='search'),
]
