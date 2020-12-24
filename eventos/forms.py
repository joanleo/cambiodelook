from django.forms import ModelForm, DateInput, TimeInput
from .models import Event

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'day': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
      'inicio': TimeInput(attrs={'type': 'time'}, format='%H:%M'),
      #'fin': TimeInput(attrs={'type': 'time'}, format='%H:%M'),
    }
    fields = '__all__'
    exclude= ['status', 'date_created', 'fin']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['day'].input_formats = ('%Y-%m-%d',)
    self.fields['inicio'].input_formats = ('%H:%M',)
   # self.fields['fin'].input_formats = ('%H:%M',)