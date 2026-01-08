import csv
import os
import numpy as np

moj_folder = "C:/Users/340172/Downloads/guided_practice/"

lista_plikow = os.listdir(moj_folder)
#print(lista_plikow)

lista = []

for plik in lista_plikow:
    nazwa = moj_folder + plik
    print(nazwa)

    with open(nazwa,'r',encoding="utf8") as plikcsv:
        csvreader = csv.reader(plikcsv)
        next(csvreader)

        for wiersz in csvreader:
            lista.append(wiersz)

    tablica = np.array(lista)

#print(tablica[:,4])
#print(tablica)

temperatura = []
opad = []


for i in range(0,len(tablica[:,4])):
    temperatura.append(float(tablica[i,4]))
    opad.append(float(tablica[i,4]))

temperatura = np.array(temperatura)
opad = np.array(opad)

minimalna_temperatura = min(temperatura)
maksymalna_temperatura = max(temperatura)

print(minimalna_temperatura)
print(maksymalna_temperatura)

indeks_temperatura_min = np.where(temperatura == minimalna_temperatura)
indeks_temperatura_max = np.where(temperatura == maksymalna_temperatura)

godzina_min_temp = tablica[indeks_temperatura_min,3]
data_min_temp = tablica[indeks_temperatura_min,2]
lokalizacja_min_temp = tablica[indeks_temperatura_min,1]
godzina_max_temp = tablica[indeks_temperatura_max,3]
data_max_temp = tablica[indeks_temperatura_max,2]
lokalizacja_max_temp = tablica[indeks_temperatura_max,1]

napis_temp_min = "Temperaturę minimalną wynoszącą " + str(minimalna_temperatura) + " st. C zanotowano na stacji " + str(lokalizacja_min_temp[0][0]) + " dnia " +str(data_min_temp[0][0]) + " o godzinie " + str(godzina_min_temp[0][0])
print(napis_temp_min)
napis_temp_max = "Temperaturę maksymalną wynoszącą " + str(maksymalna_temperatura) + " st. C zanotowano na stacji " + str(lokalizacja_max_temp[0][0]) + " dnia " +str(data_max_temp[0][0]) + " o godzinie " + str(godzina_max_temp[0][0])
print(napis_temp_max)