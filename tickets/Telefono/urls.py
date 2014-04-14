from django.conf.urls import patterns, include, url

urlpatterns = patterns('tickets.Telefono.views',
                       url(r'^(?P<eventoId>\d+)?/(?P<precioId>\d+)?/?$','solicitarTelefono'),
                       url(r'^pin/(?P<tel>\d+)?/(?P<eventoId>\d+)?/(?P<precioId>\d+)?/?$', 'solicitarPin'),
                       )