# srednia arytmetyczna listy
def Sr(wart):
    srednia = 0
    liczba = len(wart)
    for i in range(0, liczba):
        srednia = srednia + wart[i]
    srednia = srednia / liczba
    return srednia

# wariancja podanej listy
def Wariancja(wart):
    liczba = len(wart)
    wariancja = 0
    srednia = Sr(wart)
    for i in range(0, liczba):
        wariancja = wariancja + (srednia - wart[i]) * (srednia - wart[i])
    wariancja = wariancja / liczba
    return wariancja