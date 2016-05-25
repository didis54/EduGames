# Créé par yqpezzin1, le 29/04/2016 en Python 3.2

from tkinter import*
from configparser import*
from random import randint
from math import*
from decimal import Decimal

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
    if a == -1 :
        x = "-x²"
    if b == 1 :
        y = "+x"
    if b == -1 :
        y = "-x"
    f = x+y+z+" = 0"

def calculnbrSol() :
    """Fonction donnant le nombre de solution selon les valeurs de delta"""
    global reelnbrSol
    if x == 0 :
        reelnbrSol = 1
    if x < 0 :
        reelnbrSol = 0
    if x > 0 :
        reelnbrSol = 2

def calculSol(mode) :
    """Fonction donnant les solutions de l'équation"""

    global reelSol1,reelSol2
    if mode == 1 :
        reelSol1 = (-b-sqrt(x))/(2*a)
        reelSol1 = Decimal(str(round(reelSol1,2)))
    if mode == 2 :
        reelSol1 = (-b-sqrt(x))/(2*a)
        reelSol2 = (-b+sqrt(x))/(2*a)
        reelSol1 = Decimal(str(round(reelSol1,2)))
        reelSol2 = Decimal(str(round(reelSol2,2)))

def stat(mode) :
    """Fonction calculant le nombre de point"""
    global points

    if mode == 0 :
        points = 10
    if mode == 1 :
        points = points-1
    if points < 0 :
        points = 0

def recommencer() :
    """Fonction relancant le jeu"""

    minijeu_1.destroy()
    openframe()

def quitter() :
    """Fonction renvoyant au menu principal"""

    minijeu_1.destroy()

