#!/bin/python3.7
import os
from colorama import init, Fore
init()

diccionario = ["juan","2002"]

pwd="juan2002"

for a in diccionario:
    if a == pwd:
        password = a
        print(Fore.GREEN+"[+] Exito : "+password)
    else:
        print(a)
    if len(diccionario) > 1:
        for b in diccionario:
            if a+b == pwd:
                password = a+b
                print(Fore.GREEN+"[+] Exito : "+password)
            else:
                print(a+b)
            if len(diccionario) > 2:
                for c in diccionario:
                    if a+b+c == pwd:
                        password = a+b+c
                        print(Fore.GREEN+"[+] Exito : "+password+Fore.WHITE)
                    else:
                        print(a+b+c)
            else:
                break
    else:
        break