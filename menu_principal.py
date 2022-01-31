
############## DABONE SOULEYMANE #####################

import random
from random import randrange
from fonction import permutation
from fonction import conflits
from fonction import minimum


def principal_function (s):
    
    sVoisin = permutation(s)

    sCandidate = minimum(sVoisin)
    
    if conflits(sCandidate) <= conflits(s):
        #print("okkkkkkkkkk")
        resultat_final = sCandidate
    
       
    if   s == resultat_final :
        return resultat_final
    else:
        print(" Utilisons une nouvelle liste : {}" .format(resultat_final),"avec un conflit  valant : {}".format(conflits(resultat_final)))
        #print("okkkkkkkkkkk")
        resultat_final = principal_function(resultat_final)
        
        return resultat_final
    
        
        

def generer_liste ():
    #randomlist = random.sample(range(1, 9), 8)
   
    randomlist = [randrange(10) for i in range(8)]
    return randomlist


#table = generer_liste()
table = [7, 4, 2, 3, 1, 5, 6, 8]

print(" Notre liste de départ est : {}" .format(table),"avec un conflit  valant : {}".format(conflits(table)))

resultat_finals = principal_function(table)

print(" Notre liste de final est : {}" .format(resultat_finals),"avec un conflit  valant : {}".format(conflits(resultat_finals)))
