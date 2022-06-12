from Grille import *
from Objets import *
from deplacements import *
from contamination import *
import xlrd
import xlwt
from xlutils.copy import copy
Temps =250
"""Time table in hours  (24 = 1 day   720 = 1 month)"""
grille = initGrille(n)

#Personnes = setPersonne(nTot,nM)
ListePersonnes = getLastPersonnes()


#print(ListeAttributsersonnes)

def SimExcel():
    fichier =  xlrd.open_workbook('simulation.xls')
    f1= fichier.sheet_by_name('Sheet 1')
    NbrM = f1.col_values(0)
    PropM =  f1.col_values(1)
    ProbaC = f1.col_values(2)
    Mal=0
    Imm=0
    Mor=0
    copie = copy(fichier)
    for ligne in range(1,3):
        nbM=int(NbrM[ligne])
        prC=float(ProbaC[ligne])
        print(nbM,prC)
        Mal, Imm, Mor = lancerSimulation(nbM,prC)
        
        s = copie.get_sheet(0)
        s.write(ligne,3,Mal)
        s.write(ligne,4,Imm)
        s.write(ligne,5,Mor)
    copie.save('simulation.xls')

def SimExcel2():
    fichier =  xlrd.open_workbook('simulation2.xls')
    f1= fichier.sheet_by_name('Sheet 1')
    NbrM = f1.col_values(0)
    PropM =  f1.col_values(1)
    ProbaC = f1.col_values(2)
    Mal=0
    Imm=0
    Mor=0
    copie = copy(fichier)
    for ligne in range(1,3):
        nbM=int(NbrM[ligne])
        prC=float(ProbaC[ligne])
        print(nbM,prC)
        Mal, Imm, Mor = lancerSimulation2(nbM,prC)
        s = copie.get_sheet(0)
        s.write(ligne,3,Mal)
        s.write(ligne,4,Imm)
        s.write(ligne,5,Mor)
    copie.save('simulation2.xls')

def test():

    fichier = xlrd.open_workbook("simulation.xls")
    copie = copy(fichier)
    s = copie.get_sheet(1)
    s.write(0,2,'test')
    copie.save('simulation.xls')
        

def lancerSimulation(nM,pC):
    grille = initGrille(n)
    print(grille)
    variables(nM)
    global compteurMorts
    global compteurImmunises
    global compteurMalades
    ListePersonnes = []
    ListePersonnes = setPersonne(nTot,nM)[0]
    compteurMalades, compteurImmunises, compteurMorts = nM, 0, 0
    grille = placement(ListePersonnes)
    print(grille)
    for temps in range (Temps):
        compteurMalades, compteurImmunises, compteurMorts = 0, 0, 0
        grille = deplacement(grille)
        for i in range (n):
            for j in range (n):
                if (compteMalades(grille[i][j]) + comptePorteursSains(grille[i][j])) >0:                    
                    contaminer(grille[i][j],pC)
                    evolution(grille[i][j])
        compteurMalades, compteurImmunises, compteurMorts = printvar()
#        print(compteurMalades,'Malades ',compteurImmunises, 'Immunisés ', compteurMorts,'Morts')
    print('Results:', compteurMalades,'Malades ',compteurImmunises, 'Immunisés ', compteurMorts,'Morts')    
    return(compteurMalades,compteurImmunises,compteurMorts)
 

def lancerSimulation2(nM,pC):

    variables(nM)
    global compteurMorts
    global compteurImmunises
    global compteurMalades
    ListePersonnes = setPersonne(nTot,nM)[0]
    compteurMalades, compteurImmunises, compteurMorts = nM, 0, 0
    grille = placement(ListePersonnes)
    for i in range(n):
        for j in range(n):
            for p in range(len(grille[i][j])):
                grille[i][j][p].tempsEcole = 0
                grille[i][j][p].tempsHorsEcole = 0
    for temps in range (Temps):
        compteurMalades, compteurImmunises, compteurMorts = 0, 0, 0
        grille = deplacementOriente(grille)
        for i in range (n):
            for j in range (n):
                if (compteMalades(grille[i][j]) + comptePorteursSains(grille[i][j])) >0:                    
                    contaminer(grille[i][j],pC)
                    evolution(grille[i][j])
        compteurMalades, compteurImmunises, compteurMorts = printvar()
#        print(compteurMalades,'Malades ',compteurImmunises, 'Immunisés ', compteurMorts,'Morts')
    print('Results:', compteurMalades,'Malades ',compteurImmunises, 'Immunisés ', compteurMorts,'Morts')    
    return(compteurMalades,compteurImmunises,compteurMorts)


















    
#def tester():
#    
#    ListePersonnes = setPersonne(nTot,Etats)[0]
#    print(ListePersonnes)
#    grille = placement(ListePersonnes)
#    print(grille)
#    for temps in range(Temps):
#        grille = deplacement(grille)
#        print(grille)

def showGrille():
    return(grille)



