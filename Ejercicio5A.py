# Encoding = UTF-8
from pattern.es import conjugate, INFINITIVE
from pattern.es import parse
from pattern.en import pprint




def infinitivo(str):
    """Recibe un string. Devuelve una lista de verbos en infinitivo."""

    resultado = []
    listaVerbos = parse(str).split()
    # The output of parse() is a string of sentences in which each word has been annotated with the requested tags.
    for nivel2 in listaVerbos:
        for codigo in nivel2:
            if codigo[1] == 'VB' or codigo[1] == 'VBG':
                resultado.append(conjugate(codigo[0], tense=INFINITIVE))

    return resultado




cadena = 'Imprima un listado de los archivos que contiene el directorio actual. La información a mostrar deberá ser nombre \n ' \
         'de archivo, tamaño y fecha de su último acceso. Tener en cuenta que funcione en cualquier plataforma.'

print(infinitivo(cadena))




