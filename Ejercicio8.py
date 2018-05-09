from collections import Counter

def cuentapalabras(str):
	count = Counter(frase.split(' ')).most_common()
	for key in range(3):
		print(count[key][0])

frase = "Si trabajás mucho con computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. \n" \
		"Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número de archivos de texto, o renombrar \n" \
        " y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de \n " \
        "datos personalizada, o una aplicación especializada con interfaz gráfica, o un juego simple."

cuentapalabras(frase)
