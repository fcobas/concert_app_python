from django.db import models
from lugar import Lugar
from sector import Sector
from precio import Precio
from datetime import datetime

class Evento (models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    activo = models.BooleanField()
    categoria = models.ForeignKey('Categoria')
    lugar = models.ForeignKey('Lugar')
    precios=models.ManyToManyField('Sector', through = 'Precio')
    
    def __unicode__(self):
        return self.nombre
    
    def darDisponible(self):
        lugar = None
        sectores = None
        
        #E = Evento.objects.filter(id=self.id)
        precios = Precio.objects.filter(evento_id = self.id)
        lugar = self.lugar
        sectores = Sector.objects.filter(lugar_id = lugar)
        total = 0
        for P in precios:
            total += P.disponibles
            
        return total
    
    def darMensaje(self):
        total = 0
        disp = 0
        
        if self.fecha < datetime.today():
            return 4        
        
        precios = Precio.objects.filter(evento_id = self.id)
        
        for P in precios:
            disp = disp + P.disponibles
            total = total + P.sector.butacas
        
        if disp <= 0 : return 0
        elif disp >= (total*0.01) and disp <= (total*0.10): return 1
        elif disp >= (total*0.11) and disp <= (total*0.50): return 2
        elif disp >= (total*0.51): return 3
        else : return 4