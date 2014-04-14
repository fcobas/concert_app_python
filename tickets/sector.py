from django.db import models


class Sector(models.Model):
    nombre = models.CharField(max_length=50)
    lugar = models.ForeignKey('Lugar')
    butacas = models.IntegerField()
    
    def __unicode__(self):
        string = '{0} - {1}'.format(self.lugar.nombre,self.nombre)
        return string
    
    class Meta:
        db_table = 'tickets_sector'
        managed = False
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'