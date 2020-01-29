#twórz skrypt do znajdowania miejsc zerowych trójmianu kwadratowego 
from math import sqrt
a = input("Podaj a: ")
b = input("Podaj b: ")
c = input("Podaj c: ")
a=int(a)
b=int(b)
c=int(c)
delta = b*b - 4*a*c 
if delta > 0: 
        x1 = (-b - sqrt(delta))/(2*a) 
        x2 = (-b + sqrt(delta))/(2*a) 
        print("x1= ",x1)
        print("x2= ",x2)
elif delta == 0: 
        x = -b/2/a 
        print("x=",x)
else : 
        print("brak pierwiastkow rzeczywistych")