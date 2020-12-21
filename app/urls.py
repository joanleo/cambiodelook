from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'app'
urlpatterns = [

    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('user', views.userPage, name='user_page'),

    path('account/<str:id>', views.accountSettings, name='account'),

    path('products', views.Products, name='products'),
    path('create_product', views.CreateProduct, name='create_product'),
    path('update_product/<str:pk>', views.UpdateProduct, name='update_product'),
    path('delete_product/<str:pk>', views.DeleteProduct, name='delete_product'),

    path('profesionals', views.Profesionals, name='profesionals'),
    path('profesional/<str:pk>', views.profesional, name='profesional'),
    path('create_profesional', views.CreateProfesional, name='create_profesional'),
    path('update_profesional/<str:pk>', views.UpdateProfesional, name='update_profesional'),
    path('delete_profesional/<str:pk>', views.DeleteProfesional, name='delete_profesional'),

    path('customers', views.Customers, name='customers'),
    path('customer/<str:pk>', views.customer, name='customer'),
    path('create_customer', views.CreateCustomer, name='create_customer'),
    path('update_customer/<str:pk>', views.UpdateCustomer, name='update_customer'),
    path('delete_customer/<str:pk>', views.DeleteCustomer, name='delete_customer'),

    path('create_order/<str:pk>', views.CreateOrder, name='create_order'),
    path('update_order/<str:pk>', views.UpdateOrder, name='update_order'),
    path('delete_order/<str:pk>', views.DeleteOrder, name='delete_order'),

    path('create_sale', views.CreateSale, name='create_sale'),


    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="app/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="app/password_reset_done.html"), 
        name="password_reset_complete"),
]