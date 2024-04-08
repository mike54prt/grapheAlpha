#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 09:28:36 2020

@author: perrot
"""

#--------------------------ALGORITHME DE DIJKSTRA-----------------------------------------------------
# liste d'adjacence avec les poids : 


#Initialisation

def dijkstra(graphe, sdeb):
   #Initialisation
   predecesseur = {}
   d = {}
   Q = []
   for noeud in graphe:
       d[noeud]= 10000000 #infini
       d[sdeb]=0
       Q.append(noeud)
   
   #dijkstra
   while (not(not Q)):          # liste non vide
     #trouvez la distance mini
     minimum = 100000000  #infini
     sommet = ""
     for s in Q:
         if (d[s] < minimum):
             minimum = d[s]
             sommet = s
     s1 = sommet
     Q.pop(0)
     
     #mise à jour des distances
     for s2 in list(graphe[s1].keys()):
         #mise à jour des distances
         if (d[s2] > d[s1] + graphe[s1][s2]):
             d[s2] = d[s1] + graphe[s1][s2]
             predecesseur[s2]=s1

   #retourne les predecesseurs
   return predecesseur, d

G = {'s':{'u':10, 'x':5}, 'u':{'v':1, 'x':2}, 'v':{'y':4}, 'x':{'u':3, 'v':9, 'y':2}, 'y':{'s':7, 'v':6}}
sdeb = 's'
sfin = 'v'
print(dijkstra(G,sdeb))
L = dijkstra(G,sdeb)
A = []
while(sfin != sdeb):
    A.append(sfin)
    sfin = L[0][sfin]
A.reverse()
print(A)