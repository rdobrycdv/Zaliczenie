def srednia(x):
    return sum(x)/len(x)

def sos(x):
    #suma odchylen sekwencji
    c = srednia(x)
    ss = sum((x-c)**2 for x in x)
    return ss

def odch(x, ddof=0):
    n = len(x)
    if n < 2:
        raise ValueError('odchylenie standardowe potrzebuje conajmniej dwoch wartosci')
    pvar = sos(x)/(n-ddof)
    return pvar**0.5

def skosnosc(x, y=0):
    n = len(x)
    pvar = sos(x)/(n-y)
    return(1/odch(x)**3)*(pvar**2)