def calcul(mode,essais) :
    """Fonction vérifiant les solution de l'équation"""

    global a,b,c,x,y,utilA,utilB,utilC,utilDelta,texte,repA,repB,repC,repD,utilnbrSol,reelnbrSol,repnbrSol,utilSol1,utilSol2,reelSol1,reelSol2,Etat,points
    Init.place_forget()
    Etat = Frame(minijeu_1)
    Etat.place(x=0,y=0,height=hauteur,width=largeur)
    equation = Label (Etat,text=f).place(x=0,y=20,height=25,width=largeur)
    Indpoints = Label (Etat,text="points : "+str(points)+"/10",fg="red").place(x=largeur-100,y=0,height=25,width=100)
    Btnquitter = Button(Etat,text="Quitter",command=quitter)
    Btnquitter.place(x=0,y=0,height=25,width=75)

    if mode == "Cas1" :

        if essais == 0 :
            texte = "Indique le nombre de solution possible"

        utilnbrSol = StringVar()
        nbrSol = Entry(Etat,textvariable=utilnbrSol).place(x=190,y=hauteur/2+38,height=25,width=25)
        IndnbrSol = Label (Etat,text="Nombre de\n solution :").place(x=110,y=hauteur/2+28,height=50,width=75)
        ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
        ValABC = Button(Etat,text="ok",command=lambda:calcul("Cas1.1",0)).place(x=132,y=hauteur/2+78,height=25,width=35)

    if mode == "Cas1.1" :

            if -c/a >= 0 :

                reelnbrSol = 2
                repnbrSol = utilnbrSol.get()
                utilSol1 = StringVar()
                utilSol2 = StringVar()

                if str(reelnbrSol) == repnbrSol :

                    if essais == 0 :
                        texte = "Maintenant donne les valeurs de ces solutions"

                    FinnbrSol = Label (Etat,text="Nombre de\n solution : %s" %repnbrSol).place(x=110,y=hauteur/2+28,height=75,width=75)
                    ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
                    Sol1 = Entry(Etat,textvariable=utilSol1).place(x=60,y=hauteur/2+106,height=25,width=50)
                    Sol2 = Entry(Etat,textvariable=utilSol2).place(x=190,y=hauteur/2+106,height=25,width=50)
                    IndSol1 = Label (Etat,text="x' = ").place(x=10,y=hauteur/2+106,height=25,width=50)
                    IndSol2 = Label (Etat,text="x\" = ").place(x=140,y=hauteur/2+106,height=25,width=50)
                    ValABC = Button(Etat,text="ok",command=lambda:calcul("Cas1.2",0)).place(x=250,y=hauteur/2+106,height=25,width=35)

                else :
                    texte = "Non ce n'est pas le bon nombre"
                    stat(1)
                    calcul("Cas1",1)

            if -c/a < 0 :

                reelnbrSol = 0
                repnbrSol = utilnbrSol.get()

                if str(reelnbrSol) == repnbrSol :

                    if essais == 0 :
                        texte = "Bien tu a résolu cette équation !"

                    FinnbrSol = Label (Etat,text="Nombre de\n solution : %s" %repnbrSol).place(x=110,y=hauteur/2+28,height=75,width=75)
                    ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
                    reboot = Button(Etat,text="Recommencer",command=recommencer).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)

                else :

                    texte = "Non ce n'est pas le bon nombre"
                    stat(1)
                    calcul("Cas1",1)

    if mode == "Cas1.2" :

        repSol1 = utilSol1.get()
        repSol2 = utilSol2.get()
        reelSol1 = Decimal(str(round(x,2)))
        reelSol2 = Decimal(str(round(y,2)))

        if str(reelSol1) == repSol1 or str(reelSol2) == repSol2 :

            if str(reelSol2) == repSol1 or str(reelSol2) == repSol2 :

                texte = "Bien !! tu à résolu cette équation !"
                FinnbrSol = Label (Etat,text="Nombre de\n solution : %s" %repnbrSol).place(x=110,y=hauteur/2+28,height=75,width=75)
                FinSol1 = Label (Etat,text="x' = %s" %reelSol1).place(x=10,y=hauteur/2+106,height=25,width=100)
                FinSol2 = Label (Etat,text="x\" = %s" %reelSol2).place(x=140,y=hauteur/2+106,height=25,width=100)
                ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
                reboot = Button(Etat,text="Recommencer",command=recommencer).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)


            else :

                texte = "Non, tu a une erreur"
                stat(1)
                calcul("Cas1.1",1)

        else :

            texte = "Non, tu a une erreur"
            stat(1)
            calcul("Cas1.1",1)

    if mode == "Cas2" :

        if essais == 0 :
            texte = "Indique le nombre de solution possible"

        utilnbrSol = StringVar()
        nbrSol = Entry(Etat,textvariable=utilnbrSol).place(x=190,y=hauteur/2+38,height=25,width=25)
        IndnbrSol = Label (Etat,text="Nombre de\n solution :").place(x=110,y=hauteur/2+28,height=50,width=75)
        ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
        ValABC = Button(Etat,text="ok",command=lambda:calcul("Cas2.1",0)).place(x=132,y=hauteur/2+78,height=25,width=35)

    if mode == "Cas2.1" :

        repnbrSol = utilnbrSol.get()
        reelnbrSol = 2
        utilSol1 = StringVar()
        utilSol2 = StringVar()

        if essais == 0 :
            texte = "Maintenant donne les valeurs de ces solutions"

        if str(reelnbrSol) == repnbrSol :

            FinnbrSol = Label (Etat,text="Nombre de\n solution : %s" %repnbrSol).place(x=110,y=hauteur/2+28,height=75,width=75)
            ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
            Sol1 = Entry(Etat,textvariable=utilSol1).place(x=60,y=hauteur/2+106,height=25,width=50)
            Sol2 = Entry(Etat,textvariable=utilSol2).place(x=190,y=hauteur/2+106,height=25,width=50)
            IndSol1 = Label (Etat,text="x' = ").place(x=10,y=hauteur/2+106,height=25,width=50)
            IndSol2 = Label (Etat,text="x\" = ").place(x=140,y=hauteur/2+106,height=25,width=50)
            ValABC = Button(Etat,text="ok",command=lambda:calcul("Cas2.2",0)).place(x=250,y=hauteur/2+106,height=25,width=35)

        else :

            texte = "Non ce n'est pas le bon nombre"
            stat(1)
            calcul("Cas2",1)

    if mode == "Cas2.2" :

        repSol1 = utilSol1.get()
        repSol2 = utilSol2.get()
        reelSol1 = Decimal(str(round(x,2)))
        reelSol2 = Decimal(str(round(y,2)))

        if str(reelSol1) == repSol1 or str(reelSol2) == repSol2 :

            if str(reelSol2) == repSol1 or str(reelSol2) == repSol2 :

                texte = "Bien !! tu à résolu cette équation !"
                FinnbrSol = Label (Etat,text="Nombre de\n solution : %s" %repnbrSol).place(x=110,y=hauteur/2+28,height=75,width=75)
                FinSol1 = Label (Etat,text="x' = %s" %reelSol1).place(x=10,y=hauteur/2+106,height=25,width=100)
                FinSol2 = Label (Etat,text="x\" = %s" %reelSol2).place(x=140,y=hauteur/2+106,height=25,width=100)
                ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
                reboot = Button(Etat,text="Recommencer",command=recommencer).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)


            else :

                texte = "Non, tu a une erreur"
                stat(1)
                calcul("Cas1.1",1)


        else :

            texte = "Non, tu a une erreur"
            stat(1)
            calcul("Cas1.1",1)

    if mode == "Cas3" :

        if essais == 0 :
            texte = "Indique le nombre de solution possible"

        utilnbrSol = StringVar()
        nbrSol = Entry(Etat,textvariable=utilnbrSol).place(x=190,y=hauteur/2+38,height=25,width=25)
        IndnbrSol = Label (Etat,text="Nombre de\n solution :").place(x=110,y=hauteur/2+28,height=50,width=75)
        ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
        ValABC = Button(Etat,text="ok",command=lambda:calcul("Cas3.1",0)).place(x=132,y=hauteur/2+78,height=25,width=35)

    if mode == "Cas3.1" :

        repnbrSol = utilnbrSol.get()
        reelnbrSol = 1
        utilSol1 = StringVar()

        if essais == 0 :
            texte = "Maintenant donne la valeurs de cette solutions"

        if str(reelnbrSol) == repnbrSol :

            FinnbrSol = Label (Etat,text="Nombre de\n solution : %s" %repnbrSol).place(x=110,y=hauteur/2+28,height=75,width=75)
            ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
            Sol1 = Entry(Etat,textvariable=utilSol1).place(x=60,y=hauteur/2+106,height=25,width=50)
            IndSol1 = Label (Etat,text="x' = ").place(x=10,y=hauteur/2+106,height=25,width=50)
            ValABC = Button(Etat,text="ok",command=lambda:calcul("Cas3.2",0)).place(x=250,y=hauteur/2+106,height=25,width=35)

        else :

            texte = "Non ce n'est pas le bon nombre"
            stat(1)
            calcul("Cas3",1)

    if mode == "Cas3.2" :

        repSol1 = utilSol1.get()
        reelSol1 = x

        if str(reelSol1) == repSol1 :

            texte = "Bien !! tu à résolu cette équation !"
            FinnbrSol = Label (Etat,text="Nombre de\n solution : %s" %repnbrSol).place(x=110,y=hauteur/2+28,height=75,width=75)
            FinSol1 = Label (Etat,text="x' = %s" %reelSol1).place(x=10,y=hauteur/2+106,height=25,width=100)
            ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
            reboot = Button(Etat,text="Recommencer",command=recommencer).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)


        else :

            texte = "Non, tu a une erreur"
            stat(1)
            calcul("Cas3.1",1)

    if mode == "Delta" :

        if essais == 0 :
                texte = "Indique les valeurs de a,b et c"

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
        ValABC = Button(Etat,text="ok",command=lambda:calcul("Delta1",0)).place(x=23,y=hauteur/2+107,height=25,width=35)

    if mode == "Delta1" :
        repA = utilA.get()
        repB = utilB.get()
        repC = utilC.get()

        if repA == str(a) and repB == str(b) and repC == str(c) :

            if essais == 0 :
                texte = "Indique la valeurs de Delta"

            utilDelta = StringVar()
            FinA= Label (Etat,text="a = %s" %repA).place(x=10,y=hauteur/2,height=25,width=50)
            FinB= Label (Etat,text="b = %s" %repB).place(x=10,y=hauteur/2+38,height=25,width=50)
            FinC= Label (Etat,text="c = %s" %repC).place(x=10,y=hauteur/2+76,height=25,width=50)
            ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
            D = Entry(Etat,textvariable=utilDelta).place(x=155,y=hauteur/2,height=25,width=50)
            IndD = Label (Etat,text="Delta = ").place(x=110,y=hauteur/2,height=25,width=40)
            ValABC = Button(Etat,text="ok",command=lambda:calcul("Delta2",0)).place(x=132,y=hauteur/2+50,height=25,width=35)

        else :
            texte = "Non ce ne sont pas les bonnes valeurs"
            stat(1)
            calcul("Delta",1)

    if mode == "Delta2" :
        repD = utilDelta.get()
        calculnbrSol()

        if repD == str(x) :

            if essais == 0 :
                texte = "Déduit en le nombre de solution possible"

            utilnbrSol=StringVar()
            FinA= Label (Etat,text="a = %s" %repA).place(x=10,y=hauteur/2,height=25,width=50)
            FinB= Label (Etat,text="b = %s" %repB).place(x=10,y=hauteur/2+38,height=25,width=50)
            FinC= Label (Etat,text="c = %s" %repC).place(x=10,y=hauteur/2+76,height=25,width=50)
            FinD = Label(Etat,text="Delta = %s" %repD).place(x=110,y=hauteur/2,height=25,width=90)
            ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
            nbrSol = Entry(Etat,textvariable=utilnbrSol).place(x=190,y=hauteur/2+38,height=25,width=25)
            IndnbrSol = Label (Etat,text="Nombre de\n solution :").place(x=110,y=hauteur/2+28,height=50,width=75)
            ValABC = Button(Etat,text="ok",command=lambda:calcul("Delta3",0)).place(x=132,y=hauteur/2+78,height=25,width=35)

        else :
            texte = "Non ce n'est pas la bonne valeur"
            stat(1)
            calcul("Delta1",1)

    if mode == "Delta3" :
        repnbrSol = utilnbrSol.get()

        if repnbrSol == str(reelnbrSol) :

            if reelnbrSol == 1 :

                if essais == 0 :
                    texte = "Maintenant donne la valeur de la solution"

                calculSol(1)
                FinA= Label (Etat,text="a = %s" %repA).place(x=10,y=hauteur/2,height=25,width=50)
                FinB= Label (Etat,text="b = %s" %repB).place(x=10,y=hauteur/2+38,height=25,width=50)
                FinC= Label (Etat,text="c = %s" %repC).place(x=10,y=hauteur/2+76,height=25,width=50)
                FinD = Label (Etat,text="Delta = %s" %repD).place(x=110,y=hauteur/2,height=25,width=90)
                FinnbrSol = Label (Etat,text="Nombre de\n solution : %s" %repnbrSol).place(x=110,y=hauteur/2+28,height=75,width=75)
                ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
                Sol1 = Entry(Etat,textvariable=utilSol1).place(x=150,y=hauteur/2+106,height=25,width=50)
                IndSol1 = Label (Etat,text="x' = ").place(x=50,y=hauteur/2+106,height=25,width=50)
                ValABC = Button(Etat,text="ok",command=lambda:calcul("Delta4",1)).place(x=250,y=hauteur/2+106,height=25,width=35)

            if reelnbrSol == 0 :

                texte = "Bien !! tu à résolu cette équation !"
                FinA= Label (Etat,text="a = %s" %repA).place(x=10,y=hauteur/2,height=25,width=50)
                FinB= Label (Etat,text="b = %s" %repB).place(x=10,y=hauteur/2+38,height=25,width=50)
                FinC= Label (Etat,text="c = %s" %repC).place(x=10,y=hauteur/2+76,height=25,width=50)
                FinD = Label (Etat,text="Delta = %s" %repD).place(x=110,y=hauteur/2,height=25,width=90)
                FinnbrSol = Label (Etat,text="Nombre de\n solution : %s" %repnbrSol).place(x=110,y=hauteur/2+28,height=75,width=75)
                ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
                reboot = Button(Etat,text="Recommencer",command=recommencer).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)

            if reelnbrSol == 2 :

                if essais == 0 :
                    texte = "Maintenant donne la valeur de ces solutions"

                calculSol(2)
                utilSol1 = StringVar()
                utilSol2 = StringVar()
                FinA= Label (Etat,text="a = %s" %repA).place(x=10,y=hauteur/2,height=25,width=50)
                FinB= Label (Etat,text="b = %s" %repB).place(x=10,y=hauteur/2+38,height=25,width=50)
                FinC= Label (Etat,text="c = %s" %repC).place(x=10,y=hauteur/2+76,height=25,width=50)
                FinD = Label (Etat,text="Delta = %s" %repD).place(x=110,y=hauteur/2,height=25,width=90)
                FinnbrSol = Label (Etat,text="Nombre de\n solution : %s" %repnbrSol).place(x=110,y=hauteur/2+28,height=75,width=75)
                ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
                Sol1 = Entry(Etat,textvariable=utilSol1).place(x=60,y=hauteur/2+106,height=25,width=50)
                Sol2 = Entry(Etat,textvariable=utilSol2).place(x=190,y=hauteur/2+106,height=25,width=50)
                IndSol1 = Label (Etat,text="x' = ").place(x=10,y=hauteur/2+106,height=25,width=50)
                IndSol2 = Label (Etat,text="x\" = ").place(x=140,y=hauteur/2+106,height=25,width=50)
                ValABC = Button(Etat,text="ok",command=lambda:calcul("Delta4",2)).place(x=250,y=hauteur/2+106,height=25,width=35)


        else :
            texte = "Non ce n'est pas cela"
            stat(1)
            calcul("Delta2",1)

    if mode == "Delta4" :
        # cette fois la variable "essais" à été détourné de son utilisation afin de différencier l'équation à un solution de celle à deux solution

        repSol1 = utilSol1.get()
        repSol2 = utilSol2.get()

        if essais == 1 : # une solution

            if repSol1 == str(reelSol1) :

                texte = "Bien !! tu à résolu cette équation !"
                FinA= Label (Etat,text="a = %s" %repA).place(x=10,y=hauteur/2,height=25,width=50)
                FinB= Label (Etat,text="b = %s" %repB).place(x=10,y=hauteur/2+38,height=25,width=50)
                FinC= Label (Etat,text="c = %s" %repC).place(x=10,y=hauteur/2+76,height=25,width=50)
                FinD = Label (Etat,text="Delta = %s" %repD).place(x=110,y=hauteur/2,height=25,width=90)
                FinnbrSol = Label (Etat,text="Nombre de\n solution : %s" %repnbrSol).place(x=110,y=hauteur/2+28,height=75,width=75)
                FinSol1 = Label (Etat,text="x' = %s" %reelSol1).place(x=10,y=hauteur/2+106,height=25,width=25)
                ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
                reboot = Button(Etat,text="Recommencer",command=recommencer).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)

            else :
                texte = "Non ce n'est pas la bonne solution"
                stat(1)
                calcul("Delta3",1)

        if essais == 2 : # deux solutions

            if str(reelSol1) == repSol1 or str(reelSol1) == repSol2 :

                if str(reelSol2) == repSol1 or str(reelSol2) == repSol2 :

                    texte = "Bien !! tu à résolu cette équation !"
                    FinA= Label (Etat,text="a = %s" %repA).place(x=10,y=hauteur/2,height=25,width=50)
                    FinB= Label (Etat,text="b = %s" %repB).place(x=10,y=hauteur/2+38,height=25,width=50)
                    FinC= Label (Etat,text="c = %s" %repC).place(x=10,y=hauteur/2+76,height=25,width=50)
                    FinD = Label (Etat,text="Delta = %s" %repD).place(x=110,y=hauteur/2,height=25,width=90)
                    FinnbrSol = Label (Etat,text="Nombre de\n solution : %s" %repnbrSol).place(x=110,y=hauteur/2+28,height=75,width=75)
                    FinSol1 = Label (Etat,text="x' = %s" %reelSol1).place(x=10,y=hauteur/2+106,height=25,width=100)
                    FinSol2 = Label (Etat,text="x\" = %s" %reelSol2).place(x=140,y=hauteur/2+106,height=25,width=100)
                    ABC = Label (Etat,text=texte,fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
                    reboot = Button(Etat,text="Recommencer",command=recommencer).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)

                else :
                    texte = "Non tu a fait une erreur ! "
                    stat(1)
                    calcul("Delta3",1)
            else :
                texte = "Non tu a fait une erreur ! "
                stat(1)
                calcul("Delta3",1)


