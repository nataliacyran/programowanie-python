import requests
import time
import numpy as np
import csv
import io

def pobierz_dane_synop():
    url = "https://danepubliczne.imgw.pl/api/data/synop/format/csv"
    req = requests.get(url) 
    
    f = io.StringIO(req.content.decode('utf-8'))
    reader = csv.reader(f)
    dane = list(reader)
    return np.array(dane) 

def wyswietl_stacje(tablica_danych):
    print("Dostępne stacje synoptyczne (ID i nazwa):")
    for wiersz in tablica_danych[1:]: 
        print(f"Kod: {wiersz[0]} - Stacja: {wiersz[1]}")

def oblicz_srednia_temp(lista_temperatur):
    if not lista_temperatur:
        return 0
    wektor_temp = np.array(lista_temperatur).astype(float) 
    return np.mean(wektor_temp)


dane_poczatkowe = pobierz_dane_synop()
wyswietl_stacje(dane_poczatkowe)


wybrany_kod = input("\nWpisz kod wybranej stacji: ")


kody_stacji = dane_poczatkowe[:, 0]
if wybrany_kod not in kody_stacji:
    print("Błąd: Nieistniejący kod stacji!")
    exit()


print("Podaj czas zakończenia zbierania danych (format: YYYY-MM-DD HH:MM:SS)")
przyszla_data_str = input("Data i godzina: ")
try:
    przyszla_data_struktura = time.strptime(przyszla_data_str, "%Y-%m-%d %H:%M:%S")
    czas_zakonczenia = time.mktime(przyszla_data_struktura) 
except ValueError:
    print("Błąd: Niepoprawny format daty!")
    exit()

gromadzone_temperatury = []
czas_startu = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

print(f"Rozpoczynam zbieranie danych dla stacji {wybrany_kod}...")


while time.time() < czas_zakonczenia:
    aktualne_dane = pobierz_dane_synop()
    
    znaleziono = False
    for wiersz in aktualne_dane:
        if wiersz[0] == wybrany_kod: 
            temp = wiersz[3]
            gromadzone_temperatury.append(float(temp)) 
            print(f"[{time.strftime('%H:%M:%S')}] Odczytano temperaturę: {temp}°C")
            znaleziono = True
            break
            
    if not znaleziono:
        print("Nie udało się odnaleźć danych dla tej stacji w tej chwili.")
    if time.time() + 300 < czas_zakonczenia:
        print("Czekam 5 minut na kolejny odczyt...")
        time.sleep(300) 
    else:
        break

if gromadzone_temperatury:
    srednia = oblicz_srednia_temp(gromadzone_temperatury)
    czas_konca = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    
    wynik_tekst = f"Statystyka dla stacji {wybrany_kod}\n"
    wynik_tekst += f"Przedział czasu: {czas_startu} do {czas_konca}\n"
    wynik_tekst += f"Obliczona średnia temperatura: {srednia:.2f}°C"
    
    with open("wyniki_statystyka.txt", "w", encoding="utf-8") as plik: 
        plik.write(wynik_tekst)
    
    print("\nZadanie zakończone. Wyniki zapisano do pliku wyniki_statystyka.txt")
else:
    print("\nNie zgromadzono żadnych danych.")