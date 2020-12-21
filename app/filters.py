import django_filters
from django_filters import DateFilter

from django.template.defaulttags import register

from .models import *

class OrderFilter(django_filters.FilterSet):
    #start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    #end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)