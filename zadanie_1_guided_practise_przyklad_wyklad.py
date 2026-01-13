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

moj_folder = "C:/Users/340172/Downloads/guided_practice/"

#ciezka_test = "C:/Users/340172/Downloads/guided_practice/synop_20260106_2100.csv"
#rint(lista_plikow(moj_folder))
#rint(czytaj_plik_meteo(sciezka_test))

lista_plikow = lista_plikow(moj_folder)
min_temp_wektor = []

for plik in lista_plikow:
    sciezka_i_plik = moj_folder + plik
    tablica_Danych = czytaj_plik_meteo(sciezka_i_plik)
    minimalna_temperatura = oblicz_min_temp(tablica_Danych)
    min_temp_wektor.append(minimalna_temperatura)

print(min_temp_wektor)



#temperatura = []
#opad = []


#for i in range(0,len(tablica[:,4])):
 #   temperatura.append(float(tablica[i,4]))
 #   opad.append(float(tablica[i,4]))

#temperatura = np.array(temperatura)
#opad = np.array(opad)

#minimalna_temperatura = min(temperatura)
#maksymalna_temperatura = max(temperatura)

#print(minimalna_temperatura)
#print(maksymalna_temperatura)

#indeks_temperatura_min = np.where(temperatura == minimalna_temperatura)
#indeks_temperatura_max = np.where(temperatura == maksymalna_temperatura)

#godzina_min_temp = tablica[indeks_temperatura_min,3]
#data_min_temp = tablica[indeks_temperatura_min,2]
#lokalizacja_min_temp = tablica[indeks_temperatura_min,1]
#godzina_max_temp = tablica[indeks_temperatura_max,3]
#data_max_temp = tablica[indeks_temperatura_max,2]
#lokalizacja_max_temp = tablica[indeks_temperatura_max,1]

#napis_temp_min = "Temperaturę minimalną wynoszącą " + str(minimalna_temperatura) + " st. C zanotowano na stacji " + str(lokalizacja_min_temp[0][0]) + " dnia " +str(data_min_temp[0][0]) + " o godzinie " + str(godzina_min_temp[0][0])
#print(napis_temp_min)
#napis_temp_max = "Temperaturę maksymalną wynoszącą " + str(maksymalna_temperatura) + " st. C zanotowano na stacji " + str(lokalizacja_max_temp[0][0]) + " dnia " +str(data_max_temp[0][0]) + " o godzinie " + str(godzina_max_temp[0][0])
#print(napis_temp_max)