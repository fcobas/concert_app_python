from django.db import models

class Lugar (models.Model):
    nombre = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        db_table = 'tickets_lugar'
        managed = False
        unique_together = (('nombre'),)
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'
        