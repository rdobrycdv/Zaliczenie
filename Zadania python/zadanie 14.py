#Utworzyć skrypt z interfejsem tekstowym, który będzie zwracać wiersz n-tego rzędu z 
#trójkąta Pascala (użytkownik podaje n, program zwraca odpowiadający wiersz trójkąta)
print("podaj liczbe")
lic = int(input())


def wiersz (x): # x numer wiersza
    wyn = [] #pusta lista
    poprzedni = 0
    for i in x:
        wyn.append(i + poprzedni)
        poprzedni = i
    wyn.append(poprzedni) #dodanie wyniku  do listy
    return wyn
    
def trojkat(n):
    wynik = []
    obecnie = [1]
    for i in range(0, n):
        wynik.append(obecnie)
        obecnie = wiersz(obecnie)
        
    return wynik

print(trojkat(lic))