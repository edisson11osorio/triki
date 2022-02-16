from ast import Break
import email
import random
import os
from struct import calcsize

from pyrsistent import T

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
    print("4  {}     |5   {}   |6    ".format(matriz[3],matriz[4],matriz[5]))
    print("         |         |")
    print("------------------------")
    print("         |         |     ")
    print("7  {}     |8   {}   |9    ".format(matriz[6],matriz[7],matriz[8]))
    print("         |         |       ")

#--DEFINIR FINLAES DE LA PARTIDA--

def empate(matriz):
    empate=True
    i=0
    while(empate==True and i<9):
        if matriz[i]==" ":
            empate=False
        i=i+1

    return empate

def victoria(matriz):
    if (matriz[0]==matriz[1]==matriz[2]!=" "or matriz[3]==matriz[4]==matriz[5]!=" "or matriz[6]==matriz[7]==matriz[8]!=" "
       or matriz[0]==matriz[3]==matriz[6]!=" "or matriz[1]==matriz[4]==matriz[7]!=" "or matriz[2]==matriz[5]==matriz[8]!=" "or 
       matriz[0]==matriz[4]==matriz[8]!=" "or matriz[2]==matriz[4]==matriz[6]!=" "):
       return True
    else:
        return False


#--MOVIMENTOS--

def movimiento_jugador():
    while True:
        posiciones=[1, 2, 3, 4, 5, 6, 7, 8, 9]
        casilla=int(input("Selecione una casilla: "))
        if casilla not in posiciones:
            print("Casilla no disponible")

        else:
            if matriz[casilla-1]