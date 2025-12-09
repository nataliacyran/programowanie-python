import csv
import numpy as np

plik = "meteo.csv"

lista = []

with open(plik,'r') as plikcsv:
    csvreader = csv.reader(plikcsv)
    naglowek = next(csvreader)
    #print(naglowek)

    licznik = 0
    for wiersz in csvreader:
        lista.append(wiersz)

tablica = np.array(lista)
#print(tablica)

#print(tablica[3])


liczba_elementow = len(tablica)

suma_temperatur = 0
suma_cisnienia = 0
suma_wilgotnosci = 0
for i in range(0,5):
    temperatura = float(tablica[i][4])
    #print(temperatura)
    suma_temperatur = suma_temperatur + temperatura
    #print(suma_temperatur)
    wilgotnosc = float(tablica[i][-3])
    #print(wilgotnosc)
    suma_wilgotnosci = suma_wilgotnosci + wilgotnosc
    #print(suma_wilgotnosci)
    cisnienie = float(tablica[i][-1])
    #print(cisnienie)
    suma_cisnienia = suma_cisnienia + cisnienie
    #print(suma_cisnienia)


srednia_temperatura = suma_temperatur/liczba_elementow
print(srednia_temperatura)

srednia_wilgotnosc = suma_wilgotnosci/liczba_elementow
print(srednia_wilgotnosc)

srednie_cisnienie = suma_cisnienia/liczba_elementow
print(srednie_cisnienie)