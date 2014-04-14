from django.db import models

    
class Precio(models.Model):
    sector=models.ForeignKey('Sector')
    evento = models.ForeignKey('Evento')
    valor = models.DecimalField(max_digits = 6, decimal_places =2)
    tickets=models.ManyToManyField('Telefono', through = 'Ticket')
    disponibles = models.IntegerField()
    
    def __unicode__(self):
        string = '{0} - {1} - ${2}'.format(self.evento.nombre,self.sector.nombre,self.valor)
        return string