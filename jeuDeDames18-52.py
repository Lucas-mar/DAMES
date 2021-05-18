# coding: utf-8

import os
try : import pygame; from pygame.locals import *
except : 
    print("INSTALLATION DE PIP")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try : os.system("sudo python3 "+dir_path+"/get-pip.py")
    except : pass
    print("INSTALLATION DE SETUPTOOLS")
    try : os.system("sudo pip3 install setuptools")
    except : pass
    print("INSTALLATION DE PYGAME")
    try : os.system("sudo pip3 install pygame")
    except : pass

    import pygame
    from pygame.locals import *
    print("LANCEMENT DU JEU")

import time
import os
from random import randint as nombre_random



#On cree une "classe" pion, c'est comme une grosse variable avec plusieurs sous variables, a l'image des tableaux
class pion :

    #On initialise la classe avec les donnees entree, ainsi que self qui permet de definir les attributs "interieur" a la classe
    def __init__(self, joueur, couleur, position_x, position_y) :
        self.joueur = joueur #maClasse.joueur = joueur / pion.joueur = joueur
        if couleur == "bleu" : self.couleur = (0,0,255) #couleur en rgb
        elif couleur == "rouge" : self.couleur = (255,0,0)
        else : self.couleur = (0,255,0)
        self.position = (position_x, position_y) #Postion actuelle du pion
        self.type = "pion" #Savoir si le pion est une dame ou un pion simple


#---------------------------------------------------------------------------------


def afficher_texte(fenetre, texte, ratio_w, ratio_h, screen_w, screen_h, action = ["return", -1]) :

    #On definie une classe "texte" pour recuperer les valeurs dans le menu principal, pour savoir sur quel texte on clique
    class Texte :
        def __init__(self,x,y,w,h) :
            #On definie un "carre" avec (x,y) le point en haut a gauche, (max_x,max_y) le point en bas a droite
            self.x = x
            self.y = y
            self.max_x = x+w
            self.max_y = y+h
            self.action = action


    #On definie la police d'ecriture ainsi que sa taille avec la variable font, on calcule sa taille avec font.size(TEXTE)
    font = pygame.font.Font(None, 24)
    w_font, h_font = font.size(texte)
    texte = font.render(texte,1,(0,0,0))

    #On calcule la postiion du texte avec les donnees en entree et w_font/h_font, ce qui nous premettra de detecter le clic sur le texte
    x = screen_w*ratio_w-w_font//2
    y = screen_h*ratio_h-h_font//2
    fenetre.blit(texte, (x,y))

    return(Texte(x, y, w_font, h_font)) #On retourne la classe avec les coordonnees du texte


#---------------------------------------


def afficher_commandes(fenetre, w, h) :
    #On dessine un fond blanc   
    pygame.draw.rect(fenetre, (255,255,255), (0,0,w,h),0)

    position_texte = {}
    position_texte["COMMANDES"] = afficher_texte(fenetre, "COMMANDES", 0.5, 0.2, h, h)
    position_texte["Les deplacements se font a la souris"] = afficher_texte(fenetre, "Les deplacements se font a la souris", 0.5, 0.35, h, h)
    position_texte["Touche ECHAP : Entrer/Quitter le menu principal"] = afficher_texte(fenetre, "Touche ECHAP : Entrer/Quitter le menu principal", 0.5, 0.45, h, h)

    pygame.display.flip()

    time.sleep(3)



#---------------------------------------


