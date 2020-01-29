import pylab
import matplotlib.pyplot as plt
import numpy as np
import csv

print('Wybierz funkcję do obliczenia:')
fun = (int(input('1-liniowa, 2-kwadratowa, 3-odwrotna')))

if fun == 1:  #wybor funkcji
    print ("ax+b")
    print('Podaj  a')
    a = int(input()) #wprowadzenie wspolczynnika a
    
    print('Podaj b') #wprowadzenie wspolczynnika b
    b = int(input())
    

    x = np.linspace(-5,5,100) #przedzialy do wykresu
    
    y = []  #pusta lista
    for i in x:
        y.append(a * i + b)
    
    fig = plt.figure()    #towrzenie wykresu
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center') #umiejscowienie wykresu
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    pylab.plot(x, y)
    pylab.title('Wykres f(x) = a*x - b') # nazwa wykresu
    pylab.grid(True)
    plt.show()
    
    with open('wyniklinowy.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(x)
        spamwriter.writerow(y)



elif fun == 2:
    print ("Rowanie ax^2+bx+c")
    print('Podaj a')
    a = int(input())
    
    print('Podaj b')
    b = int(input())
    
    print('Podaj c')
    c = int(input())
    


    p = -b/(2*a)
    q = a*p*p + b*p + c
    
    x = np.linspace(-6,6,100)
    
    l1=[]
    l2=[]
    
    for i in x:
        y=a*(i**2)+b*i+c
        l1.append(i)
        l2.append(y)
            
    fig = pylab.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    pylab.plot(l1, l2)
    pylab.title('Wykres f(x) = ax^2+bx+c')
    pylab.grid(True)
    plt.show()
    
    with open('wynikkwadratowy.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(l1)
        spamwriter.writerow(l2)

    
if fun == 3:
    print (" a/x^n")
    print('Podaj a')
    a = int(input())
    
    print('Podaj n')
    n = int(input())
    

    x = np.linspace(-1,1,50)
    
    y = []  
    for i in x:
        y.append(a / i ** n)
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    pylab.plot(x, y)
    pylab.title('Wykres f(x) = a/x^n')
    pylab.grid(True)
    plt.show()
    
    with open('wynikodwrotny.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(x)
        spamwriter.writerow(y)