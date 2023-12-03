from django.urls import path
from . import views

urlpatterns = [
    path('', views.js2, name='home'),
    path('ritzyall', views.ritzyall, name='home'),
    path('ritzypro', views.ritzypro, name='home'),
    path('ritzychifon', views.ritzychifon, name='home'),
    path('ritzywoven', views.ritzywoven, name='home'),
    path('ritzylycra', views.ritzylycra, name='home'),
    path('ritzylinen', views.ritzylinen, name='home'),
    path('sale', views.sale, name='home'),
    path('contact', views.contact, name='home'),
    path('check', views.check, name='home'),
    path('ourstory', views.ourstory, name='home')
        ]
