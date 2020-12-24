from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe

import datetime as dt

import calendar

from .models import *
from .utils import Calendar
from .forms import EventForm
from app.forms import *
from django.utils import timezone


class CalendarView(generic.ListView):
    model = Event
    template_name = 'eventos/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        events = Event.objects.all()
        cal = Calendar(events)
        html_cal = cal.formatmonth(d.year, d.month, withyear=True)
        html_cal = html_cal.replace('<td ', '<td  width="150" height="100"')
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return dt.date.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    hora = request.POST.get('inicio')
    #print((hora))

    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    
    
    form1 = OrderForm(request.POST)
    if request.POST and form.is_valid():
        """hora, minuto = hora.split(':')
        hora = int(hora)
        minuto = int(minuto)
        fin = dt.time(hour=hora+1, minute= minuto)
        print(fin)"""
        form1 = OrderForm({'customer':request.POST['cliente'], 'product':request.POST['product'], 'date_created':request.POST.get('date_created', timezone.now()), 'status':'Pending','profesional':request.POST['profesional'] })
        print(request.POST['product'])
        if form1.is_valid():
            form1.save()

        evento = form.save(commit=False)
        #evento.fin = fin
        evento.save()
        #print(form)
        return HttpResponseRedirect(reverse('eventos:calendar'))
    return render(request, 'eventos/event.html', {'form': form})