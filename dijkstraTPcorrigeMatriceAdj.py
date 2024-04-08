#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:06:38 2020

@author: perrot
"""

import numpy as np

def Voisins(M, S):
    #renvoie la listes des voisins d'un sommet
    L= []
    for i in range(len(M)):
        if M[S][i] != 0:
            L.append(i)
    return L

def indicesommetdmin(V, D):
    #renvoie l'indice du sommet à distance de V
    dmin = min([D[i][0] for i in V])
    for i in V:
        if D[i][0] == dmin:
            return i
        
def Dijkstra(M, I):
    #initialisation
    E = []
    V = [I]
    D = [[np.inf, None] for i in range(len(M))] #initialisation du tableau des distances
    D[I][0] = 0
    
    #Recherche des plus courts chemins
    while len(V) >0 :
        S = indicesommetdmin(V, D)
        V.remove(S)
        E.append(S) #sommets déjà explorés
        for VP in Voisins(M, S):
            if VP not in E:
                V.append(VP)
                if D[VP][0] > D[S][0] + M[S][VP]:
                    D[VP] = [D[S][0] + M[S][VP], S]
    return D

def Chemin(D, S):
    #recherche du chemin du sommet I vers le sommet S
    Parcours = [S]
    prec = D[S][1]
    while prec is not None:
        Parcours.append(prec)
        prec = D[prec][1] 
    Parcours.reverse()
    return Parcours

M = [[0,10,0,8,0,0,0,0,0,0],
     [10,0,5,0,7,6,0,0,0,0],
     [0,5,0,0,0,0,0,0,0,0],
     [8,0,0,0,3,0,2,0,0,0],
     [0,7,0,3,0,9,1,4,0,0],
     [0,6,0,0,9,0,0,0,5,0],
     [0,0,0,2,1,0,0,9,0,0],
     [0,0,0,0,4,0,9,0,4,1],
     [0,0,0,0,0,5,0,4,0,0],
     [0,0,0,0,0,0,0,1,0,0]]

I = 0

print(Dijkstra(M, I))

print(Chemin(Dijkstra(M, I),9))
