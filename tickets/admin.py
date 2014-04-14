from django.contrib import admin

from categoria import Categoria
from evento import Evento
from lugar import Lugar
from precio import Precio
from sector import Sector
from telefono import Telefono
from ticket import Ticket


admin.site.register(Categoria)
admin.site.register(Evento)
admin.site.register(Lugar)
admin.site.register(Precio)
admin.site.register(Sector)
admin.site.register(Telefono)
admin.site.register(Ticket)

