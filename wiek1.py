wiek_studenta_1=input("Wpisz wiek pierwszego studenta:")
wiek_studenta_2=input("Wpisz wiek drugiego studenta:")

wiek_studenta_1=int(wiek_studenta_1)
wiek_studenta_2=int(wiek_studenta_2)

print(wiek_studenta_1)
print(wiek_studenta_2)

if wiek_studenta_1>wiek_studenta_2:
        moj_tekst="Pierwszy student jest starszy i ma" + str(wiek_studenta_1) + "lat(a)."
        print(moj_tekst)

with open("wiek1.txt",'a') as plik:
        plik.write(moj_tekst)
