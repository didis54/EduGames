# Créé par yqpezzin1, le 29/04/2016 en Python 3.2

from tkinter import*
from configparser import*
from random import randint
from math import*

def init():
    """fonction créant une fonction de second degré """

    global f,a,b,c
    a = randint(-20,20)
    b = randint(-20,20)
    c = randint(-30,30)

    while a == 0 :
        a = randint(-20,20)
    if b == 0 :
        y = ""
    if c == 0 :
        z = ""
    if b < 0 :
        y = str(b)+"x"
    if c < 0 :
        z = str(c)
    if b > 0 :
        y = "+"+str(b)+"x"
    if c > 0 :
        z = "+"+str(c)
    if a != 0 and a != 1:
        x = str(a)+"x²"
    if a == 1 :
        x = "x²"
    if b == 1 :
        y = "+x"
    if b == -1 :
        y = "-x"
    f = x+y+z+" = 0"


def calcul(mode) :
    """Fonction vérifiant les solution de l'équation"""
    Init.place_forget()
    Etat = Frame(minijeu_1)
    Etat.place(x=0,y=0,height=hauteur,width=largeur)
    equation = Label (Etat,text=f).place(x=0,y=20,height=25,width=largeur)
    global a,b,c,x,y,utilA,utilB,utilC,texte

    if mode == "Cas1" :
        a

    if mode == "Cas2" :
        a

    if mode == "Cas3" :
        a

    if mode == "Delta" :
        utilA = StringVar()
        utilB = StringVar()
        utilC = StringVar()
        A = Entry(Etat,textvariable=utilA).place(x=35,y=hauteur/2,height=25,width=25)
        B = Entry(Etat,textvariable=utilB).place(x=35,y=hauteur/2+38,height=25,width=25)
        C = Entry(Etat,textvariable=utilC).place(x=35,y=hauteur/2+76,height=25,width=25)
        IndA= Label (Etat,text="a = ").place(x=10,y=hauteur/2,height=25,width=25)
        IndB= Label (Etat,text="b = ").place(x=10,y=hauteur/2+38,height=25,width=25)
        IndC= Label (Etat,text="c = ").place(x=10,y=hauteur/2+76,height=25,width=25)
        ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
        ValABC = Button(Etat,text="ok",command=lambda:calcul("Delta1")).place(x=23,y=hauteur/2+107,height=25,width=35)

    if mode == "Delta1" :
        repA = int(utilA.get())
        repB = int(utilB.get())
        repC = int(utilC.get())
        if repA == a and repB == b and repC == c :
            texte = "Indique la valeurs de Delta"
            FinA= Label (Etat,text="a = {0!s}".format(repA)).place(x=10,y=hauteur/2,height=25,width=50)
            FinB= Label (Etat,text="b = {0!s}".format(repB)).place(x=10,y=hauteur/2+38,height=25,width=50)
            FinC= Label (Etat,text="c = {0!s}".format(repC)).place(x=10,y=hauteur/2+76,height=25,width=50)
            ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)

        else :
            texte = "Non ce ne sont pas les bonnes valeurs"
            calcul("Delta")


    if mode == "Recommencer" :
        a


