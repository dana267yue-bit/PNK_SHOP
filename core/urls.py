from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),   
    path('about/', views.about, name='about_page'),
    path('contact/', views.contact, name='contact_Page'),
    path('product/<int:id>/', views.product_details, name='product_details'),
]