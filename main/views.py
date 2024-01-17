from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event
from .forms import VenueForm, EventForm

def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')


def search_event(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        events = Event.objects.filter(name__icontains=searched)
        return render(request, 'main/search_event.html',
                      {'searched':searched,
                       'events':events})
    else:
        return render(request, 'main/search_event.html',
                      {})

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/add_venue.html', {'form': form,
                                                   'submitted': submitted})

def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/add_event.html', {'form': form,
                                                   'submitted': submitted})


def all_events(request):
    event_list = Event.objects.all().order_by('event_date')
    return render(request, 'main/event_list.html',
        {'event_list': event_list})


def home(request, year = datetime.now().year, month = datetime.now().strftime('%B')):
    name = 'Maksym'
    surname = 'Salyha'
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # create calendar

    cal = HTMLCalendar().formatmonth(
        year,
        month_number)

    now = datetime.now()
    current_year = now.year

    time = now.strftime('%I:%M %p')
    return render(request, 'main/home.html', {
        "name": name,
        "surname": surname,
        "year": year,
        "month": month,
        'month_number': month_number,
        'cal': cal,
        'current_year': current_year,
        'time': time
    })