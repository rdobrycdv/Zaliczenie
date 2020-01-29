#skrypt wszystkie kolejne dzielniki podanej liczby
print("Sprawdzanie dzielników liczby")
x=int(input("podaj liczbę: "))
print("dzielniki podanej liczby to:")
for i in range (1, x+1):
    if (x%i==0):
        print (i)