# -*- coding: utf-8 -*-

from tkinter import *
N = 5
Etage = [[i+1 for i in range(N,0,-1)],[],[]]
i=0

class Interface():
    def __init__(self):
        global i
        i = self
        self.fenetre = Tk()
        self.fenetre.title("Tour d'Hanoï")
        self.canvas = Canvas(self.fenetre,height=1500, width=500)
        self.canvas.pack()
        self.posx = 0
        self.posy = 0
        self.afficher()
        self.fenetre.after(5,self.start)
        self.fenetre.mainloop()
    def start(self):
        global Etage,N
        Hanoi(Etage,N,2)
    def afficher(self):
        global Etage
        p = self.posx 
        y = self.posy
        self.canvas.create_rectangle(10+p, 10+y, 100+p, 100+y, fill='white')
        self.canvas.create_rectangle(12+p, 90+y, 38+p, y+90)
        self.canvas.create_rectangle(42+p, 90+y, 68+p, 90+y)
        self.canvas.create_rectangle(72+p, 90+y, 98+p, y+90)
        couleur = [None, 'light blue', 'light green', 'yellow', 'orange', 'red','pink','purple','black']
        for j in range(len(Etage)):
            n=0
            for _ in range(len(Etage[j])):
                n+=1
                I = Etage[j][_]
                self.canvas.create_rectangle(12+28*j+(14//I)+2+p,y+90-10*(n-1),12+28*j+26-14//I-2+p,y+90-10*n,fill=couleur[I])
        self.posx += 100
        if int(self.canvas['width']) < self.posx:
            self.posx = 0
            self.posy += 100

def deplacer(etage, a, b):
    if etage[a] == []:
        return False
    if etage[b] != []:
        if etage[b][-1] < etage[a][-1]:
            return False
    etage[b].append(etage[a][-1])
    etage[a].pop()
    return True

def deplacement(etage,a,b):
    e = deplacer(etage,a,b)
    i.afficher()
    return e 

def Hanoi(etage, n, k, etagenonvide = None):
    if etagenonvide == None:
        # si étage non vide non paramétré, il faut le définir
        for i in [0,1,2]:
            if len(etage[i])!=0:
                etagenonvide = i
    if k==etagenonvide:
        return None #la tour est au bon endroit
    c = [0,1,2]
    c.remove(etagenonvide)
    c.remove(k)
    comp1 = c[0]
    if n==2:
        # déplacement élémentaire
        deplacement(etage, etagenonvide, comp1)
        deplacement(etage, etagenonvide, k)
        deplacement(etage, comp1, k)
        return None
    
    Hanoi(etage, n-1, comp1, etagenonvide)
    deplacement(etage, etagenonvide, k)
    Hanoi(etage, n-1, k, comp1 )
Interface()        
