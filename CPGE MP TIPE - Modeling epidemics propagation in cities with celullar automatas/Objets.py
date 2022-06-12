from Grille import getTaille
from Grille import ecole
import random

#==============================================================================
n = getTaille()
Pers=[]
M=[]
#---------------------Création de la classe individus:-------------------------

class personne :
    """Each individual is represented by various characteristics:
        -Their ID
        -Their status (enfant/parent/(autre))
        -Their health situation (Sain/Porteur Sain/Malade/Immunisé/Mort)
        -Their coordinates on the grid
        -Their next coordinates (destination)
        -Possibly their age and a "fragility coeffiient" given the version"""
    def __init__(self, nId, grade, etat, position, destination, tempsMalade, tempsEcole, tempsHorsEcole):
        self.nId = nId
        self.grade = grade 
        self.etat = etat
        self.position =position
        self.destination = destination
        self.tempsMalade = tempsMalade
        self.tempsEcole = tempsEcole
        self.tempsHorsEcole = tempsHorsEcole
    
#--------------------------Génération d'individus:-----------------------------
nTot = 4000

#Nombre de chaque type:

def resetEtats(nM):
    nS = nTot - nM
    Etats2=[]
    for i in range (nS):
        Etats2.append('Sain')
    for i in range (nM):
        Etats2.append('Malade')
    if nS + nM != nTot :
        print("erreur de proportions")
    return(Etats2)
    
#Nombre de chaque Grade:

nP=3120
nE=880
    
if nE + nP != nTot :
    print("error in the proportions") 

#Création:
"""Firt, random objects are created and stored in a list. They are numbered from 1 to nTot"""
def nvlObj(nTot):
    Objs=[]
    for i in range (nTot):
        Objs.append(i+1)
    return(Objs)
    
"""Now a generated is created on each of these objects"""

def setPersonne(nTot, nM): 
    """Rerturns the object lists and a list of their attributes"""
    Pers=[]
    Pers=nvlObj(nTot)
    Etats = resetEtats(nM)
    M=[]
    for i in range (nTot):
        Pers[i]= personne(setId(i), setGrade(i), setEtat(i,Etats), setPosition(i,n), setDestination(i,n), 0, 0, 0)
        Pers[i].tempsMalade = setTempsMalade(Pers,i)
        M.append((Pers[i].nId,Pers[i].grade, Pers[i].etat, Pers[i].position, Pers[i].destination, Pers[i].tempsMalade, Pers[i].tempsEcole, Pers[i].tempsHorsEcole))
    return(Pers,M)
    
def getLastPersonnes():
    global Pers
    return(Pers)
def showAttributs(personne):
    Attributs = (personne.nId,personne.grade, personne.etat, personne.position, personne.destination, personne.tempsMalade, personne.tempsEcole)
    return(Attributs)
def setId(i):
    L=nvlObj(nTot)
    return(L[i])
    
def setGrade(i):
    if i+1<= nE:
        return("Enfant")
    elif i+1> nE:
        return("Adulte")
     
def setEtat(i, Etats):
    a=random.choice(Etats)
    Etats.remove(a)
    return(a)

def setTempsMalade(L,i):
    if L[i].etat == 'Malade':
        return(1)
    elif L[i].etat == 'Sain' :
        return(0)
#def addTempsEcole(personne):
#    if personne.position == (70,70) and personne.grade == 'Enfant' :
#        personne.tempsEcole += 1
#def addTempsHorsEcole(personne):
#    if personne.position != (70,70) and personne.grade == 'Enfant' :
#        personne.tempsHorsEcole += 1

        
    

"""WARNING, for the positions and destination coordinates, the first component refers to the vertical axis and the second one for the horizontal axis (as in a matrix)"""
     
def setPosition(i,n):   
    ligne=random.randint(0,n-1)
    colonne=random.randint(0,n-1)
    Pos=[ligne,colonne]
    return(Pos)
    
def setDestination(i,n):
    ligne=random.randint(0,n-1)
    colonne=random.randint(0,n-1)
    Dest=[ligne,colonne]
    return(Dest)

def getPersonne(personne):
    L=[personne.nId, personne.grade, personne.etat, personne.position, personne.destination]
    return(L)


    