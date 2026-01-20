import requests
import numpy as np
import time

def pobierz_dane():
    url = "https://danepubliczne.imgw.pl/api/data/synop/format/csv"
    req = requests.get(url)
    tekst = req.content.decode('utf-8')
    wiersze = tekst.splitlines()
    lista = []
    for wiersz in wiersze:
        lista.append(wiersz.split(','))
    return np.array(lista)


dane = pobierz_dane()
for wiersz in dane[1:]:
    print("Kod: " + str(wiersz[0]) + " - Stacja: " + str(wiersz[1]))

wybrany_kod = input("\n" + "Wpisz kod stacji: ")

if wybrany_kod not in dane[:, 0]:
    print("Blad: Nieistniejacy kod stacji!")
    exit()

print("Podaj czas zakonczenia (format: RRRR-MM-DD HH:MM:SS)")
przyszla_data_str = input("Data i godzina: ")

try:
    przyszly_czas = time.mktime(time.strptime(przyszla_data_str, "%Y-%m-%d %H:%M:%S"))
except ValueError:
    print("Blad: Zly format daty!")
    exit()

gromadzone_temp = []
czas_startu = time.strftime("%Y-%m-%d %H:%M:%S")

while time.time() < przyszly_czas:
    aktualne = pobierz_dane()
    znaleziono = False
    
    for wiersz in aktualne:
        if wiersz[0] == wybrany_kod:
            try:
                temp = float(wiersz[3])
                gromadzone_temp.append(temp)
                print(f"[{time.strftime('%H:%M:%S')}] Odczyt: {temp} C")
                print("Czekam 5 minut na kolejny odczyt.")
                znaleziono = True
                if time.time() + 300 < przyszly_czas:
                    time.sleep(300)
                else:
                    break
            except (ValueError, IndexError):
                print("Blad odczytu wartosci temperatury.")
            


if gromadzone_temp:
    srednia = np.mean(gromadzone_temp)
    czas_konca = time.strftime("%Y-%m-%d %H:%M:%S")
    
    wynik = f"Statystyka dla stacji {wybrany_kod}\n"
    wynik += f"Przedzial: {czas_startu} do {czas_konca}\n"
    wynik += f"Srednia temperatura: {round(srednia, 2)} C"
    
    with open("wyniki.txt", "w", encoding="utf-8") as plik:
        plik.write(wynik)
    print("\nZapisano wyniki do pliku wyniki.txt")
else:
    print("\nBrak danych do obliczen.")