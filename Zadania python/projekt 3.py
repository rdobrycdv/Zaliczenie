#Utwórz klase Vector2D. Wykorzystaj cala wiedze jaka posiadasz na temat wektorów
#na plaszczyznie. Zdefiniuj wszystkie znane Ci operacje.
import math as math 

class Vector2D(): 
    def __init__(self,x,y): 
        self.x=x 
        self.y=y 

    def wspolrzedne(self): 
        return(self.x,self.y)         

    def sumaw(self,b): #suma wektorow
        self.x=self.x+b.x 
        self.y=self.y+b.y 
        print(self.x) 
        print(self.y) 

    def roznicaw(self,b): #roznica wektorow
        self.x=self.x-b.x 
        self.y=self.y-b.y 
        print(self.x) 
        print(self.y) 

         
    def mnliczba(self,c):  #mnozenie liczb
        self.x=self.x*c 
        self.y=self.y*c 
        print(self.x,self.y) 

         
    def mnw(self,b):  #mnozenie wektorow
        self.x=self.x*b.x 
        self.y=self.y*b.y 
        print(self.x) 
        print(self.y)  

    def modul(self): 
        print(((self.x)**2+(self.y)**2)**0.5) 

    def wprzeciw(self): 
        return (-self.x,-self.y) 

    def okat(self,k): 
        sin=(math.sin(k*(math.pi/180))) 
        cos=(math.cos(k*(math.pi/180))) 
        x=self.x 
        y=self.y 
        self.x=x*cos-y*sin 
        self.y=x*sin+y*cos 
        print(self.x, self.y)