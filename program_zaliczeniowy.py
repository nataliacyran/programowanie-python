import csv
import requests
import numpy as np
import pandas as pd
from datetime import datetime
import time


url = "https://danepubliczne.imgw.pl/api/data/synop"

pobrane = requests.get(url)
dane = pobrane.json()



lista_wstepna = []

def pobierz_lista_stacji(a):
    lista_wstepna = []
    for zmienna in dane:
        lista_wstepna.append((zmienna["id_stacji"],zmienna["stacja"]))
    return lista_wstepna

pobierz_lista_stacji = pobierz_lista_stacji(dane)

lista_stacji = np.array(pobierz_lista_stacji)

for id_stacji, stacja in lista_stacji:
    print(id_stacji,stacja)

wybrana_stacja = input("Wpisz kod wybranej stacji: ")



while wybrana_stacja not in lista_stacji:
    wybrana_stacja = input("Kod nierozpoznany. Wpisz poprawny kod stacji: ")
else:
    print("Wybrano stację o poprawnym kodzie: " + wybrana_stacja)

format_daty = "%Y-%m-%d %H:%M"
while True:
    wybrana_data = input("Wprowadź datę i godzinę końcową (RRRR-MM-DD GG:MM): ")
    try:
        data_koncowa = datetime.strptime(wybrana_data, format_daty)
        
        if data_koncowa > datetime.now():
            print("Program będzie zbierał dane do: " + str(data_koncowa))
            break
        else:
            print("Błąd: Wprowadzona data już minęła")
            
    except ValueError:
        print("Błąd: Niepoprawny format lub data nie istnieje. Spróbuj ponownie.")

pomiary_temperatury = []
ostatnia_godzina = None
while datetime.now() < data_koncowa:
        odpowiedz = requests.get(url)
        dane_api = odpowiedz.json()
        wybrana_stacja_dane = next((item for item in dane_api if item["id_stacji"] == wybrana_stacja), None)
        
        if wybrana_stacja_dane:
            aktualna_godzina = wybrana_stacja_dane["godzina_pomiaru"]
            aktualna_temp = float(wybrana_stacja_dane["temperatura"])
            
            if aktualna_godzina != ostatnia_godzina:
                pomiary_temperatury.append(aktualna_temp)
                ostatnia_godzina = aktualna_godzina
                
                print(datetime.now().strftime('%H:%M') + " Nowy odczyt. Godzina " + str(aktualna_godzina) + ". Temp: " + str(aktualna_temp) + " °C.")
                print("Aktualna liczba pomiarów: " + str(len(pomiary_temperatury)))
                time.sleep(60)
                
            


if pomiary_temperatury:
    srednia = sum(pomiary_temperatury) / len(pomiary_temperatury)
    print("\n" + "Koniec czasu pomiaru. Średnia temperatura dla stacji " + str(wybrana_stacja) + " wyniosła: " + srednia)
else:
    print("\n" + "Nie zebrano żadnych danych.")