def bouton(reponse):
    """Fonction vérifiant si la réponse à "doit-je utiliser delta ?" est correcte ou non"""

    texte = "Indique les valeurs de a,b et c"
    correction = ""
    global a,b,c,x,y,texte

    if reponse == 1 :

        if b == 0 and c != 0 :
            R = -c/a

            if -c/a >= 0 :
                x = sqrt(-c/a)
                y = -sqrt(-c/a)
                correction = "Non, \n tu n'est pas obliger de faire delta, \n tu a ax²+c = 0 <=> x² = -c/a \n ainsi les solution sont \n x = racine(-c/a) ou x = -racine(-c/a).\n Continue et trouve le résultat"
                continuer = Button(Init,text="Continuer",command=lambda:calcul("Cas1")).place(x=largeur/2-56,y=hauteur/2,height=25,width=112)
            else :
                correction = "Non, \n tu n'est pas obliger de faire delta, \n tu a ax²+c = 0 <=> x² = -c/a \n or cela est impossible dans notre cas car -c/a est négatif, \n il n'y a donc pas de résultat"
                continuer = Button(Init,text="Continuer",command=lambda:calcul("Recommencer")).place(x=largeur/2-56,y=hauteur/2,height=25,width=112)

        if c == 0 and b != 0 :
            x = 0
            y = -b/a
            correction = "Non, \n tu n'est pas obliger de faire delta, \n tu a ax²+bx = 0 <=> x(ax+b) = 0 \n ainsi les solution sont x = 0 et x = -b/a.\n Continue et trouve le résultat"
            continuer = Button(Init,text="Continuer",command=lambda:calcul("Cas2")).place(x=largeur/2,y=hauteur/2-56,height=25,width=112)

        if c == 0 and b == 0 :
            x = 0
            correction = "Non, \n tu n'est pas obliger de faire delta, \n tu a ax² = 0 <=> x² = 0 \n ainsi la solution est x = 0."
            continuer = Button(Init,text="Continuer",command=lambda:calcul("Recommencer")).place(x=largeur/2-56,y=hauteur/2,height=25,width=112)

        if b != 0 and c != 0:
            x = (b*b)-(4*a*c)
            correction = "Bien ! \n maintenant applique delta et trouve le résultat"
            continuer = Button(Init,text="Continuer",command=lambda:calcul("Delta")).place(x=largeur/2-56,y=hauteur/2,height=25,width=112)


    reponse1 = Label (Init,text=correction).place(x=0,y=175,height=85,width=largeur)



    if reponse == 0 :

        if b == 0 and c != 0 :
            R = -c/a

            if -c/a >= 0 :
                x = sqrt(-c/a)
                y = -sqrt(-c/a)
                correction = "Bien ! \n ici tu n'est pas obliger d'utiliser delta.\n Continue et trouve le résultat"
                continuer = Button(Init,text="Continuer",command=lambda:calcul("Cas1")).place(x=largeur/2-56,y=hauteur/2,height=25,width=112)
            else :
                correction = "Bien ! \n ici tu n'est pas obliger d'utiliser delta, \n tu a ax²+c = 0 <=> x² = -c/a \n or cela est impossible dans notre cas car -c/a est négatif, \n il n'y a donc pas de résultat"
                continuer = Button(Init,text="Continuer",command=lambda:calcul("Recommencer")).place(x=largeur/2-56,y=hauteur/2,height=25,width=112)

        if c == 0 and b != 0 :
            x = 0
            y = -b/a
            correction = "Bien ! \n ici tu n'est pas obliger de faire delta.\n Continue et trouve le résultat"
            continuer = Button(Init,text="Continuer",command=lambda:calcul("Cas2")).place(x=largeur/2-56,y=hauteur/2,height=25,width=112)

        if c == 0 and b == 0 :
            x = 0
            correction = "Bien ! \n ici tu n'est pas obliger de faire delta.\n Continue et trouve le résultat"
            continuer = Button(Init,text="Continuer",command=lambda:calcul("Cas3")).place(x=largeur/2-56,y=hauteur/2,height=25,width=112)

        if b != 0 and c != 0:
            x = (b*b)-(4*a*c)
            correction = "Non, \n ici tu ne peut pas trouvé le résultat sans delta \n maintenant applique delta et trouve le résultat"
            continuer = Button(Init,text="Continuer",command=lambda:calcul("Delta")).place(x=largeur/2-56,y=hauteur/2,height=25,width=112)

    reponse1 = Label (Init,text=correction).place(x=0,y=175,height=85,width=largeur)


minijeu_1 = Tk()
Init = Frame(minijeu_1)
minijeu_1.title ("Trouve les illuminatis !")
largeur,hauteur = 310,270
minijeu_1.geometry ("{0!s}x{1!s}".format(largeur, hauteur))
minijeu_1.minsize (height=hauteur,width=largeur)
minijeu_1.maxsize (height=hauteur,width=largeur)
init()
equation = Label (Init,text=f).place(x=0,y=20,height=25,width=largeur)
question = Label (Init,text="Doit-je utiliser Delta ?",fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
oui = Button(Init,text="Oui",command=lambda:bouton(1)).place(x=largeur/2,y=hauteur/2-25,height=25,width=75)
non = Button(Init,text="Non",command=lambda:bouton(0)).place(x=largeur/2-75,y=hauteur/2-25,height=25,width=75)
Init.place(x=0,y=0,height=hauteur,width=largeur)
minijeu_1.mainloop()
