from django.urls import path
from .views import bbc, Index

urlpatterns = [
    path('', Index, name='Index'),
    path('bbc', bbc, name='BBC')


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]