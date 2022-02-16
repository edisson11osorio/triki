from ast import Break
import random
import os

#--INICIO DEL JUEGO / FICHA--

def inicio_juego():
    print("***Bienvenido***")
    while True:
        ficha = input("Selecione ficha: X / O \n")
        ficha = ficha.upper()
        if ficha=="X":
            humano="X"
            ordenador="O"
            break
        elif ficha=="O":
            humano="O"
            conputador="X"
            break
        else:
            print("por favor ntroduc un ficha")

#--Creacion del tablero--

def tablero():
    print("TRES EN RAYA / TIC TAC TOE")
    print()
    print("         |         |      ")
    print("1  {}     |2   {}   |3    ".format(matriz[0],matriz[1],matriz[2]))
    print("         |         |      ")
    print("------------------------")
    print("         |         |      ")
    print("1  {}     |2   {}   |3    ".format(matriz[3],matriz[4],matriz[5]))
    print("         |         |")
    print("------------------------")
    print("         |         |     ")
    print("1  {}     |2   {}   |3    ".format(matriz[0],matriz[1],matriz[2]))
    print("         |         |       ")