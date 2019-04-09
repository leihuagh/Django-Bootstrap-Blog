from django.urls import path
from home.views import index
from company.views import about, contact

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
]
