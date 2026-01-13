#def moj_napis():
   # tekst = "Nowy napis"
    #return tekst

#zmienna = moj_napis()
#print(zmienna)


#import math

#def obwod(r):
 #   ob = 2* math.pi * r
   # return ob

#obwod_kola = obwod(5)

#print(obwod_kola)

#def warunek(tf):
  #  if tf == True:
  #      print("Prawda")
  #  elif tf == False:
 #       print("Falsz")
 #   else:
 #       print("Parametr nie jest zmienną logiczną True/False")

#wynik = warunek(3)

import math

def pole_i_obwod(r):
    p = math.pi * r * r
    obw = 2* math.pi * r
    return p,obw

wynik = pole_i_obwod(5)
print(wynik)

def sprawdz_Czy_lancuch(a):
    if isinstance(a,str) == True:
        print("Typ zmiennej: lancuch.")
        czy_to_lancuch = True
    else:
        print("Typ zmiennej: nie jest to lancuch.")
        czy_to_lancuch = False
    return czy_to_lancuch

b = '3'
wynik = sprawdz_Czy_lancuch(b)
print(wynik)