def bouton(reponse):
    """Fonction vérifiant si la réponse à "doit-je utiliser delta ?" est correcte ou non"""
    Btnnon.place_forget()
    Btnoui.place_forget()
    correction = ""
    global a,b,c,x,y

    if reponse == 1 :

        if b == 0 and c != 0 :

            if -c/a >= 0 :
                x = sqrt(-c/a)
                y = -sqrt(-c/a)
                correction = "Non, \n tu n'est pas obliger de faire delta.\n Continue et trouve le résultat"
                continuer = Button(Init,text="Continuer",command=lambda:calcul("Cas1",0)).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)
                stat(1)


            else :
                correction = "Non, \n tu n'est pas obliger de faire delta.\n Continue et trouve le résultat"
                continuer = Button(Init,text="Continuer",command=lambda:calcul("Cas1",0)).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)
                stat(1)

        if c == 0 and b != 0 :
            x = 0
            y = -b/a
            correction = "Non, \n tu n'est pas obliger de faire delta. \n Continue et trouve le résultat"
            continuer = Button(Init,text="Continuer",command=lambda:calcul("Cas2",0)).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)
            stat(1)

        if c == 0 and b == 0 :
            x = 0
            correction = "Non, \n tu n'est pas obliger de faire delta. \n Continue et trouve le résultat"
            continuer = Button(Init,text="Continuer",command=lambda:calcul("Cas3",0)).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)
            stat(1)

        if b != 0 and c != 0:
            x = (b*b)-(4*a*c)
            correction = "Bien ! \n maintenant applique delta et trouve le résultat"
            continuer = Button(Init,text="Continuer",command=lambda:calcul("Delta",0)).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)


    reponse1 = Label (Init,text=correction).place(x=0,y=175,height=85,width=largeur)



    if reponse == 0 :

        if b == 0 and c != 0 :

            if -c/a >= 0 :
                x = sqrt(-c/a)
                y = -sqrt(-c/a)
                correction = "Bien ! \n ici tu n'est pas obliger d'utiliser delta.\n Continue et trouve le résultat"
                continuer = Button(Init,text="Continuer",command=lambda:calcul("Cas1",0)).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)

            else :
                correction = "Bien ! \n ici tu n'est pas obliger d'utiliser delta"
                continuer = Button(Init,text="Continuer",command=lambda:calcul("Cas1",0)).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)

        if c == 0 and b != 0 :
            x = 0
            y = -b/a
            correction = "Bien ! \n ici tu n'est pas obliger de faire delta.\n Continue et trouve le résultat"
            continuer = Button(Init,text="Continuer",command=lambda:calcul("Cas2",0)).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)

        if c == 0 and b == 0 :
            x = 0
            correction = "Bien ! \n ici tu n'est pas obliger de faire delta.\n Continue et trouve le résultat"
            continuer = Button(Init,text="Continuer",command=lambda:calcul("Cas3",0)).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)

        if b != 0 and c != 0:
            x = (b*b)-(4*a*c)
            correction = "Non, \n ici tu ne peut pas trouvé le résultat sans delta \n maintenant applique delta et trouve le résultat"
            continuer = Button(Init,text="Continuer",command=lambda:calcul("Delta",0)).place(x=largeur/2-56,y=hauteur/2-25,height=25,width=112)
            stat(1)

    reponse1 = Label (Init,text=correction).place(x=0,y=175,height=85,width=largeur)

