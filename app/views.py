from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.forms import inlineformset_factory, Form
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.db.models import Sum


from django.contrib import messages

from .models import *
from .forms import *
from .filters import *
from .decorators import *


# Create your views here.
@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Cuenta creada para '+username)
            return redirect('app:login')

    context = {'form': form}
    return render(request, 'app/register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('app:home')
        else:
            messages.info(request, 'Username o Password incorrectos')

    context = {}
    return render(request, 'app/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('app:login')

@login_required(login_url='app:login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    finished = orders.filter(status='Finished').count()
    pending = orders.filter(status='Pending').count()
    orders = orders.filter().order_by('-date_created')[:5]
    context = {'orders': orders,
               'customers': customers,
               'total_customers': total_customers,
               'total_orders': total_orders,
               'finished': finished,
               'pending': pending
               }

    return render(request, 'app/dashboard.html', context)

@login_required(login_url='app:login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()

    total_orders = orders.count()
    finished = orders.filter(status='Finished').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders,
               'total_orders': total_orders,
               'finished': finished,
               'pending': pending
               }
    return render(request, 'app/user.html', context)

@login_required(login_url='app:login')
@allowed_users(allowed_roles=['admin'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'app/account_settings.html', context)

@login_required(login_url='app:login')
@allowed_users(allowed_roles=['admin'])
def Products(request):
    products = Product.objects.all()
    return render(request, 'app/products.html', {'products': products})

def CreateProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    
    return render(request, 'app/product_form.html', context)


def UpdateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form =  ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    #print(context)
    
    return render(request, 'app/product_form.html', context)


def DeleteProduct(request, pk):

    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/')

    context = {'item': product}
    
    return render(request, 'app/delete_product.html', context)


def Profesionals(request):
    profesionals = Profesional.objects.all()
    return render(request, 'app/profesionals.html', {'profesionals': profesionals})
    

def profesional(request, pk):

    profesional = Profesional.objects.get(id=pk)

    orders = profesional.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'profesional': profesional,
               'orders': orders,
               'order_count': order_count,
               'myFilter': myFilter}
    return render(request, 'app/profesional.html', context)

def CreateProfesional(request):
    form = ProfesionalForm()

    if request.method == 'POST':
        form= ProfesionalForm(request.POST)
        form = ProfesionalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    
    return render(request, 'app/profesional_form.html', context)


def UpdateProfesional(request, pk):
    profesional = Profesional.objects.get(id=pk)
    #print(profesional.profile_pic.url)
    form = ProfesionalForm(instance=profesional)

    if request.method == 'POST':
        form =  ProfesionalForm(request.POST, instance=profesional)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form,
               'profesional':profesional}
    #print(context)
    
    return render(request, 'app/profesional_form.html', context)


def DeleteProfesional(request, pk):
    profesional = Profesional.objects.get(id=pk)
    if request.method == 'POST':
        profesional.delete()
        return redirect('/')

    context = {'item': profesional}
    
    return render(request, 'app/delete_profesional.html', context)


@login_required(login_url='app:login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer,
               'orders': orders,
               'order_count': order_count,
               'myFilter': myFilter}
    return render(request, 'app/customer.html', context)


def Customers(request):
    customers = Customer.objects.all()
    return render(request, 'app/customers.html', {'customers': customers})


def CreateCustomer(request):
    form = CustomerForm()

    if request.method == 'POST':
        form= CustomerForm(request.POST)
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    
    return render(request, 'app/customer_form.html', context)

def UpdateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    #print(customer.profile_pic.url)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form =  CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form,
               'customer':customer}
    #print(context)
    
    return render(request, 'app/customer_form.html', context)

def DeleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')

    context = {'item': customer}
    
    return render(request, 'app/delete_customer.html', context)



@login_required(login_url='app:login')
@allowed_users(allowed_roles=['admin'])
def CreateOrder(request, pk):

    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status', 'profesional'), extra=4)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset= Order.objects.none() ,instance=customer)
    #form = OrderForm(initial={'customer':customer})

    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    
    return render(request, 'app/order_form.html', context)

@login_required(login_url='app:login')
@allowed_users(allowed_roles=['admin'])
def UpdateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form =  OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    #print(context)
    
    return render(request, 'app/edit_order.html', context)

@login_required(login_url='app:login')
@allowed_users(allowed_roles=['admin'])
def DeleteOrder(request, pk):

    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    
    return render(request, 'app/delete_order.html', context)

"""class custoForm(forms.ModelForm):
    customers = forms.ModelChoiceField(queryset=Customer.objects.all().order_by('name'))

class ordeForm(forms.ModelForm):
    orders = forms.ModelChoiceField(queryset=Order.objects.all().order_by('id'))"""

def CreateSale(request):

    """customerForm = custoForm(request.Post)
    orders = ordeForm(request.Post)
    subtotal = orders.aggregate(Sum('product__price'))
    iva = 19
    total_iva = subtotal['product__price__sum'] * (iva/100)
    total = subtotal['product__price__sum'] + total_iva"""
    
    form = Saleform()
    #print(form)
    if request.method == 'POST':
        form = Saleform(request.POST)
        #print(form)
        #customerForm = custoForm(request.POST['customer'])
        #print(form)
        if form.is_valid:
            form.save()
            redirect('/')
    else:
        print("No es post")
    context = {
        'form': form,        
    }

    return render(request, 'app/create_sale1.html', context)


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Product.objects.filter(name__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    # item['value'] = i.name
                    item['text'] = i.name
                    data.append(item)
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    

