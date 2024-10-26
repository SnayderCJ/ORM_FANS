from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(AutorCapitulo)
admin.site.register(Editorial)
admin.site.register(LibroCronica)
admin.site.register(VLibroautores)