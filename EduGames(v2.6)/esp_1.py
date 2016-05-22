# Créé par lhenrion3, le 29/04/2016 en Python 3.2

from tkinter import*
from random import*
from Matter import*

global partie_en_cours, mot_partiel, mot_choisi, nb_echecs, lettre_ds_mot,bouton, bravo, image_pendu, canevas, lettres, listes, afficher_mot, fenetre, bt_supp, init_jeu
fichier = open("listes_esp.txt", "r")
listes = fichier.readlines()    # met tous les mots du fichier dans une liste
fichier.close()
bt_supp = []
cfg = ConfigParser()
name = ""

def lettre_ds_mot(lettre):
    global partie_en_cours, mot_partiel, mot_choisi, nb_echecs, image_pendu, bouton, bravo, bt_supp
    if partie_en_cours:
        nouveau_mot_partiel = ""
        lettre_ds_mot = False
        i = 0
        while i<len(mot_choisi):
            if mot_choisi[i]==lettre:
                nouveau_mot_partiel = nouveau_mot_partiel + lettre
                lettre_ds_mot = True
            else:
                nouveau_mot_partiel = nouveau_mot_partiel + mot_partiel[i]
            i+=1
        mot_partiel = nouveau_mot_partiel
        afficher_mot(mot_partiel)
        bouton[ord(lettre)-65].pack_forget() #effacer bouton utiliser pack_forget()
        bt_supp.append(ord(lettre)-65)
        if mot_partiel == mot_choisi: # le mot à été trouvé
            partie_en_cours = False
            canevas.itemconfig(bravo,text="¡Enhorabuena!")
            partie_gagne = int(cfg.get(name, "esp_gagne")) + 1
            cfg.set(name, "esp_gagne", str(partie_gagne))
            cfg.write(open("profils.cfg", 'w'))
        else:
            pass
    if not lettre_ds_mot:   # lettre fausse. Changer le dessin.
        nb_echecs += 1
        nomFichier = "images/esp/pendu_"+str(nb_echecs)+".gif"
        photo = PhotoImage(file = nomFichier)
        image_pendu.config(image = photo)
        image_pendu.image = photo
        if nb_echecs == 7:  # trop d'erreurs. Fini.
            partie_en_cours = False
            afficher_mot(mot_choisi)
            for i in range(26):
                if i in bt_supp:
                    pass
                else:
                    bouton[i].pack_forget()
            bt_supp = []
            partie_perdu = int(cfg.get(name, "esp_perdu")) + 1
            cfg.set(name, "esp_perdu", str(partie_perdu))
            cfg.write(open("profils.cfg", 'w'))
        elif mot_partiel == mot_choisi: # le mot à été trouvé
            partie_en_cours = False
            canevas.itemconfig(bravo,text="¡Enhorabuena!")
            for i in range(26):
                if i in bt_supp:
                    pass
                else:
                    bouton[i].pack_forget()
            bt_supp = []

def afficher_mot(mot):
    global lettres
    mot_large = ""
    i = 0
    while i<len(mot):   # ajoute un espace entre les lettres
        mot_large = mot_large + mot[i] + " "
        i+=1
    canevas.delete(lettres)
    lettres = canevas.create_text(320, 60, text = mot_large, fill = 'black', font = 'Courrier 30')

def init_jeu():
    global mot_choisi, mot_partiel, lettres, nb_echecs, partie_en_cours, listes, bouton, bravo, bt_supp, fenetre
    if bt_supp != []:
        for i in range(26):
            if i in bt_supp:
                pass
            else:
                bouton[i].pack_forget()
            bt_supp = []
    for i in range(26):
        bouton[i] = Button(fenetre, text = chr(i+65), command = lambda x = i+65:lettre_ds_mot(chr(x)))
        bouton[i].pack(side = LEFT)
    nb_echecs = 0
    partie_en_cours = True
    mot_choisi = choice(listes).rstrip()
    mot_choisi = mot_choisi.upper()
    mot_partiel = "-" * len(mot_choisi)
    afficher_mot(mot_partiel)
    photo = PhotoImage(file = "images/esp/pendu_0.gif")
    image_pendu.config(image = photo)
    image_pendu.image = photo
    canevas.itemconfig(bravo,text="")

def recommencer():
    for i in range(26):
        bouton[i].pack_forget()
    init_jeu()

def fermeture(profilName):
    fenetre.destroy()

def openFrame(profilName):
    global name
    name = profilName
    cfg.read("profils.cfg")
    if "esp_gagne" in cfg.options(profilName) and "esp_perdu" in cfg.options(profilName):
        pass
    else:
        cfg.set(profilName, "esp_gagne", '0')
        cfg.set(profilName, "esp_perdu", '0')
        cfg.write(open("profils.cfg", 'w'))

    global fenetre, bouton, canevas, lettres, image_pendu, bravo, photo
    fenetre = Tk()
    fenetre.title("El Ahorcado")
    fenetre.wm_iconbitmap("images/EduGames_logo.ico")

    canevas = Canvas(fenetre, bg = 'white', height = 500, width = 620)
    canevas.pack(side = BOTTOM)

    bouton = [0]*26

    bouton2 = Button(fenetre, text = 'Quitter', command = lambda:fermeture(profilName))
    bouton2.pack(side = RIGHT)
    bouton1 = Button(fenetre, text = 'Recommencer', command = recommencer)
    bouton1.pack(side = RIGHT)

    photo = PhotoImage(file = "images/esp/pendu_0.gif")
    image_pendu = Label(canevas, image=photo, border = 0)
    image_pendu.place(x = 120, y = 140)
    lettres = canevas.create_text(320, 60, text = "", fill = 'black', font = 'Courrier 30')
    bravo = canevas.create_text(320,110,text="",fill='red',font='Courrier 40')

    init_jeu()
    fenetre.mainloop()