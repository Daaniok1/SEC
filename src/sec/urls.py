from django.conf.urls import url, include
from sec.views import *


urlpatterns = [
    url(r'^principal/$', principal, name='principal'),
    url(r'^principal/addpregunta/$', add_pregunta, name='add_pregunta'),
]
