#-------------------------------------------------------------------------------
# Name:        EduGame.py
# Purpose:     Création et/ou connection d'un profil.
#
# Author:      Pedro Filipe Ribeiro Sousa
#
# Created:     25/04/2016
# Copyright:   © Copyright Pedro
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from tkinter import*
from tkinter.messagebox import*
from configparser import*
from time import sleep
import Matter
import os.path as file

cfg = ConfigParser()
if file.exists("profils.cfg"):
    cfg.read("profils.cfg")

def addProfil():
    """ Ajoute un profile d'utilisateur sur le programme """
    mainFrame.place_forget()
    extend('+')
    addFrame.place(x=5, y=5, width=sizeX-10, height=sizeY-10)

def selectProfil():
    """ Permet de choisir un profil existant """
    mainFrame.place_forget()
    extendPlus('+')
    selectFrame.place(x=10, y=10, width=175, height=45+nbRB*35)

def selectProfil_close():
    """ Ferme la page de selection de profil """
    selectFrame.place_forget()
    extendPlus('-')
    mainFrame.place(x=0, y=0, width=sizeX, height=sizeY)

def extendPlus(signe):
    """ Permet d'adapter la fenêtre selon le nombre de profil existant """
    global sizeX, sizeY
    if signe == '+':
        for i in range(0, 10):
            sizeY += 4*nbRB-15
            iFrame.minsize(width=sizeX, height=sizeY)
            iFrame.maxsize(width=sizeX, height=sizeY)
            iFrame.geometry('{0!s}x{1!s}'.format(sizeX, sizeY))
            iFrame.update()
            sleep(0.03)
    elif signe == '-':
        for i in range(0, 10):
            sizeY -= 4*nbRB-15
            iFrame.minsize(width=sizeX, height=sizeY)
            iFrame.maxsize(width=sizeX, height=sizeY)
            iFrame.geometry('{0!s}x{1!s}'.format(sizeX, sizeY))
            iFrame.update()
            sleep(0.03)

def createProfil():
    """ Crée le profil défini par l'utilisateur """
    if len(cfg.sections()) < 5:
        name = str(varName.get())
        age = str(sbAge.get())
        gender = str(varGender.get())
        if varLvLType.get() == 0:
            lvlType = "Collège"
            lvl = str(listLVL0.get(ACTIVE))
        elif varLvLType.get() == 1:
            lvlType = "Lycée"
            lvl = str(listLVL1.get(ACTIVE))
        lv1 = str(varLV1.get())
        if varLV1.get() == varLV2.get():
            lv2 = "none"
        else:
            lv2 = str(varLV2.get())
        if cfg.has_section(name):
            showerror("Erreur : Création de profil", "Le profil \"{0!s}\" existe déjà. Choisissez un autre nom ou supprimez le profil existant.".format(name))
        elif name == " " or name == "":
            showerror("Erreur : Création de profil", "Le champ de \"Nom de profil\" est vide. Veuillez choisir un nom pour créer un profil.")
        else:
            cfg.add_section(name)
            cfg.set(name, "Age", age)
            cfg.set(name, "Gender", gender)
            cfg.set(name, "Level Type", lvlType)
            cfg.set(name, "Level", lvl)
            cfg.set(name, "LV1", lv1)
            cfg.set(name, "LV2", lv2)
            cfg.write(open("profils.cfg", 'w'))
            showinfo("Création de profil achevé", "Le profil \"{0!s}\" à été créé avec succés ! Vous serrez connecté dans un instant.".format(name))
            connect(name)
    else:
        showerror("Erreur : Création de profil", "Le nombre maximum de profils a été atteint. Pour créer un nouveau profil, veuillez supprimer un profil existant.")

def addProfil_close():
    """ Ferme la page de création de profils """
    addFrame.place_forget()
    extend('-')
    mainFrame.place(x=0, y=0, width=sizeX, height=sizeY)

def extend(signe):
    """
    Agrandit ou Rétrécit la fenêtre
      extend(signe):
        parm signe: '-' pour rétrécir, '+' agrandir
    """
    global sizeX, sizeY
    if signe == '+':
        for i in range(0, 10):
            sizeX += 10
            sizeY += 20
            iFrame.minsize(width=sizeX, height=sizeY)
            iFrame.maxsize(width=sizeX, height=sizeY)
            iFrame.geometry('{0!s}x{1!s}'.format(sizeX, sizeY))
            iFrame.update()
            sleep(0.03)
    elif signe == '-':
        for i in range(0, 10):
            sizeX -= 10
            sizeY -= 20
            iFrame.minsize(width=sizeX, height=sizeY)
            iFrame.maxsize(width=sizeX, height=sizeY)
            iFrame.geometry('{0!s}x{1!s}'.format(sizeX, sizeY))
            iFrame.update()
            sleep(0.03)

def showLvLList():
    """ Affiche la liste des niveaux scolaires """
    if varLvLType.get() == 0:
        listLVL1.place_forget()
        listLVL0.place(x=40, y=140, width=100, height=75)
    elif varLvLType.get() == 1:
        listLVL0.place_forget()
        listLVL1.place(x=150, y=140, width=100, height=75)

def connect(profileName):
    """ Se connect avec le profil choisit """
    iFrame.destroy()
    Matter.open(profileName)

