import requests
import time
import numpy as np
import csv

def pobierz_dane_synop():
    url = "https://danepubliczne.imgw.pl/api/data/synop/format/csv"
    req = requests.get(url) 
    
    linie = req.content.decode('utf-8').splitlines()
    reader = csv.reader(linie)
    dane = list(reader)
    return np.array(dane) 

def wyswietl_stacje(tablica_danych):
    print("Dostępne stacje synoptyczne (ID i nazwa):")
    for wiersz in tablica_danych[1:]: 
        print("Kod:", wiersz[0], "- Stacja:", wiersz[1])

def oblicz_srednia_temp(lista_temperatur):
    if not lista_temperatur:
        return 0
    wektor_temp = np.array(lista_temperatur).astype(float) 
    return np.mean(wektor_temp)


dane_poczatkowe = pobierz_dane_synop()
wyswietl_stacje(dane_poczatkowe)

kody_stacji = dane_poczatkowe[:, 0]

while True:
    wybrany_kod = input("\nWpisz kod wybranej stacji: ").strip()
    
    if wybrany_kod in kody_stacji:
        break 
    else:
        print("Błąd: Kod " + wybrany_kod + " nie istnieje w bazie IMGW. Spróbuj ponownie.")

while True:
    print("\nPodaj czas zakończenia zbierania danych (format: YYYY-MM-DD HH:MM:SS)")
    przyszla_data = input("Data i godzina: ")
    try:
        przyszla_data_struktura = time.strptime(przyszla_data, "%Y-%m-%d %H:%M:%S")
        czas_zakonczenia = time.mktime(przyszla_data_struktura)
        
        if czas_zakonczenia <= time.time():
            print("Wpisana data już minęła. Podaj czas z przyszłości.")
        else:
            break  
    except ValueError:
        print("Nieprawidłowy format daty. Spróbuj ponownie")

print()

gromadzone_temperatury = []
zaimportowane_godziny = set()
czas_startu = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

print("Rozpoczynam zbieranie danych dla stacji " + wybrany_kod)

while time.time() < czas_zakonczenia:
    aktualne_dane = pobierz_dane_synop()
    nowe_dane_pobrane = False
    
    if aktualne_dane is not None:
        for wiersz in aktualne_dane[1:]:
            if wiersz[0] == wybrany_kod:
                godzina_pomiaru = wiersz[3]
                temp = wiersz[4]
                data = wiersz[2]
                do_tabeli = godzina_pomiaru + " " +  data
                if do_tabeli not in zaimportowane_godziny:
                    gromadzone_temperatury.append(float(temp))
                    zaimportowane_godziny.add(do_tabeli)
                    print("[" + time.strftime('%H:%M:%S') + "] Nowy odczyt z godziny " + godzina_pomiaru + ":00 -> " + temp + "°C")
                    nowe_dane_pobrane = True
                else:
                    print("[" + time.strftime('%H:%M:%S') + "] Dane z godziny " + godzina_pomiaru + ":00 już są.")
                break
    
    if nowe_dane_pobrane and int(godzina_pomiaru) == time.localtime().tm_hour:
        teraz = time.localtime()
        sekundy_do_pelnej = (60 - teraz.tm_min) * 60 - teraz.tm_sec
        do_czekania = sekundy_do_pelnej + 60
    else:
        do_czekania = 300 

    if time.time() + do_czekania > czas_zakonczenia:
        print("\n[" + time.strftime('%H:%M:%S') + "] Kolejne sprawdzenie wypadłoby po czasie zakończenia. Zbieranie danych zostało zakończone.")
        break

    if nowe_dane_pobrane:
        print("Dane pobrane. Następne sprawdzenie za około " + str(int(do_czekania/60)) + " min.")
    else:
        print("Nowych danych jeszcze nie wystawiono. Ponowię próbę za 5 minut.")
        
    time.sleep(do_czekania)

if gromadzone_temperatury:
    srednia = oblicz_srednia_temp(gromadzone_temperatury)
    czas_konca = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

    wynik_tekst = "Statystyka dla stacji " + wybrany_kod + "\n"
    wynik_tekst += "Przedział czasu: " + czas_startu + " do " + czas_konca + "\n"
    wynik_tekst += "Obliczona średnia temperatura: " + str(round(srednia, 2)) + "°C"
    
    with open("wyniki_statystyka.txt", "w", encoding="utf-8") as plik: 
        plik.write(wynik_tekst)
    
    print("\nZadanie zakończone. Wyniki zapisano do pliku wyniki_statystyka.txt")
else:
    print("\nNie zgromadzono żadnych danych.")