from django.db import models


class Telefono(models.Model):
    numero = models.CharField(max_length=9)
    
    def __unicode__(self):
        return self.numero
    