iFrame = Tk()
iFrame.title("EduGame")
iFrame.wm_iconbitmap("images/EduGames_logo.ico")
sizeX, sizeY = 200, 200
iFrame.geometry('{0!s}x{1!s}'.format(sizeX, sizeY))

""" ***** Fenêtre Principale ***** """
mainFrame = Frame(iFrame)
btAddProfile = Button(mainFrame, text="Créer un profile d'utilisateur", command=addProfil).place(x=5, y=5, width=sizeX-10, height=sizeY/2-10)
btConnectProfil = Button(mainFrame, text="Se connecter à un profile existant", command=selectProfil).place(x=5, y=sizeY/2+5, width=sizeX-10, height=sizeY/2-10)
mainFrame.place(x=0, y=0, width=sizeX, height=sizeY)

""" ***** Fenêtre Ajouter Profil ***** """
addFrame = LabelFrame(iFrame, text="Ajouter un Profile")
varName = StringVar()
varName.set("Nouveau Profil")
lbName = Label(addFrame, text="Nom de profil:").place(x=10, y=10)
eName = Entry(addFrame, textvariable=varName).place(x=10, y=30, width=270, height=20)
lbAge = Label(addFrame, text="Âge :").place(x=10, y=60)
sbAge = Spinbox(addFrame, from_=10, to=20)
sbAge.place(x=55, y=60, width=50, height=20)
lbGender = Label(addFrame, text="Sexe :").place(x=120, y=60)
varGender = StringVar()
rbGender1 = Radiobutton(addFrame, text="Masculin", variable=varGender, value='M')
rbGender1.select()
rbGender1.place(x=160, y=60)
rbGneder2 = Radiobutton(addFrame, text="Féminin", variable=varGender, value='F').place(x=160, y=80)
# ***** Niveau scolaire ***** #
lbLVL = Label(addFrame, text="Niveau Scolaire :").place(x=10, y=110)
varLvLType = IntVar()
rbLvLType1 = Radiobutton(addFrame, text="Collège", indicatoron = 0, variable=varLvLType, value=0, command=showLvLList).place(x=120, y=110, width=75, height=25)
rbLvLType2 = Radiobutton(addFrame, text="Lycée", indicatoron = 0, variable=varLvLType, value=1, command=showLvLList).place(x=200, y=110, width=75, height=25)
listLVL0 = Listbox(addFrame)
listLVL1 = Listbox(addFrame)
listLVL0.insert(0, "Sixième")
listLVL0.insert(1, "Cinquième")
listLVL0.insert(2, "Quatrième")
listLVL0.insert(3, "Troisième")
listLVL1.insert(0, "Seconde")
listLVL1.insert(1, "Première")
listLVL1.insert(2, "Terminale")
listLVL0.place(x=40, y=140, width=100, height=75)
# ***** Choix de la langue LV1 ***** #
varLV1 = StringVar()
lbLV1 = Label(addFrame, text="LV1 :").place(x=10, y=240)
lv1Anglais = Radiobutton(addFrame, text="Anglais", variable=varLV1, value="Anglais")
lv1Anglais.select()
lv1Anglais.place(x=5, y=260)
lv1Allemand = Radiobutton(addFrame, text="Allemand", variable=varLV1, value="Allemand").place(x=70, y=260)
lv1Espagnole = Radiobutton(addFrame, text="Espagnole", variable=varLV1, value="Espagnole").place(x=145, y=260)
lv1Italien = Radiobutton(addFrame, text="Italien", variable=varLV1, value="Italien").place(x=225, y=260)
# ***** Choix de la langue LV2 ***** #
varLV2 = StringVar()
lbLV2 = Label(addFrame, text="LV2 (sinon mettre même que LV1) :").place(x=10, y=285)
lv2Anglais = Radiobutton(addFrame, text="Anglais", variable=varLV2, value="Anglais")
lv2Anglais.select()
lv2Anglais.place(x=5, y=305)
lv2Allemand = Radiobutton(addFrame, text="Allemand", variable=varLV2, value="Allemand").place(x=70, y=305)
lv2Espagnole = Radiobutton(addFrame, text="Espagnole", variable=varLV2, value="Espagnole").place(x=145, y=305)
lv2Italien = Radiobutton(addFrame, text="Italien", variable=varLV2, value="Italien").place(x=225, y=305)
# ***** Boutons ***** #
btRetour = Button(addFrame, text="Retour", command=addProfil_close).place(x=10, y=340, width=75, height=25)
btCreate = Button(addFrame, text="Créer", command=createProfil).place(x=200, y=340, width=75, height=25)

""" ***** Fenêtre Choisir Profil ***** """
selectFrame = LabelFrame(iFrame, text="Choisir un Profil")
profil = StringVar()
nbRB = 0
rb = [0]*5
for section in cfg.sections():
    rb[nbRB] = Radiobutton(selectFrame, text=section, variable=profil, value=section, indicatoron=0).place(x=10, y=nbRB*35, width=150, height=30)
    nbRB+=1

btRetour = Button(selectFrame, text="Retour", command=selectProfil_close).place(x=10, y=nbRB*35, width=75, height=25)
btConnect = Button(selectFrame, text="Se connecter", command=lambda:connect(profil.get())).place(x=85, y=nbRB*35, width=75, height=25)

iFrame.mainloop()