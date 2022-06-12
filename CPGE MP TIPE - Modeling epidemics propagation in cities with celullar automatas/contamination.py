import random
from Objets import *

#--------------------------------Contamination---------------------------------

pmin = 0.1
pmax = 0.2

#----------------------------------Mortalité-----------------------------------

"""Starting the study with the ebola rates """
TauxMortalite = 0
TauxImmunite = 1 - TauxMortalite
TempsIncubationMax = 7*24
TempsExpoMax = 8*24

#---------------------------------DEBUT ALGO-----------------------------------

#compteurMalades = nM
compteurMorts = 0
compteurImmunises= 0
Personnes = M
AttributsPersonnes= Pers


"""Is the cell going to be be contaminated """    
def variables(nM):
    global compteurMalades, compteurMorts, compteurImmunises
    compteurMalades, compteurMorts, compteurImmunises = nM, 0, 0
    
def contaminer(Personnes,pC):
    global compteurMorts
    global compteurImmunises
    global compteurMalades
    L=Personnes
    nombre = len(L)
    if nombre != 0:
        nbr = compteMalades(L) + comptePorteursSains(L)
#        proportion = (compteMalades(L) + comptePorteursSains(L)-1)/nombre
        for i in range (len(L)):
            if L[i].etat == 'Malade' or L[i].etat == 'Porteur Sain':
                L[i].tempsMalade +=1 
            
            elif L[i].etat == 'Sain':
                """ we remove 1 because we want the minimum  probabiliity to be equal to pmin.
                    Also, as the function is runned only if compteMalades >0 there is no negative probability problem"""
                tirage = random.randint(1,1000)
                if tirage <= 1000*pC:
#                    print('contamination')
                    L[i].etat = 'Porteur Sain'
                    L[i].tempsMalade =1
                    nouveauMalade()

def evolution(Personnes):
    L=Personnes
    global compteurMorts
    global compteurImmunises
    global compteurMalades
    if L != [] :    
        longueur = len(L)
        for i in range (longueur):
            if len(L)>i:
                tirage = random.randint(1,100)
#                print(showAttributs(L[i]))
                if L[i].etat == 'Porteur Sain':
                    if tirage <= probaMalade(L[i].tempsMalade):
                        L[i].etat = 'Malade'
                        L[i].tempsMalade = 0
                elif L[i].etat == 'Malade':
                    if tirage <= probaIssue(L[i].tempsMalade):
                        tirage2 = random.randint(1,10)
                        if tirage2<=3:
#                            print('immunise')
                            L[i].etat = 'Immunise'
                            compteurImmunises+=1
#                            print('Imunnise', compteurImmunises)
                        else:
#                            print('mort')
                            L[i].etat = 'Mort'
                            compteurMorts +=1
#                            print('mort', compteurMorts)
                            L.pop(i)
                            longueur = longueur -1
                        
def printvar():
    return(compteurMalades, compteurImmunises, compteurMorts)
                    
            
def probaIssue(t):
    proba = ((t/TempsExpoMax)**2)*100
    return(proba)
           

def probaMalade(t):
    proba = ((t/TempsIncubationMax)**2)*100
    return(proba)
    
def resetCompteurs(nM):
    global compteurMalades
    global compteurMorts
    global compteurImmunises
    compteurImmunises = 0
    compteurMorts = 0
    compteurMalades = nM

def nouveauMalade():
    global compteurMalades
    compteurMalades +=1

"""Number of contaminated peoples per cell"""
def compteMalades(L):
    nbr = 0
    for i in range (len(L)):
        if L[i].etat == 'Malade':
            nbr +=1
    return(nbr)
def comptePorteursSains(L):
    nbr=0
    for i in range (len(L)):
        if L[i].etat == 'Porteur Sain':
            nbr +=1
    return(nbr)