# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import tkinter as tk
#import math
import numpy as np
import time
import random


root = tk.Tk()
root.title("PARCOURS DES GRAPHES")

canvas = tk.Canvas(root, width=800, height=800, bg="white")
canvas.pack(side=tk.LEFT)

#variables globales
global monChoix
monChoix=""
global listeSA
listeSA = []
#---------------------------------------------AFFICHAGE GRAPHIQUE--------------------------------------------------------------
#dessine une grille de fond
def draw_grille(canvas, width, height, nombre):
    for i in range(nombre):
        position=width/(nombre+1)*(i+1)
        canvas.create_line((position,0),(position,height),fill="gray",width=2, dash=(5,5))
        canvas.create_text(position,10,text=str(int(position)),font= ("courier", 10, "bold italic"), anchor="center", justify= "center")
        canvas.create_line((0,position),(width,position),fill="gray",width=2, dash=(5,5))
        canvas.create_text(10,position,text=str(int(position)),font= ("courier", 10, "bold italic"), anchor="center", justify= "center")

#dessine les sommets
def draw_vertex(canvas, x, y, rayon, couleur, label):
    x0 = x-rayon
    x1 = x+rayon
    y0 = y-rayon
    y1 = y+rayon
    canvas.create_oval (x0,y0,x1,y1, fill=couleur, outline="black", width=3)
    canvas.create_text((x,y),text= label, fill= "black", font= ("courier",20, "bold italic"), anchor="center", justify= "center")

#dessine les arêtes     
def draw_arc(canvas, xd, yd, xa, ya):
    canvas.create_line(xd, yd, xa, ya, fill = "black", width=3)

#dessine le graphe  
def afficheGraphe(canvas,graphe):
    global coordonnées
    coordonnées = {}
    
    #calcul des coordonnées de chaque sommet
    coordonnées = {"R1":[50, 450],"R2":[200, 250],"R3":[350,50],"R4":[200,700],"R5":[350,450],
             "R6":[500,250],"R7":[500,700],"R8":[600,450],"R9":[750,250],"R10":[750,700]}
    
    '''
    i=0
    for clé in graphe.keys():
        pas_angulaire = 2*math.pi/len(graphe)
        angle = i*pas_angulaire - math.pi/2
        x = int(300*math.cos(angle) +400)
        y = int(300*math.sin(angle) +400)
        coordonnées.update({clé:[x,y]})
        i = i+1
    '''
    
    
    #dessin des arêtes
    for clé in graphe.keys():     
        voisin = True
        indice = 0 
        antecedent = clé
        successeur = graphe[clé]
        debutArc = coordonnées[antecedent]      
        while (voisin):     
            finArc = coordonnées[successeur[indice]]
            draw_arc(canvas, debutArc[0], debutArc[1], finArc[0], finArc[1])
            indice = indice+1
            if(indice > len(successeur)-1):
                voisin = False
  
    #dessin des sommets par dessus les arêtes
    for clé in graphe.keys():
        antecedent = clé
        debutArc = coordonnées[antecedent]
        draw_vertex(canvas, debutArc[0], debutArc[1],30,"yellow", clé)    

#coloration en rouge des sommets parcourus
def parcoursSommets(noeudsVisite, couleur):
    for noeud in noeudsVisite:
        antecedent = noeud
        debutArc = coordonnées[antecedent]
        draw_vertex(canvas, debutArc[0], debutArc[1],30,couleur, noeud) 
        root.update()
        time.sleep(1.5)    
#ferme une fenêtre
#def choix():   
    #monChoix = v.get()
#    pass

def choixParcours():
    monChoix = v.get()
    if(monChoix=="BFS"):
        noeudsVisite = {}
        noeudsVisite = bfs(mongraphe,"R1")
        parcoursSommets(noeudsVisite, "red")
        print(bfs(mongraphe,"R1"))

    elif(monChoix=="DFS"):
        noeudsVisite = {}
        noeudsVisite = dfs(mongraphe,"R1")
        parcoursSommets(noeudsVisite, "blue")
        print(dfs(mongraphe,"R1"))  
        
    elif(monChoix=="RANDOM"):
        nombreNoeuds = 10
        premier = "R1"
        randomWalk(mongraphe,premier,nombreNoeuds)
        parcoursSommets(listeSA, "green")
        
    elif(monChoix=="DIJMAT"):
        nombreNoeuds = 10
        noeudsParcours = dijkstraCheminMatrice(M, I, S)
        parcoursSommets(noeudsParcours, "purple")
        
    elif(monChoix=="DIJLIST"):
        nombreNoeuds = 10
        noeudsParcours = dijkstraCheminListe(G, sdeb, sfin)
        parcoursSommets(noeudsParcours, "wheat3")
        
    