def openframe() :
    global minijeu_1,Init,equation,question,Btnnon,Btnoui,largeur,hauteur,points
    minijeu_1 = Tk()
    Init = Frame(minijeu_1)
    minijeu_1.title ("Trouve les illuminatis !")
    largeur,hauteur = 310,270
    minijeu_1.geometry ("%sx%s" %(largeur,hauteur))
    minijeu_1.minsize (height=hauteur,width=largeur)
    minijeu_1.maxsize (height=hauteur,width=largeur)
    init()
    stat(0)
    equation = Label (Init,text=f).place(x=0,y=20,height=25,width=largeur)
    question = Label (Init,text="Doit-je utiliser Delta ?",fg="red").place(x=0,y=hauteur/4,height=25,width=largeur)
    Indpoints = Label (Init,text="points : "+str(points)+"/10",fg="red").place(x=largeur-100,y=0,height=25,width=100)
    Btnoui = Button(Init,text="Oui",command=lambda:bouton(1))
    Btnoui.place(x=largeur/2-75,y=hauteur/2-25,height=25,width=75)
    Btnnon = Button(Init,text="Non",command=lambda:bouton(0))
    Btnnon.place(x=largeur/2,y=hauteur/2-25,height=25,width=75)
    Btnquitter = Button(Init,text="Quitter",command=quitter)
    Btnquitter.place(x=0,y=0,height=25,width=75)
    Init.place(x=0,y=0,height=hauteur,width=largeur)
    minijeu_1.mainloop()

openframe()