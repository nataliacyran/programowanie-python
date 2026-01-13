import csv
import os
import numpy as np

def lista_plikow(folder):
    lista = os.listdir(folder)
    return lista

def czytaj_plik_meteo(sciezka):
    lista = []
    with open(sciezka,'r',encoding="utf8") as plikcsv:
       csvreader = csv.reader(plikcsv)
       next(csvreader)
       for wiersz in csvreader:
            lista.append(wiersz)
    tablica = np.array(lista)
    return tablica

def oblicz_min_temp(moja_tablica):
    temperatura = []
    for i in range(0,len(moja_tablica[:,4])):
      temperatura.append(float(moja_tablica[i,4]))
    temperatura = np.array(temperatura)
    minimalna_temperatura = min(temperatura)
    return minimalna_temperatura

