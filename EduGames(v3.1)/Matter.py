#-------------------------------------------------------------------------------
# Name:        Matter.py
# Purpose:     Regrouper tout les jeux dans une fenêtre.
#
# Author:      Pedro
#
# Created:     30/04/2016
# Copyright:   © Copyright Pedro
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from tkinter import*
from configparser import*
from tkinter.messagebox import*
from time import sleep
import ang_1
import all_1
import esp_1
import ita_1
import math_1
import os.path as file

cfg = ConfigParser()
name = ""

def openGame1(lang):
    """ Ouvre la partie choix du jeu selon la langue choisit """
    iFrame.destroy()
    if lang == "Anglais":
        ang_1.openFrame(name)
    elif lang == "Allemand":
        all_1.openFrame(name)
    elif lang == "Espagnole":
        esp_1.openFrame(name)
    elif lang == "Italien":
        ita_1.openFrame(name)

def openGame(matter):
    """ Ouvre le jeu correspondant a la matière choisit """
    if matter == "math":
        iFrame.destroy()
        math_1.openframe(name)

def gameLV1():
    """ Lance le jeu LV1 associé à la langue de l'utilisateur """
    lv1 = cfg.get(name, "lv1")
    mainFrame.place_forget()
    extend('-')
    if lv1 == "Anglais":
        Jeu1.config(text="The Hanged Man", command=lambda:openGame1("Anglais"))
    elif lv1 == "Allemand":
        Jeu1.config(text="Die Gehenkten", command=lambda:openGame1("Allemand"))
    elif lv1 == "Espagnole":
        Jeu1.config(text="El Ahorcado", command=lambda:openGame1("Espagnole"))
    elif lv1 == "Italien":
        Jeu1.config(text="L'impiccato", command=lambda:openGame1("Italien"))
    gameFrame.place(x=0, y=0, width=sizeX, height=sizeY)

def gameLV2():
    """ Lance le jeu LV2 associé à la langue de l'utilisateur """
    lv2 = cfg.get(name, "lv2")
    mainFrame.place_forget()
    extend('-')
    if lv2 == "Anglais":
        Jeu1.config(text="The Hanged Man", command=lambda:openGame1("Anglais"))
    elif lv2 == "Allemand":
        Jeu1.config(text="Die Gehenkten", command=lambda:openGame1("Allemand"))
    elif lv2 == "Espagnole":
        Jeu1.config(text="El Ahorcado", command=lambda:openGame1("Espagnole"))
    elif lv2 == "Italien":
        Jeu1.config(text="L'impiccato", command=lambda:openGame1("Italien"))
    gameFrame.place(x=0, y=0, width=sizeX, height=sizeY)

def extend(signe):
    """ Augmente ou reduit la taill fenêtre selon le paramêtre
        signe : str
            '+' --> augmente la fenêtre
            '-' --> reduit la fenêtre
    """
    global sizeX, sizeY
    if signe == '-':
        for i in range(0, 10):
            sizeX-=5
            sizeY-=10
            iFrame.minsize(width=sizeX, height=sizeY)
            iFrame.maxsize(width=sizeX, height=sizeY)
            iFrame.geometry('%sx%s' % (sizeX, sizeY))
            iFrame.update()
            sleep(0.03)
    if signe == '+':
        for i in range(0, 10):
            sizeX+=5
            sizeY+=10
            iFrame.minsize(width=sizeX, height=sizeY)
            iFrame.maxsize(width=sizeX, height=sizeY)
            iFrame.geometry('%sx%s' % (sizeX, sizeY))
            iFrame.update()
            sleep(0.03)

def extendStat(signe):
    """ Augmente ou reduit la taill fenêtre selon le paramêtre
        signe : str
            '+' --> augmente la fenêtre
            '-' --> reduit la fenêtre
    """
    global sizeX, sizeY
    if signe == '-':
        for i in range(0, 10):
            sizeX-=24
            sizeY-=0
            iFrame.minsize(width=sizeX, height=sizeY)
            iFrame.maxsize(width=sizeX, height=sizeY)
            iFrame.geometry('%sx%s' % (sizeX, sizeY))
            iFrame.update()
            sleep(0.03)
    if signe == '+':
        for i in range(0, 10):
            sizeX+=24
            sizeY+=0
            iFrame.minsize(width=sizeX, height=sizeY)
            iFrame.maxsize(width=sizeX, height=sizeY)
            iFrame.geometry('%sx%s' % (sizeX, sizeY))
            iFrame.update()
            sleep(0.03)

def langFrameClose():
    """ Ferme la fenêtre du choix de jeu """
    gameFrame.place_forget()
    extend('+')
    mainFrame.place(x=0, y=0, width=sizeX, height=sizeY)

