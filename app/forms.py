from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['date_created']

class ProfesionalForm(ModelForm):
    class Meta:
        model = Profesional
        fields = '__all__'
        exclude = ['user']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'date_created']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['user', 'date_created']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Saleform(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['customers'].widget.attrs['autofocus'] = True
        self.fields['customers'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['customers'].widget.attrs['style'] = 'width: 70%'

        print(self.fields)

        self.fields['iva'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['iva'].widget.attrs['readonly'] = True

        self.fields['subtotal'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['subtotal'].widget.attrs['readonly'] = True

        self.fields['total'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['total'].widget.attrs['readonly'] = True

    class Meta:
        model = Sale
        fields = '__all__'

    
    customers = forms.ModelChoiceField(queryset=Customer.objects.all(), empty_label="")
    date_created = forms.DateTimeField()
    subtotal = models.DecimalField()
    iva = models.DecimalField()
    total = models.DecimalField()
    
    

