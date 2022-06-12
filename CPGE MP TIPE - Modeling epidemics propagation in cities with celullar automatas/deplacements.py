from Objets import setPersonne
from Grille import initGrille
from Grille import getTaille

import random
n= getTaille()

#---------------------------------Placements-----------------------------------
grille = initGrille(n)

def placement(Liste):
#    Liste=setPersonne(nTot,Etats)[0]
    x , y = 0 , 0
    while len(Liste) > 0 :
        x , y = Liste[0].position[0] , Liste[0].position[1]
        p = Liste.pop(0)
        grille[x][y].append(p)
    return(grille)
    
#-------------------------------Déplacements-----------------------------------
""" Retuns the moving vector for a given person. Oriented towards its next position but normalized"""
def vecteurDeplacement(grille,i,j,p):
    Dhorizontal = grille[i][j][p].destination[1] - grille[i][j][p].position[1]    
    Dvertical = grille[i][j][p].destination[0] - grille[i][j][p].position[0]
    if Dvertical == 0:
        Vvertical = 0
    else :
        Vvertical = Dvertical/(abs(Dvertical))
    if Dhorizontal == 0:
        Vhorizontal = 0
    else :
        Vhorizontal = Dhorizontal/(abs(Dhorizontal))
    return(int(Vvertical),int(Vhorizontal))
    
"""Moving all people according to their moving vetor, but by 1 unit only"""
def deplacement(grille):
    nouvellegrille = initGrille(n)
    for j in range (n):
        for i in range(n):
            for p in range (len(grille[i][j])):
                if (grille[i][j][p].position[0] , grille[i][j][p].position[1]) == (grille[i][j][p].destination[0] , grille[i][j][p].destination[1]):
                    grille[i][j][p].destination[0] = random.randint(0,n-1)
                    grille[i][j][p].destination[1] = random.randint(0,n-1)
                    nouvellegrille[i][j].append(grille[i][j][p])
                else:
                    h = vecteurDeplacement(grille,i,j,p)[0]
                    l = vecteurDeplacement(grille,i,j,p)[1]
                    grille[i][j][p].position[0] = grille[i][j][p].position[0] + h
                    grille[i][j][p].position[1] = grille[i][j][p].position[1] + l                    
                    nouvellegrille[i+h][j+l].append(grille[i][j][p])

    return(nouvellegrille)
