#ME DA PAJA HACERLO


jugadores = {}
stats = {}
stats2 = {}
stats3 = {}
nivel='nivel'
puntaje='puntaje'
horas='horas'

#Hardcodeo para facilitar la carga
jugador = 'Vincent Price'
stats[jugador] = 'The Abominable Dr. Phibes'
stats[nivel] = 10
stats[puntaje] = 123456
stats[horas] = '10:30:02'
jugadores[jugador] = stats



jugador = 'Boris Karloff'
stats2[jugador] = 'The Mummy'
stats2[nivel] = 21
stats2[puntaje] = 123456123456
stats2[horas] = '200:30:02'
jugadores[jugador] = stats2


jugador = 'Vela Lugosi'
stats3[jugador] = 'Dracula'
stats3[nivel] = 50
stats3[puntaje] = 1234561234562112313231
stats3[horas] = 'is dead'
jugadores[jugador] = stats3


print(jugadores['Boris Karloff'].get('Boris Karloff') + ' == ' + jugadores['Vincent Price'].get('Vincent Price') + ' == ' + jugadores['Vela Lugosi'].get('Vela Lugosi'))