# coding: utf-8

# 2. Usando el diccionario del Ejercicio 1, acceder a las coordenadas y, según el color asociado,
# ejecute una función, donde las funciones planteen la resolución de ejercicios simples como
# ser:(a) Suma de dos números que se generen en forma aleatoria cada vez que se llama a la
# función, reciba el resultado por teclado y verifique el resultado.
# (b) Dada la estructura que contiene palabras clasificadas según su acentuación:
# palabras = [('grave',['molesto']), ('aguda',['ratón']),
# ('esdrujula',['murciélago'])]
# cada vez que se ejecuta la función elija una palabra en forma aleatoria, consulte al
# usuario sobre el tipo que es por su acentuación y verifique la respuesta.

import random
from Ejercicio1_2 import coordenadas 

def azul():
	return random.randrange(1000) - random.randrange(2000)
	
def amarillo(x, y):
	return ((x + y) * 3,14)

def rojo():
	return ('esto es un string')
	
def blanco():
	return ('n' * 4)
	
def negro(x, y):
	return ((x - y) / y**3)	
	
dic = coordenadas()

print('Ingrese alguna de las siguientes coordenadas: (2,3),(5,6),(8,8),(10,2),(-5,-8)')	
	
e1 = int(input())
e2 = int(input())

tupCoor = (e1, e2)

funciones = {'azul' : azul(), 'amarillo': amarillo(e1, e2), 'rojo': rojo(), 'blanco': blanco(), 'negro': negro(e1, e2)}

print(funciones[dic[tupCoor]])
