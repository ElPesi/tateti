tablero = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

import random

def funcionPrincipal():
    
    p1 = input("Inserte nombre del jugador 1: ")
    

    while True:
        select = input(f"{p1}, ¿quieres jugar con X o O? ").upper()
        if select == 'X' or select == 'O':
            break
        else:
            print("Por favor, selecciona X o O.")
            

    if select == 'X':
        p1_symbol = 'X'
        p2_symbol = 'O'
    else:
        p1_symbol = 'O'
        p2_symbol = 'X'
            
    p2 = input("Inserte nombre del jugador 2:")
            
    starting_player = random.choice([p1, p2])
    print(f"{starting_player} comienza el juego.")
    
funcionPrincipal()

def Table(tablero):
    
    for i in range(0,len(tablero),1):
        print(tablero[i])
        print
    return tablero

Table(tablero)

def juego(tablero, jugada, jugador):a
fila, columna = jugada

    if tablero[fila][columna] != ' ':
        print("¡Esa casilla ya está ocupada! Inténtalo de nuevo.")
            return False

    
tablero[fila][columna] = jugador
    return True


tablero = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

jugador = 'X'
jugada = (0, 0)
juego_realizado = juego(tablero, jugada, jugador)

if juego_realizado:
    for fila in tablero:
        print("|".join(fila))
'''arribai = [0][0]
arrribam = [0][1]
arribad = [0][2]
medioi = [1][0]
centro = [1][1]
mediod = [1][2]
abajoi= [2][0]
abajom= [2][1]
abajod= [2][2]


def juego(tablero):
    jugada = (starting_player)
    
    input(f"")

print(juego(tablero))'''
