
############## DABONE SOULEYMANE #####################

import random
from math import *
from random import randrange
from fonction import permutation
from fonction import conflits
from fonction import minimum
from fonction import prob





def principal_function (s , t , e , cool ):
    #print(s,t,e,cool)
    while (t > e) :
    #while (conflits(s) != 0) :
        tabs = permutation(s)
        if conflits(s) == 0:     
           break
        #print(tabs)
        a = minimum(tabs)
        #a = random.choice(tabs)
        #print(a)
        conf = conflits(a) - conflits(s)
        print(conf,conflits(a),conflits(s))
        if conf <= 0:
                #print("okkkkkkkkkk")
            s = a
        else: 
            r = random.uniform(0, 1)
            div = -conf/t
            expo = exp(div)
            if r < expo :
                s = a
                print(s)
        t = t * cool
        print("t:",t)
        #print(s,resultat_final)
        #principal_function (resultat_final , t , e , cool )
        
    return s
        
            
        

def generer_liste ():
    randomlist = random.sample(range(1, 9), 8)
   
    #randomlist = [randrange(10) for i in range(8)]
    return randomlist


#table = generer_liste()
#print(table)
""""""
table = [7, 4, 2, 3, 1, 5, 6, 8]
nb = 1000
cool1 = 0.95
tables = table
alpha = 0.01

print(" Notre liste de départ est : {}" .format(table),"avec un conflit  valant : {}".format(conflits(table)))

resultat_finals = principal_function(tables,nb,alpha,cool1)

print(" Notre liste de final est : {}" .format(resultat_finals),"avec un conflit  valant : {}".format(conflits(resultat_finals)))







        
"""  
        for sCandidate in sVoisin:
            
            if (sCandidate not in tabouTable) and (conflits(sCandidate) < conflits(sSelection)):
                sSelection = sCandidate
                 
        if conflits(sCandidate) <= conflits(sSelection):
            print("ok")
            s = sCandidate
"""