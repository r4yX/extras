#!/bin/python3.7

import pyautogui as pg

diccionario=["paul","Paul","PAUL"]
year=["2022","2020","2021","2019","2018","2017","2016","2015","2014","2013","2012","2011","2010"]

for a in range(0,3):
    for b in range(0,13):
        print(diccionario[a]+year[b])
    b=0

