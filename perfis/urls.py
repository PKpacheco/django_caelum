from django.conf.urls import include, url, patterns
from django.contrib import admin
from perfis import views

urlpatterns = patterns('',
    url (r'^$', views.index, name = 'index'),
    url (r'^perfis/(?P<perfil_id>\d+)$', views.exibir, name = 'exibir'),
    url (r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name = 'convidar'),
    url (r'^convite/(?P<convite_id>\d+)/aceitar$', views.aceitar, name = 'aceitar')
)

#\+ =  aceitar digitos na url
# ^ $ define inicio e final da string 