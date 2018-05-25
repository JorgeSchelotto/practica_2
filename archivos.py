#!/usr/bin/env python3
import os


# Crear dentro del archivo "archivos.py" la funcion leer_archivos() que genere un diccionario en donde cada clave corresponda al nombre de un subdirectorio de "imagenes", y su valor sea una lista con los nombres de los archivos. 
#Por ejemplo, para la siguiente estructura de directorios:

#./imagenes/dir06/Excepcion5.png
#./imagenes/dir06/Excepcion9.png
#./imagenes/dir07/Excepcion6.png
#./imagenes/dir02/school.jpg

#Devuelva el siguiente diccionario:

#{'dir06': ['Excepcion5.png', 'Excepcion9.png'], 'dir07': ['Excepcion6.png'], 'dir02': ['school.jpg']}

def leer_archivos(path):
    """Modulo que recibe una ruta y devuelve un diccionario cuya claves serán sus subdirectorios, y el valor por cada clave será
    una lista con los archivos que se encuentran en dichos subdirectorios"""
    diccio = {}
    for ruta, dir, archivos in os.walk(path, topdown=False):
        if os.path.split(ruta)[1] != os.path.split(path)[1]:
            ruta2 = os.path.split(ruta)[1]
            diccio[ruta2] = archivos

    return diccio




#En la variable path debe ingresarse la ruta de la carpeta a leer o la funcion os.getcwd()
path= 'C:/Users\Mozquito\Desktop\imagenes'
print(leer_archivos(path))