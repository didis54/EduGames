#-------------------------------------------------------------------------------
# Name:        ang_1.py
# Purpose:     Jeu du Pendu Anglais
#
# Author:      Loris
#
# Created:     29/04/2016
# Copyright:   © Copyright Loris
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from tkinter import*
from random import*
import Matter
from configparser import*
import os.path as file

global partie_en_cours, mot_partiel, mot_choisi, nb_echecs, lettre_ds_mot,bouton, bravo, image_pendu, canevas, lettres, listes, afficher_mot, fenetre, bt_supp, init_jeu
fichier = open("listes_ang.txt", "r")
listes = fichier.readlines()    # met tous les mots du fichier dans une liste
fichier.close()
bt_supp = []
cfg = ConfigParser()
name = ""

def lettre_ds_mot(lettre):
    """Vérifie si la lettre est dans le mot, si oui elle est placé au bon endroit"""
    global partie_en_cours, mot_partiel, mot_choisi, nb_echecs, image_pendu, bouton, bravo, bt_supp
    if partie_en_cours:
        nouveau_mot_partiel = "" # Vide la variable
        lettre_ds_mot = False
        i = 0 # remet i à zero
        while i<len(mot_choisi): # Tant que i est inferieur à la taille du mot, effectue le programme dans l'indentation ci dessous.
            if mot_choisi[i]==lettre:
                nouveau_mot_partiel = nouveau_mot_partiel + lettre # Ajoute a la variable la lettre choisi par lutilisateur
                lettre_ds_mot = True
            else:
                nouveau_mot_partiel = nouveau_mot_partiel + mot_partiel[i]
            i+=1 # Rajoute 1 à i puis retourne au début du while
        mot_partiel = nouveau_mot_partiel
        afficher_mot(mot_partiel) # Affiche le mot avec la lettre trouver
        bouton[ord(lettre)-65].pack_forget() # Supprime chaque lettre utilisé
        bt_supp.append(ord(lettre)-65) # Ajoute a la fin de la liste le contenu du append
        if mot_partiel == mot_choisi: # le mot à été trouvé
            partie_en_cours = False
            canevas.itemconfig(bravo,text="Bravo !") # affiche bravo
            partie_gagne = int(cfg.get(name, "ang_gagne")) + 1
            cfg.set(name, "ang_gagne", str(partie_gagne))
            cfg.write(open("profils.cfg", 'w'))
        else:
            pass
    if not lettre_ds_mot:   # lettre fausse. Changer le dessin.
        nb_echecs += 1
        nomFichier = "images/ang/pendu_"+str(nb_echecs)+".gif"
        photo = PhotoImage(file = nomFichier)
        image_pendu.config(image = photo)
        image_pendu.image = photo
        if nb_echecs == 7:  # trop d'erreurs fin du jeu
            partie_en_cours = False
            afficher_mot(mot_choisi)
            for i in range(26):
                if i in bt_supp: # si i est dans la liste OK
                    pass
                else:
                    bouton[i].pack_forget() # Si pas dans la liste supprimer
            bt_supp = []
            partie_perdu = int(cfg.get(name, "ang_perdu")) + 1
            cfg.set(name, "ang_perdu", str(partie_perdu))
            cfg.write(open("profils.cfg", 'w'))
        elif mot_partiel == mot_choisi: # le mot à été trouvé
            partie_en_cours = False
            canevas.itemconfig(bravo,text="Bravo !")
            for i in range(26):
                if i in bt_supp: # si i est dans la liste OK
                    pass
                else:
                    bouton[i].pack_forget() # Si pas dans la liste supprimer
            bt_supp = []

def afficher_mot(mot):
    """Remplace le mot choisi par des tirets, et par les lettres trouvées """
    global lettres
    mot_large = "" # vide la variable
    i = 0
    while i<len(mot):   # ajoute un espace entre les lettres
        mot_large = mot_large + mot[i] + " " # Contient la portion de mot trouver par l'utiliseur et mise en forme pour l'afficher sur la fenetre
        i+=1
    canevas.delete(lettres) # Supprime l'ancien mot_partiel puis le remplace par le mot complet
    lettres = canevas.create_text(320, 60, text = mot_large, fill = 'black', font = 'Courrier 30') # Ecrit la lettre

def init_jeu():
    """ initialise toutes les variables globales avant de commencer ( ou recommencer ) la partie"""
    global mot_choisi, mot_partiel, lettres, nb_echecs, partie_en_cours, listes, bouton, bravo, bt_supp, fenetre
    if bt_supp != []: # Si un bouton est different de ceux dans la listes
        for i in range(26):
            if i in bt_supp: # si i est dans la liste OK
                pass
            else:
                bouton[i].pack_forget() # Si pas dans la liste supprimer
            bt_supp = []
    for i in range(26): # Crée les boutons
        bouton[i] = Button(fenetre, text = chr(i+65), command = lambda x = i+65:lettre_ds_mot(chr(x))) # Exectuer des fonctions comportant des parametre
        bouton[i].pack(side = LEFT)
    nb_echecs = 0 # met le nbr dechecs de base
    partie_en_cours = True
    mot_choisi = choice(listes).rstrip() # choisit un mot au hasard
    mot_choisi = mot_choisi.upper() # Met en majuscule
    mot_partiel = "-" * len(mot_choisi) # remplace les lettres par des tirets
    afficher_mot(mot_partiel)
    photo = PhotoImage(file = "images/ang/pendu_0.gif") # met limage de base
    image_pendu.config(image = photo)
    image_pendu.image = photo
    canevas.itemconfig(bravo,text="") # Met du texte vide ( remplacer par Bravo si gagner )

def recommencer():
     """ recommence la partie en supprimant les boutons restants """
     for i in range(26):
        bouton[i].pack_forget()
     init_jeu()

def fermeture(profilName):
    """ retourne sur lecran de selection des jeux """
    fenetre.destroy()
    Matter.open(profilName)

def openFrame(profilName):
    global name
    name = profilName
    cfg.read("profils.cfg")
    if "ang_gagne" in cfg.options(profilName) and "ang_perdu" in cfg.options(profilName):
        pass
    else:
        cfg.set(profilName, "ang_gagne", '0')
        cfg.set(profilName, "ang_perdu", '0')
        cfg.write(open("profils.cfg", 'w'))

    global fenetre, bouton, canevas, lettres, image_pendu, bravo, photo
    fenetre = Tk()
    fenetre.title("The Hanged Man")
    fenetre.wm_iconbitmap("images/EduGames_logo.ico")

    canevas = Canvas(fenetre, bg = 'white', height = 500, width = 620)
    canevas.pack(side = BOTTOM)

    bouton = [0]*26

    bouton2 = Button(fenetre, text = 'Retour', command = lambda:fermeture(profilName))
    bouton2.pack(side = RIGHT)
    bouton1 = Button(fenetre, text = 'Recommencer', command = recommencer)
    bouton1.pack(side = RIGHT)

    photo = PhotoImage(file = "images/ang/pendu_0.gif")
    image_pendu = Label(canevas, image=photo, border = 0)
    image_pendu.place(x = 120, y = 140)
    lettres = canevas.create_text(320, 60, text = "", fill = 'black', font = 'Courrier 30')
    bravo = canevas.create_text(320,110,text="",fill='red',font='Courrier 40')

    init_jeu()
    fenetre.mainloop()