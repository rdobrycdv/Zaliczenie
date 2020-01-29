import numpy as np
import csv

print('Wybierz funkcję:')
fun = (int(input('1 - funkcja liniowa, 2-funkcja kwadratowa, 3-funkcja odwrotna')))

if fun == 1:
    print ("Rowanie kwardatowe")
    print('Podaj a')
    a = int(input())
    
    print('Podaj b')
    b = int(input())
    

    x = np.linspace(-5,5,100)
    
    y = []  
    for i in x:
        y.append(a * i + b)
        
       
elif fun == 2:
    print ("Rowanie kwardatowe")
    print('Podaj a')
    a = int(input())
    
    print('Podaj b')
    b = int(input())
    
    print('Podaj c')
    c = int(input())
    


    p = -b/(2*a)
    q = a*p*p + b*p + c
    
    x = np.linspace(-5,5,100)
    
    l1=[]
    l2=[]
    
    for i in x:
        y=a*(i**2)+b*i+c
        l1.append(i)
        l2.append(y)
            
    
if fun == 3:
    print ("funkcja odwrotna")
    print('Podaj a')
    a = int(input())
    
    print('Podaj n')
    n = int(input())
    

    x = np.linspace(-5,5,100)
    
    y = []  
    for i in x:
        y.append(a / i ** n)