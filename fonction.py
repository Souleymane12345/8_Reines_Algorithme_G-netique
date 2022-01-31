
import random
from math import *

def  genererPopulation (s):
    s1 = s[:]
    #print("s1",s1)
    permut_table = []
    for k in range(1, len(s1)): 
        for i in range(1, len(s1)):
            for j in range(1, len(s1)):
                if s1[i] == s1[j]:
                    if i != j:
                        c = [0,1,2,3,4,5,6,7]
                        b = random.choice(c)
                        s1[j], s1[b] = s1[b], s1[j]
                        permut_table.append(s1)
                        s1 = s[:]
                else:
                    d = [0,1,2,3,4,5,6,7]
                    b = random.choice(d)
                    s1[j], s1[b] = s1[b], s1[j]
                    permut_table.append(s1)
                    s1 = s[:]
    #print(permut_table)
    return permut_table          


def conflits (s):
    
    compteur = 0
    
    for i in range(0, 8):
        for j in range(0, 8):
            if i != j :         
                if s[i] == s[j]:
                    compteur += 1
                               
    for i in range(0, 8):
        for j in range(0, 8):
            if i != j :
               if abs( s[i] - s[j]) == abs (i - j):
                   compteur += 1
                        
    return compteur

 
    
def minimum(tab):
    tabmin = [6, 6, 6, 4, 1, 2, 1, 2]
    
    for i in range(1, len(tab)):
        #print(tab[i],conflits(tab[i]))
        if conflits(tab[i]) <= conflits(tabmin):
            tabmin = tab[i]

    #print (tabmin,conflits(tabmin))
    return tabmin

def selectionNaturel (tab1):
    tab = tab1[0:250]
    l = len(tab)
    t = []
    for i in range(0,l-1):

        fitness = conflits(tab[i]) - conflits(tab[i+1]) 
        if fitness > 0:
            t = tab[i]
            tab[i] = tab[i+1]
            tab[i+1] = t
            #print("tab",tab)
    return tab[0:100]
              
"""
def selectionParents(tab):
    tabA, tabB = [],[]
    proCroise = random.random()
    if proCroise >= 0.6: 
        tabA,tabB  = minimum(tab)
    else:
        selectionParents(tab) 
    return tabA, tabB
"""  
def generationEnfant(parent):
    i=0
    probCrois = 0
    probMut = 0
    listNouvelleGeneration = []
    while i < 5000:
        a = random.randint(0, 20)
        b = random.randint(0,20)
        probCrois = random.uniform(0, 1)
        if probCrois > 0.6 :
            enfant = croisement(parent[a],parent[b])
            #print(f"a {a} {b} , enfant {enfant}"
            # )
            probMut = random.uniform(0, 1)
            if probMut > 0.2 :
                enfantMuter = mutation(enfant)
                listNouvelleGeneration.append(enfantMuter)
            
        i = i+1
        
    listNouvelleGenerationFinal = [] 
    for i in listNouvelleGeneration : 
        if i not in listNouvelleGenerationFinal: 
            listNouvelleGenerationFinal.append(i) 
    #print("listNouvelleGeneration",listNouvelleGeneration)
        
    return listNouvelleGenerationFinal
    
    
def croisement(tab1, tab2):
    tabcrois ,tabcrois = [],[]
    tabcrois = tab1[0:3]+tab2[3:]
    #tabcrois1 = tab2[0:3]+tab2[3:]
    return tabcrois
    
def mutation(tab):
    tabDepart = [1,2,3,4,5,6,7,8]
    tabElement = []
    tab1 = tab 
    tabNettoyer = []
    for i in tabDepart:
        if i not in tab1:
            tabElement.append(i)
    for i in tab1:
        if i not in tabNettoyer:
            tabNettoyer.append(i)
        else :
            tabNettoyer.append(tabElement[0])
            tabElement.pop(0)
    tabFinal = []
    return tabNettoyer
        
    
    