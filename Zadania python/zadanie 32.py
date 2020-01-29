import numpy as np
import matplotlib.pyplot as plt
macierz = np.zeros(10*10).reshape(10, 10)
plt.imshow(macierz, cmap = 'Greys')


def bochenek(i, j):
    bochenek = np.array([[0, 255, 255, 0], [255, 0, 0, 255], [255, 0, 255, 0],[0, 255, 0, 0]])
    macierz[i:i+4, j:j+4] = bochenek
    plt.imshow(macierz, cmap = 'Greys')
    
def blok(i, j):
    glider = np.array([[255, 255, 0], [255, 255, 0], [0, 0, 0]])
    macierz[i:i+3, j:j+3] = glider
    plt.imshow(macierz, cmap = 'Greys')

def ul(i, j):
    bochenek = np.array([[0, 255, 255, 0], [255, 0, 0, 255], [0, 255, 255, 0],[0, 0, 0, 0]])
    macierz[i:i+4, j:j+4] = bochenek
    plt.imshow(macierz, cmap = 'Greys')
    
def lodz(i, j):
    glider = np.array([[255, 255, 0], [255, 0, 255], [0, 255, 255]])
    macierz[i:i+3, j:j+3] = glider
    plt.imshow(macierz, cmap = 'Greys')
    
def swiatla(i, j):
    glider = np.array([[0, 255, 0], [0, 255, 0], [0, 255, 0]])
    macierz[i:i+3, j:j+3] = glider
    plt.imshow(macierz, cmap = 'Greys')
    
def zaba(i, j):
    bochenek = np.array([[0, 255, 0, 0], [0, 255, 255, 0], [0, 255, 255, 0],[0, 0, 255, 0]])
    macierz[i:i+4, j:j+4] = bochenek
    plt.imshow(macierz, cmap = 'Greys')
    
def latarnia(i, j):
    bochenek = np.array([[0, 255, 255, 0], [255, 0, 255, 255], [255, 255, 255, 0],[0, 255, 0, 0]])
    macierz[i:i+4, j:j+4] = bochenek
    plt.imshow(macierz, cmap = 'Greys')
    
    


