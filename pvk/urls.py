from django.urls import path
from django.views.generic import TemplateView

from pvk import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('artwork/', views.artwork, name='artwork'),
    path('artwork/(?P<filter>\d+)/', views.artwork_filter, name='artwork_filter'),
    path('add_inquiry/', views.add_inquiry, name='add_inquiry'),
    path('add_session/', views.add_session, name='add_session'),
    path('get_in_touch/', views.get_in_touch, name='get_in_touch'),
    path('get_product_image/', views.get_product_image, name='get_product_image'),
]