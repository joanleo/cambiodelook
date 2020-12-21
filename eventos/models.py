from django.db import models

from django.core.validators import ValidationError

import datetime
from django.urls import reverse

from app.models import Product, Profesional, Customer
from  django.utils import timezone
import datetime



class Event(models.Model):

    STATUS = [
        ('Pending', 'Pending'),
        ('Finished', 'Finished')
    ]
    status = models.CharField(max_length=200, choices=STATUS, default='Pending', null=True)
    profesional = models.ForeignKey(Profesional, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    day = models.DateField()
    cliente = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    inicio = models.TimeField(datetime.time(), null=True)
    fin = models.TimeField(editable=False, null=True)
    date_created = models.DateTimeField( default=timezone.now, null=True)

    def save(self, *args, **kwargs):

        horas = (str(self.inicio))
        hora, minuto, _ = horas.split(':')
        hora = int(hora)
        minuto = int(minuto)
        fin = datetime.time(hour=hora+1, minute= minuto)
        print(fin)
        super(Event, self).save(*args, **kwargs)
        

    def __str__(self):
        return '{}'.format(self.cliente)

    @property
    def get_html_url(self):
        url = reverse('eventos:event_edit', args=[(self.id)])
        #producto = self.product.objects.all()
        #print(producto)
        return f'<a href="{url}">{self.cliente} {self.inicio} {self.profesional}</a>'


    """def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True

        return overlap


    def clean(self):
        if self.fin == self.inicio and self.fin  self.inicio:
            raise ValidationError('Ending hour must be after the starting hour')

        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.inicio, event.fin, self.inicio, self.fin):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.inicio) + '-' + str(event.fin))"""