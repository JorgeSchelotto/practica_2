from pattern.es import tag
from pattern.es import conjugate, INFINITIVE

def verbosInfinitivos (str):
    verbos=[]
    for word, pos in tag(str): #tag devuelve una lista de tuplas formadas por (palabra, tipo de palabra)
        if pos == "VB":
            verbos.append(conjugate(word, tense=INFINITIVE))
    return verbos

cadena = 'Imprima un listado de los archivos que contiene el directorio actual. La información a mostrar deberá ser nombre \n ' \
         'de archivo, tamaño y fecha de su último acceso. Tener en cuenta que funcione en cualquier plataforma.'

print(verbosInfinitivos(cadena))