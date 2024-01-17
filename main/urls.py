from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<int:year>/<str:month>/', views.home, name = 'home'),
    path('events', views.all_events, name ="list-events"),
    path('add_venue', views.add_venue, name ='add-venue'),
    path('search_event', views.search_event, name='search-event'),
    path('add_event', views.add_event, name='add-event'),
    path('delete-event/<event_id>/', views.delete_event, name='delete-event'),

]