def openStatFrame():
    """ Affiche les statistiques du joueur """
    mainFrame.place_forget()
    extendStat('+')
    statFrame.place(x=0, y=0, width=sizeX, height=sizeY)

def showStat(matter):
    lbTitle = Label(statFrame, text="")
    lbTitle.place(x=10, y=45)
    lbVal1 = Label(statFrame, text="")
    lbVal1.place(x=10, y=80)
    lbVal2 = Lable(statFrame, text="")
    lbVal2.place(x=100, y=80)
    lbRatio1 = Label(statFrame, text="")
    lbRatio1.place(x=10, y=115)

    lbTotal = Label(statFrame, text="Total :").place(x=200, y=45)
    lbVal3 = Label(statFrame, text="").place(x=200, y=80)
    lbVal4 = Lable(statFrame, text="").place(x=300, y=80)
    lbRatio2 = Label(statFrame, text="").place(x=200, y=115)
    if matter == "math":
        if "math_score" in cfg.options(name):
            lbTitle.config(text="Mathématiques :")
            lbVal1.config(text="Score :" + cfg.get(name, "math_score"))
            lbVal2.config(text="Nombre de parties :" + cfg.get(name, "math_nbr_partie"))

def open(profilName):
    """ Permet d'ouvrir la fenêtre de choix de la matière """
    if file.exists("profils.cfg"):
        cfg.read("profils.cfg")

    global name, sizeX, sizeY, iFrame, mainFrame, gameFrame, Jeu1, langJeu2, Retour, statFrame
    name = profilName

    iFrame = Tk()
    iFrame.title("EduGames - " + name)
    iFrame.wm_iconbitmap("images/EduGames_logo.ico")
    sizeX, sizeY = 340, 200
    iFrame.geometry("%sx%s" % (sizeX, sizeY))
    iFrame.minsize(width=sizeX, height=sizeY)
    iFrame.maxsize(width=sizeX, height=sizeY)

    """ ***** Fenêtre principale ***** """
    mainFrame = Frame(iFrame)

    imgMath = PhotoImage(file="images/math.gif")
    imgPhilo = PhotoImage(file="images/philo.gif")
    imgHist_Geo = PhotoImage(file="images/hi_ge.gif")
    imgPhysique = PhotoImage(file="images/phys.gif")
    imgFrancais = PhotoImage(file="images/fran.gif")
    imgAnglais = PhotoImage(file="images/Anglais.gif")
    imgAllemand = PhotoImage(file="images/Allemand.gif")
    imgEspagnole = PhotoImage(file="images/Espagnole.gif")
    imgItalien = PhotoImage(file="images/Italien.gif")

    # ***** Création des boutons selon le profil ***** #
    lv1 = cfg.get(name, "lv1")
    lv2 = cfg.get(name, "lv2")

    btMath = Button(mainFrame, text="Math", image=imgMath, command=lambda:openGame("math")).place(x=10, y=10, width=64, height=64)
    if cfg.get(name, "level") == "Terminale":
        btPhilo = Button(mainFrame, text="Philosophie", image=imgPhilo, command=lambda:showinfo("Non disponible", "Ce jeu n'est pas disponible pour le moment.")).place(x=138, y=10, width=64, height=64)
    else:
        btFr = Button(mainFrame, text="Français", image=imgFrancais, command=lambda:showinfo("Non disponible", "Ce jeu n'est pas disponible pour le moment.")).place(x=138, y=10, width=64, height=64)
    btHG = Button(mainFrame, text="Histoire-Géographie", image=imgHist_Geo, command=lambda:showinfo("Non disponible", "Ce jeu n'est pas disponible pour le moment.")).place(x=266, y=10, width=64, height=64)
    if cfg.get(name, "level") != "Sixième" and lv2 != "none":
        btPhy = Button(mainFrame, text="Physique-Chimie", image=imgPhysique, command=lambda:showinfo("Non disponible", "Ce jeu n'est pas disponible pour le moment.")).place(x=10, y=84, width=64, height=64)
        btLV1 = Button(mainFrame, text=lv1, command=gameLV1)
        btLV1.place(x=138, y=84, width=64, height=64)
        btLV2 = Button(mainFrame, text=lv2, command=gameLV2)
        btLV2.place(x=266, y=84, width=64, height=64)
    elif cfg.get(name, "level") != "Sixième" and lv2 == "none":
        btPhy = Button(mainFrame, text="Physique-Chimie", image=imgPhysique, command=lambda:showinfo("Non disponible", "Ce jeu n'est pas disponible pour le moment.")).place(x=74, y=84, width=64, height=64)
        btLV1 = Button(mainFrame, text=lv1, command=gameLV1)
        btLV1.place(x=202, y=84, width=64, height=64)
    elif cfg.get(name, "level") == "Sixième" and lv2 == "none":
        btLV1 = Button(mainFrame, text=lv1, command=gameLV1)
        btLV1.place(x=138, y=84, width=64, height=64)

    if lv1 == "Anglais":
        btLV1.config(image=imgAnglais)
    elif lv1 == "Allemand":
        btLV1.config(image=imgAllemand)
    elif lv1 == "Espagnole":
        btLV1.config(image=imgEspagnole)
    elif lv1 == "Italien":
        btLV1.config(image=imgItalien)

    if lv2 == "Anglais":
        btLV2.config(image=imgAnglais)
    elif lv2 == "Allemand":
        btLV2.config(image=imgAllemand)
    elif lv2 == "Espagnole":
        btLV2.config(image=imgEspagnole)
    elif lv2 == "Italien":
        btLV2.config(image=imgItalien)

    bt_quite = PhotoImage(file="images/bt_quite.gif")
    bt_stats = PhotoImage(file="images/bt_stats.gif")
    bt_param = PhotoImage(file="images/bt_param.gif")

    # ***** Création des boutons pratiques ***** #
    btQuite = Button(mainFrame, text="Quitter", image=bt_quite, command=iFrame.destroy).place(x=10, y=158, width=100, height=30)
    btStat = Button(mainFrame, text="Statistiques", image=bt_stats, command=openStatFrame).place(x=120, y=158, width=100, height=30)
    btSettings = Button(mainFrame, text="Paramêtres", image=bt_param, command=lambda:showinfo("Non disponible", "Non disponible pour le moment.")).place(x=230, y=158, width=100, height=30)

    mainFrame.place(x=0, y=0, width=sizeX, height=sizeY)

    """ ***** Fenêtre Langue ***** """
    gameFrame = Frame(iFrame)
    Jeu1 = Button(gameFrame, text="")
    Jeu1.place(x=10, y=10, width=125, height=25)
