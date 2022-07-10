#!/bin/python3.7
import os
import pyautogui as pg
import time as tm
import optparse

diccionario=[]
def init_hack():
    print("[1] Facebook     [2] Instagram\n[3] Red Wifi")
    entorno = input(">> ")
    if entorno == "1":
        print("[-] Funcion no desarrollada... :(")
    elif entorno == "2":
        print("[-] Funcion no desarrollada... :(")
    if entorno == "3":
        essid = input("SSID >> ")
        

def init_program():
    print("\n[0] Cancel   [1] Add   [2] Del   [3] Show   [4] Confirm")
    action = input(">>")
    if action == "0":
        exit()
    elif action == "1":
        obj_diccionario = input("Añadir >> ")
        diccionario.append(obj_diccionario)
        init_program()
    elif action == "2":
        obj_diccionario = input("Eliminar >> ")
        diccionario.remove(obj_diccionario)
        init_program()
    elif action == "3":
        for a in range(0, len(diccionario)):
            print("["+str(a)+"] "+diccionario[a])
        init_program()
    elif action == "4":
        init_hack(diccionario)
    else:
        print("[-] Err: Opcion no existe.")
        init_program()

init_program()



import os
diccionario = ["pepe","juan","2002"]

for a in diccionario:
    print(a)
    if len(diccionario) > 1:
        for b in diccionario:
            print(a+b)
            if len(diccionario) > 2:
                for c in diccionario:
                    print(a+b+c)
            else:
                break
    else:
        break