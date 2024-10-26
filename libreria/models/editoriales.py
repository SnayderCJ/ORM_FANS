from django.db import models
from django_cte import CTEManager


class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f'Editorial: {self.nombre}' # Lo agregue para que se vea mas bonito en la consola

    class Meta:
        managed = True
        db_table = 'libreria_editorial'

    objects = CTEManager()