#----------------------------------------------ALGORITHMES--------------------------------------------------------                 
#parcours en profondeur        
def dfs(graphe, debut):
    visite, pile = {}, [debut]
    while pile:
        noeud = pile.pop()
        visite[noeud] = True
        for voisin in graphe[noeud]:
            if voisin not in visite:
                pile.append(voisin)
    return visite 
 
#parcours en largeur
def bfs(graphe, debut):
    visite, pile = {}, [debut]
    while pile:
        noeud = pile.pop(0)
        visite[noeud] = True
        for voisin in graphe[noeud]:
            if voisin not in visite:
                pile.append(voisin)
    return visite

#parcours aléatoire
def randomWalk(graphe,u,n):
    if n== 0:
        w=u
    elif graphe[u]==[]:
        w=u
    else :
        print(u)
        listeSA.append(u)
        w=randomWalk(graphe,random.choice(graphe[u]),n-1)
        return w
    
#plus court chemin dijkstra dictionnaire----------------------------------------------------------------------

def dijkstraCheminListe(graphe, sdeb, sfin):

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
    
    def dijkstraDict(graphe, sdeb):
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
    
    def cheminDict(L, sdeb, sfin):
        A = []
        while(sfin != sdeb):
           A.append(sfin)
           sfin = L[0][sfin]
        A.append(sdeb)
        A.reverse()
        print(A)
        return A
    
    P = cheminDict(dijkstraDict(graphe, sdeb), sdeb, sfin)
    return P
#______________________________________________________________________________________________

#plus court chemin dijkstra matrice d'adjacence------------------------------------------------
def dijkstraCheminMatrice(M, I, S):
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
            
    def DijkstraMatrice(M, I):
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
    
    def CheminMatrice(D, S):
        #recherche du chemin du sommet I vers le sommet S
        Parcours = [S]
        prec = D[S][1]
        while prec is not None:
            Parcours.append(prec)
            prec = D[prec][1] 
        Parcours.reverse()
        return Parcours
    
    P = CheminMatrice(DijkstraMatrice(M, I), S) 
    listeSommets = ['R1', 'R2', 'R3', 'R4', 'R5','R6','R7','R8','R9','R10']
    Sparcourus = []
    for i in P:
        Sparcourus.append(listeSommets[i])
        
    return Sparcourus
#____________________________________________________________________________________________________

#-----------------------------------------PROGRAMME PRINCIPAL-----------------------------------------------------------------------------------------------

# Saisie du graphe

mongraphe = {"R1":["R2","R4"],"R2":["R1","R3","R5","R6"],"R3":["R2","R6"],"R4":["R1","R5","R7"],"R5":["R2","R4","R5","R7"],
             "R6":["R2","R3","R5","R9"],"R7":["R4","R5","R8"],"R8":["R5","R7","R9","R10"],"R9":["R6","R8"],"R10":["R8"]}

G = {'R1':{'R2':10, 'R4':8}, 'R2':{'R1':10, 'R3':5, 'R5':7, 'R6':6}, 'R3':{'R2':5, 'R6':4}, 'R4':{'R1':8, 'R5':3, 'R7':2}, 'R5':{'R2':7, 'R4':3, 'R6':9, 'R7':1, 'R8':4},'R6':{'R2':6, 'R3':4, 'R5':9, 'R9':5},'R7':{'R4':2, 'R5':1, 'R8':9},'R8':{'R5':7,'R7':9,'R9':4,'R10':1},'R9':{'R6':5,'R8':4},'R10':{'R8':1} }

sdeb = 'R1'
sfin = 'R10'
I = 0
S = 9
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


#Affichage du graphe
draw_grille(canvas,800,800,15)
afficheGraphe(canvas,mongraphe)

#choix algorithme

v = tk.StringVar()
tk.Label(root, text="Choisir un parcours graphe", justify = tk.LEFT, padx = 20).pack()
tk.Radiobutton(root, text="PARCOURS EN LARGEUR", padx = 20, variable=v, value="BFS").pack(anchor=tk.W)
tk.Radiobutton(root, text="PARCOURS EN PROFONDEUR", padx = 20, variable=v, value="DFS").pack(anchor=tk.W)
tk.Radiobutton(root, text="PARCOURS ALEATOIRE", padx = 20, variable=v, value="RANDOM").pack(anchor=tk.W)
tk.Radiobutton(root, text="PARCOURS DIJKSTRA MATRICE", padx = 20, variable=v, value="DIJMAT").pack(anchor=tk.W)
tk.Radiobutton(root, text="PARCOURS DIJKSTRA LISTE", padx = 20, variable=v, value="DIJLIST").pack(anchor=tk.W)
tk.Button(root, text="VALIDER", command=choixParcours, padx=20, pady=10).pack()

# RESET  utilisation de la fonction lambda pour commander avec un bouton une fonction avec paramètres
tk.Button(root, text="RESET", command=lambda:afficheGraphe(canvas,mongraphe), padx=20, pady=10).pack()


root.mainloop()
