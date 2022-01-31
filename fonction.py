"""
def permutation (s): 
    """"""
    permut_table = []
    for i in range(1, len(s)):
        s[0], s[1] = s[1], s[0]
        permut_table.append(s)
        s[2], s[3] = s[3], s[2]
        permut_table.append(s)
  
        s[6], s[7] = s[7], s[6]
        permut_table.append(s)
    
    return permut_table
        
"""
import random

def  permutation (s):
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
    #print(permut_table)#print(" On peut avoir la liste : {}" .format(a),"avec un conflit  valant : {}".format(conflits(a)))
    return permut_table          
    

def conflits (s):
    
   # taille = len(str(s))
    #print(s)
    compteur = 0
    
    for i in range(1, 8):
        for j in range(1, 8):
            if i != j :
                
                if s[i] == s[j]:
                    compteur += 1
                
                
    for i in range(1, 8):
        for j in range(1, 8):
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