def menu_principal(fenetre, w, h, partie=0) :

    #On importe les variables globales
    global jeu
    global continuer
    global rapidite

    #On dessine un fond blanc
    pygame.draw.rect(fenetre, (255,255,255), (0,0,w,h),0)

    if not(partie) :
        #On ecrit les differents elements et on recupere la classe retournee dans un dictionnaire grace a la fonction afficher_texte()
        position_texte = {}
        position_texte["MENU PRINCIPAL"] = afficher_texte(fenetre, "MENU PRINCIPAL", 0.5, 0.2, h, h)
        position_texte["1 Joueur - IA Naive"] = afficher_texte(fenetre, "1 Joueur - IA Naive", 0.5, 0.4, h, h, ["return", 1])
        position_texte["1 Joueur - IA Guidee"] = afficher_texte(fenetre, "1 Joueur - IA Guidee", 0.5, 0.45, h, h, ["return", 2])
        position_texte["2 Joueurs"] = afficher_texte(fenetre, "2 Joueurs", 0.5, 0.5, h, h, ["return", 0])
        position_texte["IA Guidee vs IA Naive"] = afficher_texte(fenetre, "IA Guidee vs IA Naive", 0.5, 0.55, h, h, ["return", 4])
        position_texte["Commandes"] = afficher_texte(fenetre, "Commandes", 0.5, 0.60, h, h, ["afficher_commandes(fenetre, w, h)", "return", -1])
        position_texte["Rapidite IA :"] = afficher_texte(fenetre, "Rapidite IA :", 0.43, 0.65, h, h)
        position_texte["1"] = afficher_texte(fenetre, "1", 0.53, 0.65, h, h, ["rapidite", 1])
        position_texte["2"] = afficher_texte(fenetre, "2", 0.57, 0.65, h, h, ["rapidite", 2])
        position_texte["3"] = afficher_texte(fenetre, "3", 0.61, 0.65, h, h, ["rapidite", 3])
        position_texte["Quitter"] = afficher_texte(fenetre, "Quitter", 0.5, 0.7, h, h, ["exit"])
        position_texte["Fait par Lucas Marsalle"] = afficher_texte(fenetre, "Fait par Lucas Marsalle", 0.8,0.95,h,h)
    
    else :
        position_texte = {}
        position_texte["MENU PAUSE"] = afficher_texte(fenetre, "MENU PAUSE", 0.5, 0.2, h, h)
        position_texte["Reprendre la partie"] = afficher_texte(fenetre, "Reprendre la partie", 0.5, 0.35, h, h, ["return", -1])
        position_texte["Commandes"] = afficher_texte(fenetre, "Commandes", 0.5, 0.40, h, h, ["afficher_commandes(fenetre, w, h)", "return", -1])
        position_texte["Quitter"] = afficher_texte(fenetre, "Quitter", 0.5, 0.7, h, h, ["exit"])
        position_texte["Fait par Lucas Marsalle"] = afficher_texte(fenetre, "Fait par Lucas Marsalle", 0.8,0.95,h,h)
    


    #On rafraichi l'affichage
    pygame.display.flip()

    #On cree une boucle pour recuperer les differentes entrees souris/clavier
    capturer_action = 1

    while capturer_action :
        for event in pygame.event.get() :
            if event.type == MOUSEBUTTONDOWN :
                x,y = event.pos[0], event.pos[1]
                #On lis toutes les classes presentent dans position_texte pour voir si le clic souris correspond a l'une d'elles et on execute l'action de Texte.action
                for texte in list(position_texte.keys()) :
                    if (position_texte[texte].x <= x <= position_texte[texte].max_x) and (position_texte[texte].y <= y <= position_texte[texte].max_y) :
                        action = position_texte[texte].action
                        for i in range(len(action)) :
                            if action[i] == "return" :
                                return(action[i+1])
                            elif action[i] == "rapidite" :
                                rapidite = action[i+1]
                                return(-1)
                            elif action[i] == "exit" :
                                exit()
            if partie :
                if event.type == KEYDOWN and event.key == K_ESCAPE :
                    capturer_action=0
            if event.type == QUIT :
                quit()



#---------------------------------------

#Fonction qui va se charger d'afficher le cradrillage du jeu de dame
def table_jeu(fenetre, tab, square) :
    for y,i in enumerate(tab) : #tab = map du cadrillage
        for x,j in enumerate(i) : # enumerate sert a enumerer les valeurs dans la liste pointee, x prend les valeurs 0,1,2 etc...
            if j == "1" : pygame.draw.rect(fenetre, (0,0,0), (square*x, square*y, square*x+square, square*y+square), 0) #1 correspond a une case noire, 0 a une case blanche
            elif j == "2" : pygame.draw.rect(fenetre,(150,128,128), (square*x, square*y, square*x+square, square*y+square), 0) #2 correspond a une case en surbrillance quand on clique sur un pion
            else : pygame.draw.rect(fenetre, (255,255,255), (square*x, square*y, square*x+square, square*y+square), 0) #pygame.draw.rect -> dessine un rectangle


#---------------------------------------

