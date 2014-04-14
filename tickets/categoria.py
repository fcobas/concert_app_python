from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        db_table = 'tickets_categoria'
        managed = False
        ordering = ['id']
        unique_together = (('nombre',))
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
