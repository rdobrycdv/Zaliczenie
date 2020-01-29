import numpy as np
import matplotlib.pyplot as plt

#najpierw nalezy umiejscowic bochenek prez funkcje na przyklad bochenek(1,2,macierz)
#nastepnie zeby poznac liczbe sasiadow nalezy wspisac na przyklad: suma(2,3,macierz)

macierz = np.zeros(6*6).reshape(6, 6)
plt.figure()


def bochenek(i, j, kwadrat):
    bochenek = np.array([[0, 255, 255, 0], [255, 0, 0, 255], [255, 0, 255, 0],[0, 255, 0, 0]])
    kwadrat[i:i+4, j:j+4] = bochenek

def suma(i, j, m):

    total = int((m[i-1, j-1] + m[i-1, j] + m[i-1, j+1] + 
						m[i, j-1] + m[i, j+1] + 
						m[i+1, j-1] + m[i+1, j] + m[i+1, j+1])/255)
    print("ten punkt ma:", total, "sasiadow")