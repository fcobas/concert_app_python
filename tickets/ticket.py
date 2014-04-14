from django.db import models


class Ticket(models.Model):
    telefono = models.ForeignKey('Telefono')
    precio = models.ForeignKey('Precio')
    numero = models.IntegerField()
    disponible = models.BooleanField()
    
    def __unicode__(self):
        string = '{0} - {1} ${2}'.format(self.id,self.telefono.numero,self.precio.valor) 
        return string
    