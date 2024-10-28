from libreria.models import *

# Comando para ejecutar el shell de Orm de Django
# python manage.py shell_plus -–print-sql



Consultar todos los registros de la tabla Autor
Autor.objects.all() 
# Obtener un unico registro de la tabla Autor
Autor.objects.get(id=1)
# Obtener solo el primer resultado
Libro.objects.all().first()
# Obtener solo el ultimo resultado
Libro.objects.all().last()
# Obtener los primeros N resultados
Libro.objects.all()[:5]  # Los primeros 5 resultados

# Consultar coincidencias por el inicio
Libro.objects.filter(isbn__startswith="16")

''' Consultas por mayor que Ejemplo de los libros que tienen mas de 200 paginas '''
Libro.objects.filter(paginas__gt=200)

# Ejemplo de libros que tienen mas de 200 paginas pero cuyo isbn no sea ninguno de estos dos
# ('1933988592','1884777600')
Libro.objects.filter(paginas__gt=200).exclude(isbn__in=('1933988592','1884777600'))

# Consultas por mayor o igual que
Libro.objects.filter(paginas__gte=200)


# FILA 2
# 1. Crea 5 autores y relaciónalos con el libro “Ciencia para Todos” usando bulk_create.

autores = Autor.objects.bulk_create([
    Autor(nombre="Juan"),
    Autor(nombre="Pedro"),
    Autor(nombre="Luis"),
    Autor(nombre="Carlos"),
    Autor(nombre="Jorge")
])

libro = Libro.objects.get(titulo="Ciencia para Todos")
for autor in autores:
    autor.libros.add(libro)
    autor.save()

# 2. Encuentra todos los autores cuyos nombres contengan la letra "e" y que hayan escrito un libro en la categoría "Educación".
autores_educacion = Autor.objects.filter(nombre__icontains="e", libros__categoria__nombre="Educación").distinct()

# 3. Busca libros publicados entre los años 2018 y 2022, con más de 300 páginas, y que no pertenezcan a la categoría "Historia".

Libro.objects.filter(fecha_publicacion__year__range=(2018, 2022), paginas__gt=300).exclude(categoria__nombre="Historia")

# 4. Dado el libro “Cuentos Cortos”, muestra todos sus autores.

Libro.objects.get(titulo="Cuentos Cortos").autores.all()

# 5. Decrementa el número de páginas en 25 para todos los libros con más de 200 páginas y cuyo autor sea “Luis”.

libros = Libro.objects.filter(paginas__gt=200, autores__nombre="Luis").update()


