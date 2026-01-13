import csv
import requests
import numpy as np
import pandas as pd

url = "https://danepubliczne.imgw.pl/api/data/synop"

response = requests.get(url)
dane = response.json()



lista_wstepna = []

def lista_stacji(a):
    lista_wstepna = []
    for zmienna in dane:
        lista_wstepna.append((zmienna["id_stacji"],zmienna["stacja"]))
    return lista_wstepna

lista_stacji = lista_stacji(dane)

lista_stacji1 = np.array(lista_stacji)

for id_stacji, stacja in lista_stacji1:
    print(id_stacji,stacja)

wybrana_stacja = input("Wpisz kod wybranej stacji:")


if wybrana_stacja != lista_stacji:
    haslo = input("Kod nierozpoznany.Wpisz kod poprawnej stacji: ")
    print(haslo)








