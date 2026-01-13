import csv
import os
import numpy as np
from funkcje_pomocnicze_meteo import lista_plikow, czytaj_plik_meteo, oblicz_min_temp

moj_folder = "C:/Users/340172/Downloads/guided_practice/"

lista = lista_plikow(moj_folder)
min_temp_wektor = []

for plik in lista_plikow:
    sciezka_i_plik = moj_folder + plik
    tablica_Danych = czytaj_plik_meteo(sciezka_i_plik)
    minimalna_temperatura = oblicz_min_temp(tablica_Danych)
    min_temp_wektor.append(minimalna_temperatura)

print(min_temp_wektor)

