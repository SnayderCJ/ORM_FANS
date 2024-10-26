from django.db import models
from django_cte import CTEManager


class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'libreria_editorial'

    objects = CTEManager()