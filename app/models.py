from django.db import models
from django.contrib.auth.models import User
from  django.utils import timezone
import datetime


# Create your models here.

class Profesional(models.Model):
    SEXO = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Otrher')
    ]
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200,null=True)
    birthday = models.DateField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile_pic.png", null=True, blank=True)
    date_created = models.DateTimeField( default=timezone.now)

    sexo = models.CharField(max_length=200, choices=SEXO, null=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dic(self)
        item['phone'] = self.phone
        item['email'] = self.email
        item['sexo'] = {'id': self.sexo, 'name': self.get_sexo_display()}

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'

class Customer(models.Model):

    SEXO = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Otrher')
    ]
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    birthday = models.DateField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile_pic.png", null=True, blank=True)
    date_created = models.DateTimeField( default=timezone.now)

    sexo = models.CharField(max_length=200, choices=SEXO, null=True)

    def __str__(self):
        return self.name
    
    def toJSON(self):
        item = model_to_dic(self)
        item['phone'] = self.phone
        item['email'] = self.email
        item['sexo'] = {'id': self.sexo, 'name': self.get_sexo_display()}

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Product(models.Model):

    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField()
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dic(self)
        item['price'] = self.price
        item['category'] = self.category.toJSON()
        item['description'] = self.description 

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Order(models.Model):

    STATUS = [
        ('Pending', 'Pending'),
        ('Finished', 'Finished')
    ]
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField( default=timezone.now, null=True, blank=True)
    status = models.CharField(max_length=200, choices=STATUS, default='Pending', null=True)
    profesional = models.ForeignKey(Profesional, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

    def toJSON(self):
        item = model_to_dic(self)
        item['customer'] = self.customer.toJSON()
        item['product'] = self.product.toJSON()
        item['date_created'] = self.date_created.strftime('%Y-%m-%d')
        item['status'] = {'id': self.status, 'name': self.get_status_display()}
        item['profesional'] = self.profesional.toJSON()

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_created = models.DateTimeField( default=timezone.now, null=True, blank=True)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.customer.name

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

class DetailSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Detalle de venta'
        verbose_name_plural = 'Detalle de ventas'