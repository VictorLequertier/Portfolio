from math import *
import numpy as np


#On initialise la grille:
ecole =(70,70)
n=10
"""size of the grid"""

def initGrille(n):
    a=np.empty([n,n], dtype = list)
    for i in range (n):
        for j in range (n):
            a[i][j]=[]
    return(a)
    
def getTaille():
    global n
    return(n)

def afficherGrille(grille):
    return(grille)

