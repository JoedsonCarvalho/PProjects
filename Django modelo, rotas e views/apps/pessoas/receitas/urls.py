from xml.etree.ElementInclude import include
from django.urls import URLPattern
from django.urls import path

from . import views
urlpatterns = [

    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
    path('buscar', views.buscar, name='buscar'),
]