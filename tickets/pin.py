from django.db import models

class Pin(models.Model):
    numero = models.IntegerField()
    telefono = models.ForeignKey('Telefono')
    
    def generarPin(self):
        import random
        return random.randrange(1000,9999)