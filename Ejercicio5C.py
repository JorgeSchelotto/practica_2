# 5. Utilizando el módulo pattern.es defina una función denominada verbosInfinitivos que
# reciba un string, el cual puede contener varias oraciones y devuelva una lista de los verbos
# en infinitivo.

from pattern.es import conjugate, parse, INFINITIVE

def verbosInfinitivos (txt):
	"""Recibe un string. Devuelve una lista de sus verbos en infinitivo."""

	print()
	print('análisis hecho por pattern: ')
	lista_general = parse(txt).split()[0]
	print (lista_general)
	
	lista_verbos = ['VB', 'VBP', 'VBZ', 'VBG', 'VBD', 'VBN']
	verbos = list(filter(lambda verbo: verbo[1] in lista_verbos, lista_general))
	
	print()
	print('los verbos de la oración son: ')
	print(verbos)	
	
	verbos_infinitivo = []
	for v in verbos:
		if v[1] in lista_verbos:
			verbos_infinitivo.append(conjugate(v[0], INFINITIVE))
	print()
	print('los verbos pasados a infinitivo son: ')			
	return verbos_infinitivo

texto = 'perro, corre. gato muerde. peces: saltan. clientes: mueren.'
texto = texto.lower().strip().replace('.', '').replace(';', '').replace(':', ' ').replace(',', ' ').replace('/n', ' ')
print('Párrafo inicial: ')
print(texto)
print (verbosInfinitivos(texto))



