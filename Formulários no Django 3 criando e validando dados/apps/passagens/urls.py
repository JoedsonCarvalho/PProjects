from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('minha_consulta', revisao_consulta, name='consulta_minha')
]