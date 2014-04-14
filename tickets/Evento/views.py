from django.shortcuts import render_to_response
from tickets.evento import Evento
from obligatorio import settings
from django.template import RequestContext
from tickets.precio import Precio

def info(request,id):
    msg = ''
    evento = None
    if id:
        try:
            evento = Evento.objects.get(pk = id)
            try:
                precios = Precio.objects.filter(evento_id = evento.id)
            except Precio.DoesNotExist:
                msg = 'No hay precios disponibles.'
        except Evento.DoesNotExist:
            msg = 'El evento con el id {0} no existe'.format(id)
        except Evento.MultipleObjectsReturned:
            msg = 'Se encontraron muchos eventos con el id {0}'.format(id)
        return render_to_response('{0}/Evento/templates/detalle.html'.format(settings.INSTALLED_APPS[6]),
                          {'evento':evento,'precios':precios , 'msg':msg},
                              context_instance = RequestContext(request))
    else:
        msg = 'Ingrese un codigo de evento en la URL'
        return render_to_response('{0}/Evento/templates/detalle.html'.format(settings.INSTALLED_APPS[6]),
                          {'msg':msg},
                              context_instance = RequestContext(request)) 