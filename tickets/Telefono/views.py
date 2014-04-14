from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from obligatorio import settings
from tickets.telefono import Telefono
from tickets.pin import Pin
from tickets.rpc import retornarUsuariosRPC
from forms import TelForm
from forms import PinForm 
from tickets.precio import Precio

def solicitarTelefono(request,eventoId,precioId):
    msg = ''
    agotadas = ''
    precio = Precio.objects.get(pk=precioId)
    
    if precio.disponibles == 0:
        form = TelForm()
        agotadas = 'Agotadas!'
        msg = 'No hay mas localidades en este sector, por favor seleccione otro.'
        return render_to_response('{0}/Telefono/templates/telefono.html'.format(settings.INSTALLED_APPS[6]), 
                              {'form': form, 'agotadas':agotadas,'msg':msg }, context_instance = RequestContext(request))
        
    if request.method == 'POST':
        form = TelForm(request.POST)
        if form.is_valid():
            tel = form.cleaned_data.get('telefono')
            rpcDicc = retornarUsuariosRPC(tel)
            if rpcDicc:
                try:
                    aux = Telefono.objects.get(numero = tel)
                except Telefono.DoesNotExist:
                    telefono = Telefono()
                    telefono.numero = tel
                    telefono.save()
                    pin = Pin()
                    pin.telefono = telefono
                    pin.numero = pin.generarPin()
                    pin.save()
                else:
                    pin = Pin.objects.get(telefono_id = aux.id)
                    pin.telefono = aux
                    pin.numero = pin.generarPin()
                    pin.save()
                return HttpResponseRedirect('/telefono/pin/{0}/{1}/{2}/'.format(tel,eventoId,precioId))
            else:
                    msg = 'El telefono no se encuentra en la base de datos.'                
    else:
        form = TelForm()
    return render_to_response('{0}/Telefono/templates/telefono.html'.format(settings.INSTALLED_APPS[6]), 
                              {'form': form, 'msg':msg }, context_instance = RequestContext(request))


def solicitarPin(request, tel, eventoId, precioId):
    from tickets.ticket import Ticket
    
    msg = ''
    if request.method == 'POST':
        form = PinForm(request.POST)
        if form.is_valid():
            tel = form.cleaned_data.get('tel')
            pin = form.cleaned_data.get('pin')            
            try:
                pinEnc = Pin.objects.get(numero = pin)
                telEnc = Telefono.objects.get(numero = tel)
                if pinEnc.telefono == telEnc:
                    try:
                        precio = Precio.objects.get(pk = precioId)
                    except Precio.DoesNotExist:
                        msg = 'No existe ningun precio con ese Id.'
                    rpcDicc = retornarUsuariosRPC(telEnc.numero)
                    saldo = rpcDicc.get('saldo')
                    if int(saldo) > int(precio.valor):
                        ticket = Ticket()
                        ticket.telefono = Telefono.objects.get(numero = tel)
                        ticket.precio = precio
                        ticket.numero = 1
                        ticket.disponible = False
                        ticket.save()
                        return HttpResponseRedirect('/gracias/{0}/{1}'.format(ticket.id,rpcDicc.get('documento')))
                    else:
                        msg = 'Saldo insuficiente para realizar la compra.'
                else:
                    msg = 'No coincide el pin mandado con el telefono.'
            except Pin.DoesNotExist:
                return HttpResponse('Pin no existe')
            except Telefono.DoesNotExist:
                return HttpResponse('Telefono no existe')
            
    else:
        form = PinForm({'tel':tel})    
    return render_to_response('{0}/Telefono/templates/pin.html'.format(settings.INSTALLED_APPS[6]),
                              {'form': form,'msg':msg}, context_instance = RequestContext(request))
    
def gracias(request,ticketId,di):
    from tickets.ticket import Ticket
    msg = ''
    try:
        ticket = Ticket.objects.get(pk = ticketId)
    except Ticket.DoesNotExist:
        msg = 'No existe ticket con este id.'
    except Ticket.MultipleObjectsReturned:
            msg = 'Se encontraron muchos tickets con el id {0}'.format(ticketId)
    
    if ticket:
        return render_to_response('{0}/Telefono/templates/gracias.html'.format(settings.INSTALLED_APPS[6]),
                              {'ticket': ticket,'msg':msg,'di':di}, context_instance = RequestContext(request))