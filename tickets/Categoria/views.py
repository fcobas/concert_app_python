from django.http import HttpResponse
from tickets.categoria import Categoria
from django.template import RequestContext
from obligatorio import settings

def info(request,id):
    from django.shortcuts import render_to_response
    msg = ''
    eventos = None
    categorias = None
    
    busqueda = request.POST.get('buscar')
    
    if busqueda: 
        categorias = Categoria.objects.filter(nombre__icontains = busqueda)
        return render_to_response('{0}/Categoria/templates/index.html'.format(settings.INSTALLED_APPS[6]),
                          {'categorias':categorias },
                              context_instance = RequestContext(request))
    elif id is not None:
        try:
            categoria = Categoria.objects.get(pk = id)
        except Categoria.DoesNotExist:
            msg = 'La Categoria con el id {0} no existe'.format(id)
        except Persona.MultipleObjectsReturned:
            msg = 'Se encontraron muchas categorias con el id {0}'.format(id)
        
        from tickets.evento import Evento
        eventos = Evento.objects.filter(categoria__pk = id)
        
        return render_to_response('{0}/Categoria/templates/eventos_categoria.html'.format(settings.INSTALLED_APPS[6]),
                              {'eventos':eventos,
                               'msg':msg },
                              context_instance = RequestContext(request))
    else:
        categorias = Categoria.objects.all()
        return render_to_response('{0}/Categoria/templates/index.html'.format(settings.INSTALLED_APPS[6]),
                              {'categorias':categorias },
                              context_instance = RequestContext(request))