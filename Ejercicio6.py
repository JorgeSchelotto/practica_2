import os
from datetime import datetime

# Realizado con ayuda de http://python-para-impacientes.blogspot.com.ar/2015/09/explorando-directorios-con-listdir-walk.html


formato = '%d-%m-%y %H:%M:%S' # establece formato de fecha-hora
linea = '_'*685
# os.getcwd()obtiene ruta del script
listaNombres = os.listdir(os.getcwd()) # obtiene lista con archivos/dir
listaTotal = []
for elemento in listaNombres:
    # st_size: tamaño en bytes
    # st_atime: fecha-hora del último acceso (en segundos)
    # datetime.fromtimestamp(os.stat(elemento).st_atime)
    # Obtiene del estado fechas de último acceso/modificación
    # Como los valores de las fechas-horas vienen expresados
    # en segundos se convierten a tipo datetime.
    # Creo lista con nombre, tamaño, ultimo acceso.
    listaParcial = [elemento, str(os.stat(elemento).st_size / 1024)+' kb' , datetime.fromtimestamp(os.stat(elemento).st_atime).strftime(formato)]
    # Creo una lista de listas. cada lista interna tiene nombre, tamaño, ultimo acceso de los archivos.
    listaTotal.append(listaParcial)

print()
print()
print(linea)
print(linea)
print()
print('   ', listaTotal)
print()
print(linea)
print(linea)