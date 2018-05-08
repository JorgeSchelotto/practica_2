import random


colores = list(map(lambda str: str.replace('\n',''),open('colores.txt', 'r').readlines()))
coordenadas = list(map(lambda str: str.replace('\n',''),open('coordenadas.txt', 'r').readlines()))

estructura = {}

for key in coordenadas:
	estructura[] = key


print(estructura)
print (coordenadas)





