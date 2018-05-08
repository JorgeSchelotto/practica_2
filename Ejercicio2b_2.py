# coding: utf-8

# 2.b. dada la estructura que contiene palabras clasificadas según su acentuación: 
# palabras = [('grave',['molesto']), ('aguda',['ratón']), # ('esdrujula',['murciélago'])]
# cada vez que se ejecuta la función elija una palabra en forma aleatoria, consulte al
# usuario sobre el tipo que es por su acentuación y verifique la respuesta.

import random
palabras = [('grave',['molesto']), ('aguda',['ratón']), ('esdrujula',['murciélago'])]

# si ingreso 1 entra en la función, respondo la pregunta y no informa nada.
# me parece que hay algo de los if y else que se me está pasando.
def acentos():
	num = random.randrange(2)
	
	if (num == 0):
		respuesta = (palabras[0][0])
		print('¿La palabra ',palabras[num][1],' es grave, aguda o esdrújula?')
		r = input()
		if (respuesta != r):
			resultado = 'Ud. Falló'
		else:
			resultado = 'Ud. sí que sabe'
			
	elif (num == 1):
		respuesta = palabras[1][0]
		print('¿La palabra ',palabras[num][1],' es grave, aguda o esdrújula?')
		r = input()
		if (respuesta != r):
			resultado = 'Ud. Falló'
		else:
			resultado = 'Ud. sí que sabe'

	else:
		respuesta = palabras[2][0]
		print('¿La palabra ',palabras[num][1],' es grave, aguda o esdrújula?')
		r = input()
		if (respuesta != r):
			resultado = 'Ud. Falló'
		else:
			resultado = 'Ud. sí que sabe'

	return (resultado)
	
print ('Veamos cuánto sabe sobre acentuación. Si quiere jugar, ingrese 1. ')
x = input()
if x != 2:
	acentos()
	
# no logro que me imprima este else si ingreso 2	
else:
	print('Es Ud. un amargo')