#Fonction qui sert a afficher les pions a l'ecran
def init_pions(fenetre, en_cour) :

    #On importe les variables globales
    global tab 
    global pions_joueur1
    global pions_joueur1
    global position_pions_joueur1
    global position_pions_joueur2
    global square
    global rayon_pion


    #Si la partie debute
    if en_cour == "debut" :

        #Parametrage et affichage des pions du joueur 1
        for y in range(len(tab)-1,6,-1) : #On parcours le tableau de la map et si une case est egale a 1, on met un pion dessus, 1=case noire
            for x in range(len(tab[y])) :
                if tab[y][x] == "1" : position_pions_joueur1.append((x,y))#On ajoute les positions dans un tableau

        for position in position_pions_joueur1 :
            pions_joueur1.append(pion("joueur1", "rouge", position[0], position[1])) #On cree les pions a l'aide de la classe pion
        for i in pions_joueur1 :
            pygame.draw.circle(fenetre, i.couleur, (i.position[0]*square+rayon_pion,i.position[1]*square+rayon_pion), rayon_pion-10, 0) #On dessine les pions a l'ecran

        #Parametrage et affichage des pions du joueur 2, meme procedure pour le joueur 1
        for y,i in enumerate(tab) : # enumerate sert a enumerer les valeurs dans la liste pointee, y prend les valeurs 0,1,2 etc...
            if y > 2 : break
            for x,j in enumerate(i) :
                if j == "1" : position_pions_joueur2.append((x,y))

        for position in position_pions_joueur2 :
            pions_joueur2.append(pion("joueur2", "bleu", position[0], position[1]))
        for i in pions_joueur2 :
            pygame.draw.circle(fenetre, i.couleur, (i.position[0]*square+rayon_pion,i.position[1]*square+rayon_pion), rayon_pion-10, 0)


    #Si la partie est deja en cours
    else :

        #Placement pions joueur 1
        for i in pions_joueur1 :
            if i.position[1] == 0 : i.type = "dame" #Si le pion atteind le camp adverse, il devient une dame

            if i.type == "pion" : 
                #On dessine les pions a l'ecran en se basant sur les pions crees en debut de partie qui ont etes mis a jour par la suite
            	pygame.draw.circle(fenetre, i.couleur, (i.position[0]*square+rayon_pion,i.position[1]*square+rayon_pion), rayon_pion-10, 0)
            else :
                pygame.draw.circle(fenetre, i.couleur, (i.position[0]*square+rayon_pion,i.position[1]*square+rayon_pion), rayon_pion-10, 0)
                pygame.draw.circle(fenetre, (0,0,0), (i.position[0]*square+rayon_pion,i.position[1]*square+rayon_pion), (rayon_pion-10)//2, 0)

        #Placement pions joueur 2
        for i in pions_joueur2 :
            if i.position[1] == 9 : i.type = "dame"; #Si le pion atteind le camp adverse, il devient une dame

            if i.type == "pion" : 
                #On dessine les pions a l'ecran en se basant sur les pions crees en debut de partie qui ont etes mis a jour par la suite
            	pygame.draw.circle(fenetre, i.couleur, (i.position[0]*square+rayon_pion,i.position[1]*square+rayon_pion), rayon_pion-10, 0)
            else :
                pygame.draw.circle(fenetre, i.couleur, (i.position[0]*square+rayon_pion,i.position[1]*square+rayon_pion), rayon_pion-10, 0)
                pygame.draw.circle(fenetre, (0,0,0), (i.position[0]*square+rayon_pion,i.position[1]*square+rayon_pion), (rayon_pion-10)//2, 0)


#---------------------------------------

#Fonction qui scanne tous les pions de l'equipe aliee et qui definie quel pion doit manger ou non, ainsi que ses deplacements
def doit_manger_fonction(pions_joueur_alie, pions_joueur_ennemi, position_pions_joueur_alie, position_pions_joueur_ennemi) :

    #On importe les variables globales
    global joueur
    global tab
    global rayon_pion

    pions_doivent_manger = {} # {} : definie un dictionnaire, exemple : mon_dictionnaire = {"nom1" : valeur1, "nom2" : valeur2}, print(mon_dictionnaire["nom1"]) -> valeur1
    pions_deplacements = {}
    var_doit_manger = 0
    for pions in pions_joueur_alie :
        doit_manger = 0
        position_manger = []
        deplacements_possibles = []
        position_x, position_y = pions.position #pions.position est un attribut de la classe pion, dans lequel est stocke la position sous forme de tuple : (x,y)

        if (1==1) : #Est un pion classique
            
            #En utilisant ces deux tableaux dans une boucle for on obtient tous les deplacements possible, en haut à doite/gauche -> (y-1,x+1)/(y-1,x-1), en bas à doite/gauche -> (y+1,x+1)/(y+1,x-1)
            tableau_deplacements_x = [-1,+1,-1,+1]
            tableau_deplacements_y = [-1,-1,+1,+1]

            for i in range(4) :
                deplacement_x, deplacement_y = tableau_deplacements_x[i], tableau_deplacements_y[i]
                position = ((position_x+deplacement_x),(position_y+deplacement_y))
                position_pour_manger = ((position_x+deplacement_x*2),(position_y+deplacement_y*2))
                if (position in position_pions_joueur_ennemi) :
                    if (position_pour_manger not in position_pions_joueur_alie and position_pour_manger not in position_pions_joueur_ennemi) and (0<=position_pour_manger[0]<10 and 0<=position_pour_manger[1]<10) :
                        doit_manger = 1
                        position_manger.append(position_pour_manger)
                else :
                    if (deplacement_y == -1) and (position not in position_pions_joueur_alie) and (0<=position[0]<10 and 0<=position[1]<10) and (joueur == 1 or pions.type == "dame") :
                        deplacements_possibles.append(position)
                    elif (deplacement_y == +1) and (position not in position_pions_joueur_alie) and (0<=position[0]<10 and 0<=position[1]<10) and (joueur == 2 or pions.type == "dame") :
                        deplacements_possibles.append(position)

        #Si un des pions doit manger, on initialise la variable var_doit_manger a 1, celle ci ne changera pas, on ajoute ensuite les posisions pour manger dans le dictionnaire pions_doivent_manger avec comme nom de cle la position acutelle du pions
        if doit_manger :
            pions_doivent_manger[pions.position] = position_manger
            var_doit_manger = 1
        
        #Sinon on ajoute les deplacements possible au dictionnaire pions_deplacements avec comme cle la position actuelle du pion
        else :
            if deplacements_possibles != [] : #On teste si deplacements_possibles n'est pas vide pour ne pas mettre de pions qui ne peuvent pas se deplacer dans le dictionnaire
                pions_deplacements[pions.position] = deplacements_possibles

    if var_doit_manger : 
        pions_deplacements = pions_doivent_manger
        
    return(var_doit_manger, pions_deplacements, pions_joueur_alie, pions_joueur_ennemi, position_pions_joueur_alie, position_pions_joueur_ennemi)


#---------------------------------------


def IA_Naive(doit_manger, pions_deplacements) :

    time.sleep(0.5/rapidite) #Pause de 0.5 seconde pour permettre au joueur de voir le deplacement

    #IA qui fonctionne totalement aleatoirement en choisissant des deplacements aleatoires et des pions aleatoire. Mange un pion quand elle doit manger.
    position_hasard = [i for i in pions_deplacements.keys()][nombre_random(0, len(pions_deplacements.keys())-1)]
    deplacement_hasard = pions_deplacements[position_hasard][nombre_random(0,len(pions_deplacements[position_hasard])-1)]

    return(position_hasard, deplacement_hasard)        


#---------------------------------------


def IA_Predictive(doit_manger, pions_deplacements, pions_joueur_alie, pions_joueur_ennemi, position_pions_joueur_alie = 0, position_pions_joueur_ennemi = 0) :

	global deplacement_IA2

	time.sleep(0.5/rapidite)
    #time.sleep(0.5) #Pause de 0.5 seconde pour permettre au joueur de voir le deplacement

    #IA qui mange aleatoirement mais qui predit un coup a l'avance, si elle se fera manger ou non avec tel ou tel deplacement

	global fenetre
	global square
	global tab
	position_pion = 0
	while position_pion < len(list(pions_deplacements.keys())) :
	    for deplacement in pions_deplacements[list(pions_deplacements.keys())[position_pion]] :
	        position_hasard, deplacement_hasard = list(pions_deplacements.keys())[position_pion], deplacement
	        position_pions_joueur_alie_copie = []
	        for i in position_pions_joueur_alie :
	            position_pions_joueur_alie_copie.append(i)
	        pions_joueur_alie_copie = []
	        for i in pions_joueur_alie :
	            pions_joueur_alie_copie.append(pion(i.joueur, i.couleur, i.position[0], i.position[1]))
            
	        pion_actuel = position_pions_joueur_alie_copie.index(list(pions_deplacements.keys())[position_pion])
	        x, y = list(pions_deplacements.keys())[position_pion]
	        x_new, y_new = deplacement
	        pions_joueur_alie_copie[pion_actuel].position = ((x_new, y_new))
	        position_pions_joueur_alie_copie[pion_actuel] = ((x_new, y_new))				
	        if not((doit_manger_fonction(pions_joueur_ennemi, pions_joueur_alie_copie, position_pions_joueur_ennemi, position_pions_joueur_alie_copie))[0]) :
	            return((x,y), (x_new, y_new))
	    position_pion += 1

	return(position_hasard, deplacement_hasard) 


#---------------------------------------


def tour_joueur(pions_joueur_alie, pions_joueur_ennemi, position_pions_joueur_alie, position_pions_joueur_ennemi, pions_doivent_manger = 0):
	#Global pour acceder a une variable du programme, hors de la fonction
    global tab
    global fenetre
    global joueur
    global rayon_pion
    global IA
    global IA2
    global w,h
    global continuer

    
    #On teste si un pion doit manger un autre
    if not(pions_doivent_manger) :
    	doit_manger, pions_deplacements, pions_joueur_alie, pions_joueur_ennemi, position_pions_joueur_alie, position_pions_joueur_ennemi = doit_manger_fonction(pions_joueur_alie, pions_joueur_ennemi, position_pions_joueur_alie, position_pions_joueur_ennemi)
    else : 
    	doit_manger = 1
    	pions_deplacements = pions_doivent_manger
    #On teste si au moins un deplacement est possible, sinon on renvoie des tableaux vides et l'autre joueur a donc gagne
    if not(doit_manger) and len(pions_deplacements) == 0 :
        return([],pions_joueur_ennemi,[],position_pions_joueur_ennemi)

    table_jeu(fenetre, tab, square)
    init_pions(fenetre, "partie")

    x,y = -1,-1

    if ((joueur == 1 and IA2) or (joueur == 2 and IA)) :
        if (joueur == 1 and IA2 == 2) or (joueur == 2 and IA == 2) :
            position_hasard, deplacement_hasard = IA_Predictive(doit_manger, pions_deplacements, pions_joueur_alie, pions_joueur_ennemi, position_pions_joueur_alie, position_pions_joueur_ennemi)
        
        if joueur == 2 and IA == 1 :
            position_hasard, deplacement_hasard = IA_Naive(doit_manger, pions_deplacements)

        pion_actuel = position_pions_joueur_alie.index(position_hasard)
        x, y = position_hasard
        x_new, y_new = deplacement_hasard

    else :
        while (x,y) not in pions_deplacements :
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN :
                    (x,y) = (event.pos[0]//square), (event.pos[1]//square)
                if event.type == KEYDOWN and event.key == K_ESCAPE :
                    menu_principal(fenetre, w, h, 1)
                    table_jeu(fenetre, tab, square)
                    init_pions(fenetre, "partie")
                    pygame.display.flip()

        tab[y][x] = "2"
        table_jeu(fenetre, tab, square)
        init_pions(fenetre, "partie")
        pygame.display.flip()

        pion_actuel = position_pions_joueur_alie.index((x,y))
        manger = 1
        x_new, y_new = -1,-1
        while (x_new, y_new) not in pions_deplacements[(x,y)] :
                for event in pygame.event.get() :
                    if event.type == MOUSEBUTTONDOWN :
                        x_new, y_new = (event.pos[0]//square), (event.pos[1]//square)
                    if event.type == KEYDOWN and event.key == K_ESCAPE :
                        menu_principal(fenetre, w, h, 1)
                        table_jeu(fenetre, tab, square)
                        init_pions(fenetre, "partie")
                        pygame.display.flip()
        
        tab[y][x] = "1"
        table_jeu(fenetre, tab, square)
        init_pions(fenetre, "partie")
        pygame.display.flip()


    if doit_manger :
        pion_a_manger = position_pions_joueur_ennemi.index(((x+x_new)//2, (y+y_new)//2))
        del position_pions_joueur_ennemi[pion_a_manger]
        del pions_joueur_ennemi[pion_a_manger]
    
    pions_joueur_alie[pion_actuel].position = ((x_new, y_new))
    position_pions_joueur_alie[pion_actuel] = ((x_new, y_new))
    table_jeu(fenetre, tab, square)
    init_pions(fenetre, "partie")
    pygame.display.flip()

    if doit_manger :
        pions_deplacements = doit_manger_fonction([pions_joueur_alie[pion_actuel]], pions_joueur_ennemi, position_pions_joueur_alie, position_pions_joueur_ennemi)[1]
        doit_manger = doit_manger_fonction([pions_joueur_alie[pion_actuel]], pions_joueur_ennemi, position_pions_joueur_alie, position_pions_joueur_ennemi)[0]
        if (doit_manger) and (pions_joueur_alie[pion_actuel].position in pions_deplacements) :
            for i in pions_deplacements.keys() :
                if i != pions_joueur_alie[pion_actuel].position :
                    del pions_deplacements[i]
            tour_joueur(pions_joueur_alie, pions_joueur_ennemi, position_pions_joueur_alie, position_pions_joueur_ennemi, pions_deplacements)

        
    
    return(pions_joueur_alie, pions_joueur_ennemi, position_pions_joueur_alie, position_pions_joueur_ennemi)

#---------------------------------------

def fin_partie(fenetre, joueur_gagnant, w, h) :
    pygame.draw.rect(fenetre, (255,255,255), (0,0,w,h), 0) #Fond blanc
    font=pygame.font.Font(None, 24)
    texte_a_afficher = joueur_gagnant + " a gagne !"
    text = font.render(texte_a_afficher,1,(0,0,0))
    w_font, h_font = font.size(texte_a_afficher)
    fenetre.blit(text, (w//2-w_font, h//2-h_font))
    pygame.display.flip()

#---------------------------------------------------------------------------------



w,h = 800,600 #taille ecran
square = h//10 #taille d'une case du jeu de dame (10*10 cases)
pygame.init()
fenetre = pygame.display.set_mode((h,h))
rapidite = 1
deplacement_IA2 = []

jeu = 1
while jeu :
    continuer = 1
    IA = -1
    while IA == -1 :
    	IA = menu_principal(fenetre, h, h)
    IA2 = 0
    if IA == 4 :
    	IA2 = 2
    	IA = 1

    tab = [] #map carte
    position_pions_joueur1 = [] #tableau de tuples pour les positions
    position_pions_joueur2 = []

    pions_joueur1 = [] #stocke des variable de type class (pion)
    pions_joueur2 = []
    rayon_pion = (square//2) #rayon du pion pour le dessiner


    for i in range(10) :
        tab.append([])
        if i%2==0 :
            for j in range (5) :
                tab[i].append("0")
                tab[i].append("1")
        else : 
            for j in range (5) :
                tab[i].append("1")
                tab[i].append("0")


    table_jeu(fenetre, tab, square)
    init_pions(fenetre, "debut")


    pygame.display.flip()
    joueur = 1
    
    while continuer :
        if joueur == 1 : #Tour au joueur 1
            pions_joueur1, pions_joueur2, position_pions_joueur1, position_pions_joueur2 = tour_joueur(pions_joueur1, pions_joueur2, position_pions_joueur1, position_pions_joueur2, 0)
            joueur = 2
        
        elif joueur == 2 : #Tour au joueur 2
            pions_joueur2, pions_joueur1, position_pions_joueur2, position_pions_joueur1 = tour_joueur(pions_joueur2, pions_joueur1, position_pions_joueur2, position_pions_joueur1, 0)
            joueur = 1


        if not(pions_joueur1) : 
            continuer = 0
            fin_partie(fenetre, "Joueur 2", w, h)
            time.sleep(3)
        if not(pions_joueur2) :
        	continuer = 0
        	fin_partie(fenetre, "Joueur 1", w, h)
        	time.sleep(3)