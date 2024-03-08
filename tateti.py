''' tateti '''

input("Hola Usuarios")


p1 = input("Como se llama el jugador 1")

def check(p1):
    select = input(f"{p1}, ¿quieres jugar con X o O? ")

    if select != 'X' or 'O':
        print("Porfavor ingresar X o O")
    else:
        print("letra asignada") 

    if select == 'X':
        p1_symbol = 'X'
    else:
        p1_symbol = 'O'

p2 = input("Como se llama el jugador 2")

def sorteo(p1,p2):


    print("")
