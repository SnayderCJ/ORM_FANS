from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=70)

    def _str_(self):
        return f'Yo soy {self.nombre}'

class Libro(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    titulo = models.CharField(max_length=70, blank=True)
    paginas = models.PositiveIntegerField()
    fecha_publicacion = models.DateField(null=True)
    imagen = models.URLField(max_length=85, null=True)
    desc_corta = models.CharField(max_length=2000)
    estatus = models.CharField(max_length=1)
    categoria = models.CharField(max_length=50)
    editorial = models.ForeignKey('Editorial', on_delete=models.PROTECT, null=True)
    edicion_anterior = models.ForeignKey('self', null=True, blank=True, default=None, on_delete=models.PROTECT)

    class Meta:
        constraints = [
            models.CheckConstraint(check=~models.Q(titulo='cobol'), name='titulo_no_permitido_chk')
        ]

    def clean(self):
        if self.edicion_anterior and self.edicion_anterior == self:
            raise ValidationError("Un libro no puede ser su propia edición anterior.")
        # Evita ciclos de ediciones anteriores
        edicion = self.edicion_anterior
        while edicion:
            if edicion == self:
                raise ValidationError("No se puede crear un ciclo en las ediciones anteriores.")
            edicion = edicion.edicion_anterior

    def save(self, *args, **kwargs):
        self.clean()  # Llama a la validación antes de guardar
        super().save(*args, **kwargs)
        
class AutorCapitulo(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True)
    numero_capitulos = models.IntegerField(default=0)
    
class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'libreria_editorial'
        
class Libroautores(models.Model):
    isbn = models.CharField(max_length=13, blank=True, null=True)
    titulo = models.CharField(max_length=70, blank=True, null=True)
    autores = models.TextField(db_column='Autores', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'v_libroautores'
        
class LibroCronica(models.Model):
    descripcion_larga = models.TextField(null=True)
    libro = models.OneToOneField(Libro, on_delete=models.CASCADE, primary_key=True)