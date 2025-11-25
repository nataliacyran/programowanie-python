zmienna = 6.7

#sprawdzamy czy zmienna jest liczbą (float lub int)

if isinstance(zmienna,int) or isinstance(zmienna,float):
    print("Zmienna jest liczbą.")
else:
    print("Zmienna nie jest liczbą.")

if isinstance(zmienna,int) or zmienna.is_integer()==True:
    print("Jest to liczba całkowita")
else:
    print("Nie jest to liczba o wartościach całkowitoliczbowych.")