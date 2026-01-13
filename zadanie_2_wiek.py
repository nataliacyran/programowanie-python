wiek_1=input("Wpisz wiek pierwszego studenta:")

with open("wiek_drugiego_studenta.txt") as plik:
    wiek_2 = plik.read()

wiek_1=int(wiek_1)
wiek_2=int(wiek_2)


if (wiek_1<wiek_2):
    tekst="Pierwszy student jest mlodszy od studenta drugiego o " + str(wiek_2-wiek_1) + " lat(a)."
    print(tekst)
else:
    tekst="Pierwszy student jest starszy od drugiego studenta o " + str(wiek_1-wiek_2) + " lat(a)."
    print(tekst)

with open("wiek2.txt",'a') as plik:
    plik.write(tekst)