from libreria.models import *

# Comando para ejecutar el shell de Orm de Django
# python manage.py shell_plus -–print-sql



# Consultar todos los registros de la tabla Autor
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

