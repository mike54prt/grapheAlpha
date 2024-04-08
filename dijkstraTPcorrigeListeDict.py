#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 09:28:36 2020

@author: perrot
"""

#--------------------------ALGORITHME DE DIJKSTRA-----------------------------------------------------
# liste d'adjacence avec les poids : 
import numpy as np

#Initialisation
def initialisation(graphe, sdeb):
   d = {}  
   for noeud in graphe:
       d[noeud]= np.inf #infini
   d[sdeb]=0
   return d

def distanceMini(d, Q): 
     minimum = np.inf  #infini
     sommet = ""
     for s in Q:
         if (d[s] < minimum):
             minimum = d[s]
             sommet = s
     s1 = sommet  
     return s1

def dijkstra(graphe, sdeb):
   d = initialisation(graphe, sdeb)
   predecesseur = {}
   Q = [sdeb]
   E = []
   while (not(not Q)):          # liste non vide
     #trouvez la distance mini
     s1 = distanceMini(d, Q)
     Q.remove(s1) 
     E.append(s1)
     #mise à jour des distances
     for s2 in list(graphe[s1].keys()):
         if s2 not in E:
             Q.append(s2)
             #mise à jour des distances
             if (d[s2] > d[s1] + graphe[s1][s2]):
                 d[s2] = d[s1] + graphe[s1][s2]
                 predecesseur[s2]=s1

   #retourne les predecesseurs et les distances
   return predecesseur, d

#G = {'R1':{'R2':10, 'R4':8}, 'R2':{ 'R3':5, 'R5':7, 'R6':6}, 'R3':{ 'R6':4}, 'R4':{'R5':3, 'R7':2}, 'R5':{'R2':7, 'R4':3, 'R6':9, 'R7':1, 'R8':4},'R6':{'R5':9, 'R9':5},'R7':{ 'R5':1, 'R8':9},'R8':{'R9':4,'R10':1},'R9':{'R6':5,'R8':4},'R10':{'R8':1} }

G = {'R1':{'R2':10, 'R4':8}, 'R2':{'R1':10, 'R3':5, 'R5':7, 'R6':6}, 'R3':{'R2':5, 'R6':4}, 'R4':{'R1':8, 'R5':3, 'R7':2}, 'R5':{'R2':7, 'R4':3, 'R6':9, 'R7':1, 'R8':4},'R6':{'R2':6, 'R3':4, 'R5':9, 'R9':5},'R7':{'R4':2, 'R5':1, 'R8':9},'R8':{'R5':7,'R7':9,'R9':4,'R10':1},'R9':{'R6':5,'R8':4},'R10':{'R8':1} }

sdeb = 'R1'
sfin = 'R10'
print(dijkstra(G,sdeb))
print("")
L = dijkstra(G,sdeb)
A = []
while(sfin != sdeb):
    A.append(sfin)
    sfin = L[0][sfin]
A.append(sdeb)
A.reverse()
print(A)