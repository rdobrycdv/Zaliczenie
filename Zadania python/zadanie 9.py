#Utwórz skrypt z interfejsem tekstowym, który wyliczy sumę n kolejnych liczb (użytkownik podaje pierwszą i ostatnią liczbę sumy). 
#Uwaga – w zadaniu należy zbudować funkcję własną realizującą dane zadanie

def suma(a, b):
    sumx = ((a + b)/2)*(b-a+1)
    return sumx

print("pierwsza liczba")
a = int(input())
print("ostatnia liczba")
b = int(input())

print(suma(a, b))