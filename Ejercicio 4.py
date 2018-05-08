# Encoding = UTF-8
from pattern.es import singularize, pluralize

print(singularize('caballos'))


def cambiapalabras(diccionario):
    """Recibe un diccionario con dos keys: ’s’ y ’p’. Donde ’s’ indica que la lista asociada contiene palabras en singular
    y ’p’ indica que la lista asociada contiene palabras en plural. Devuelve un diccionario con as palabras cambiadas
    de singular a plurar y viceversa"""
    cambiado = {}
    for key in diccionario:
        if key == 's':
            cambiado[key] = list(map(pluralize, diccionario.get(key)))
        elif key == 'p':
            cambiado[key] = list(map(singularize, diccionario.get(key)))

    return cambiado


cambiar = {'s': ['gato', 'caballo', 'silla'], 'p': ['informaticas', 'psicologas', 'ingenieras']}

print(cambiapalabras(cambiar))
# devuelve:
# {'p': ['informatica', 'psicologa', 'ingeniera'], 's': ['gatos', 'caballos', 'sillas']}
