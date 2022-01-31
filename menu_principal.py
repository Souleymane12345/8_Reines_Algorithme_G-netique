
############## DABONE SOULEYMANE #####################

import random
from math import *
from fonction import permutation
from fonction import conflits
from fonction import minimum






def principal_function (s):
    tabouTable = []
    tabouTable.append(s)

    while conflits(s) != 0 :
        
        sVoisin = permutation(s)
        
        """"""
        sCandidate = minimum(sVoisin)
        print(f"La liste candidate est : {sCandidate} avec un conflit  valant : {conflits(sCandidate)}")
        if sCandidate not in tabouTable:
            s = sCandidate
            
            
        tabouTable.append(s)

        
        """"""
        for deleteTabou in tabouTable:
            
            if conflits(deleteTabou) < conflits(s):
                tabouTable.remove(deleteTabou)
                print(f"La liste {deleteTabou} vient d'être supprimer de  la liste des Tabou.")
                
        
        print(f"La liste de tabou compte {len(tabouTable)} listes qui sont {tabouTable}")
        
        #print(tabouTable)
       
    return s
        
            
        

def generer_liste ():
    randomlist = random.sample(range(1, 9), 8)
   
    #randomlist = [randrange(10) for i in range(8)]
    return randomlist


table = generer_liste()

#""""""
#table = [4, 7, 5, 2, 3, 1, 6, 1]
#table = [7, 4, 2, 3, 1, 5, 6, 8]

print(f"Notre liste de départ est : {table} avec un conflit  valant : {conflits(table)}")

resultat_finals = principal_function(table)

print(f"Notre liste de final est : {resultat_finals} avec un conflit  valant : {conflits(resultat_finals)}")
"""

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
 import numpy
 
def nbroccurences (grille,chiffre,i,j) :
    imini = i - (i%3)
    jmini = j - (j%3)
    compteur=0
    if grille[i][j]==chiffre:
        compteur = -3      #on ne compte pas wij
     
    for k in range (0,9) : #compte pour i donné (colonne)
        if grille[i][k] == chiffre :
            compteur = compteur +1
             
    for k in range (0,9): #compte pour j donné (ligne)
        if grille [k][j] == chiffre :
            compteur = compteur + 1
             
    for k in range(imini, imini+3): #compte dans la sous-grille
        for z in range(jmini, jmini +3) :
            if grille[k][z] == chiffre :
                compteur = compteur +1
             
    return compteur
 
def fonctioneconomique (w):#score
    a = 0
    for i in range (0,9):
        for j in range (0,9):
            a = a + nbroccurences(w,w[i][j],i,j) #formule du polycopié
     
    return 0.5*a
 
 
 
def recuitsimule(w):
    
    delta=0.1
    ep=810
    T=ep
    i=random.randint(0,8)
    j=random.randint(0,8)
    grille=creerGrille(9,9)
     
    L=[] #liste des indices des chiffres a ne pas modifier
    for u in range (0,9):
        for v in range (0,9):
            if w[u][v]!=0:
                L.append([u,v])
            grille[u][v]=w[u][v]
             
             
    while [i,j]  in L: #on crée un voisinage
        i=random.randint(0,8)
    grille[i][j] = random.randint(1,9)
   
    c= fonctioneconomique(grille)
     
    while T>0.002:
        for k in range(81):
             
         
         
            d = random.randint(0,8)
            b=random.randint(0,8)
         
            while [d,b] in L:  #choix de la case à modifier
                d = random.randint(0,8)
                b=random.randint(0,8)
                 
             
        
                 
                 
            t=grille[d][b] #valeur initiale
     
            cun=nbroccurences(grille,grille[d][b],d,b)
         
            grille[d][b] = random.randint(1,9) #on modifie le chiffre en i,j
            while grille[d][b]==t:    
                grille[d][b]=random.randint(1,9)
         
        
            cdeux=nbroccurences(grille,grille[d][b],d,b)
                 
            cprime = c-cun+cdeux #c(wprime)
             
            u=random.random()
            a=numpy.exp((-(cprime-c)/T))
             
            if cprime == 0: #si résolu
                h=grille
                return (h,cprime)
                 
            elif  u <= a: #si cdeux < cun alors exp() >1 ==> (wprime est mieux que w)
                c=cprime
                    
            else : #on recupère la valeur initiale
                grille[d][b]= t
            print (T,c)  
        T= T / (1 + (numpy.log(1+delta)/(ep+1))*T)
        
    return grille,f
             
def creerGrille(nombreLignes, nombreColonnes):
    grid = [[]] * nombreLignes
    for ligne in range(nombreLignes):
        grid[ligne] = [0] * nombreColonnes
    return grid   
 
""
"