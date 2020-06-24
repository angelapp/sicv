from django.conf.urls import *
from web import views

urlpatterns = [
    url(r'^$',views.programas.as_view(), name = 'programas'),
    url(r'^iniciar-sesion/',views.iniciar_sesion.as_view(), name = 'iniciar_sesion'),
    url(r'^contactenos/',views.contactenos.as_view(), name = 'contactenos'),
    url(r'^detalle-programa/(?P<id>\d+)/$',views.detalle_programa.as_view(), name = 'detalle_programa'),
    url(r'^inscribir/(?P<id_programa>\d+)/(?P<id_curso>\d+)/$',views.inscribir.as_view(), name = 'inscribir'),
    url(r'^cerrar-sesion/',views.cerrar_sesion.as_view(), name = 'cerrar_sesion'),
    
]
