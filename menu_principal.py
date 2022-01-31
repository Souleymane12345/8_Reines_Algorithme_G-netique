
############## DABONE SOULEYMANE #####################

import random
from math import *
from fonction import genererPopulation
from fonction import conflits
from fonction import minimum
from fonction import selectionNaturel
from fonction import generationEnfant







def principal_function (s):

    population = []
    meilleursIndividus = []
    nouvelleGeneration = []
    population = genererPopulation(s)
    print("La taille de la population initiale est :",len(population))
    k=0
    while conflits(s) != 0  and k<25:
        
        k+=1
        meilleursIndividus = selectionNaturel(population)
        print(f"La liste des meilleurs individus de la {k} ième génération est : {meilleursIndividus} de taille {len(meilleursIndividus)}")
        nouvelleGeneration = generationEnfant(meilleursIndividus)
        print(f"La liste de la population à la  {k} ième génération est : {nouvelleGeneration} de taille {len(meilleursIndividus)} ")
        s = minimum(nouvelleGeneration)
        print(f"Le meilleur du  individu de la population à la  {k} ième génération est : {s} avec un conflit valant : {conflits(s)}")
        population.clear()
        population = nouvelleGeneration

       
    return s,k
        
            
        

def generer_liste ():
    randomlist = random.sample(range(1, 9), 8)
    return randomlist


table = generer_liste()

""""""
print(f"Notre liste de départ est : {table} avec un conflit  valant : {conflits(table)}")

resultat_finals, generation = principal_function(table)

print(f"Notre liste de final est : {resultat_finals} avec un conflit  valant : {conflits(resultat_finals)}. Elle est trouvée à la {generation} ième génération.")
