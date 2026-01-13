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
print()

wybrana_stacja = input("Wpisz identyfikator wybranej stacji: ")
print()

while wybrana_stacja not in lista_stacji1[:, 0]:
    wybrana_stacja = input("Kod nierozpoznany. Wpisz kod poprawnej stacji: ")
    print()








