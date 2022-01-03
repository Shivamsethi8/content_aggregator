from django.urls import path
from .views import bbc, Index

urlpatterns = [
    path('', Index, name='Index'),
    path('bbc', bbc, name='BBC')

]