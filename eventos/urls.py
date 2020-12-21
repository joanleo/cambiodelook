from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'eventos'

urlpatterns = [
    path('calendar', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
	path('event/edit/<str:event_id>', views.event, name='event_edit'),

]