##        langJeu2 = Button(gameFrame, text="")
##        langJeu2.place(x=95, y=10, width=125, height=25)
    Retour = Button(gameFrame, text="Retour", command=langFrameClose)
    Retour.place(x=10, y=55, width=85, height=25)

    """ ***** Fenêtre de statistique ***** """
    statFrame = Frame(iFrame)
    varStat = StringVar()
    rbMath = Radiobutton(statFrame, text="Math", variable=varStat, value="Math", indicatoron=0, command=openStatFrame).place(x=10, y=10, width=85, height=25)
    if cfg.get(name, "level") == "Terminale":
        btPhilo = Radiobutton(statFrame, text="Philosophie", variable=varStat, value="Philo", indicatoron=0, command=openStatFrame).place(x=105, y=10, width=85, height=25)
    else:
        btFr = Radiobutton(statFrame, text="Français", variable=varStat, value="Francais", indicatoron=0, command=openStatFrame).place(x=105, y=10, width=85, height=25)
    btHG = Radiobutton(statFrame, text="Histoire-Géo", variable=varStat, value="Hist-Geo", indicatoron=0, command=openStatFrame).place(x=200, y=10, width=85, height=25)
    if cfg.get(name, "level") != "Sixième" and lv2 != "none":
        btPhy = Radiobutton(statFrame, text="Physique-Chimie", variable=varStat, value="Physique", indicatoron=0, command=openStatFrame).place(x=295, y=10, width=85, height=25)
        btLV1 = Radiobutton(statFrame, text="LV1", variable=varStat, value="LV1", indicatoron=0, command=openStatFrame)
        btLV1.place(x=390, y=10, width=85, height=25)
        btLV2 = Radiobutton(statFrame, text="LV2", variable=varStat, value="LV2", indicatoron=0, command=openStatFrame)
        btLV2.place(x=485, y=10, width=85, height=25)
    elif cfg.get(name, "level") != "Sixième" and lv2 == "none":
        btPhy = Radiobutton(statFrame, text="Physique-Chimie", variable=varStat, value="Physique", indicatoron=0, command=openStatFrame).place(x=295, y=10, width=85, height=25)
        btLV1 = Radiobutton(statFrame, text="LV1", variable=varStat, value="LV1", indicatoron=0, command=openStatFrame)
        btLV1.place(x=390, y=10, width=85, height=25)
    elif cfg.get(name, "level") == "Sixième" and lv2 == "none":
        btLV1 = Radiobutton(statFrame, text="LV1", variable=varStat, value="LV1", indicatoron=0, command=openStatFrame)
        btLV1.place(x=295, y=10, width=85, height=25)

    iFrame.mainloop()
