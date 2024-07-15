# coding:utf-8
import tools

from tkinter import *
from tkinter import messagebox

from tkinter import ttk


fenetre = Tk()
fenetre.title("Gestion Contact ")
fenetre.geometry("1300x700")

labeltitre = Label(fenetre, bd=20, relief=RIDGE, text="GESTION DE CONTACT", font=(
    "Arial", 30), bg="black", fg="white")
labeltitre.place(x=0, y=0, width=1365)

labelPrenom = Label(fenetre, text="PRENOM", font=("Arial", 14), fg="black")
labelPrenom.place(x=0, y=200, width=200)
entryprenom = Entry(fenetre)
entryprenom.place(x=200, y=200, width=200, height=30)

labelNom = Label(fenetre, text="NOM", font=("Arial", 14), fg="black")
labelNom.place(x=0, y=250, width=200)
entrynom = Entry(fenetre)
entrynom.place(x=200, y=250, width=200, height=30)

labelTelephone = Label(fenetre, text="TELEPHONE ",
                       font=("Arial", 14),  fg="black")
labelTelephone.place(x=0, y=350, width=200)
entryTelephone = Entry(fenetre)
entryTelephone.place(x=200, y=350, width=200, height=30)

btnRechercher = Button(fenetre, text="Rechercher", font=(
    "Arial", 14), bg="black", fg="white")
btnRechercher.place(x=30, y=500, width=200)

btnAjouter = Button(fenetre, text="Ajouter", font=(
    "Arial", 14), bg="black", fg="white", command=tools.ajouter)
btnAjouter.place(x=30, y=450, width=200)

btnModifier = Button(fenetre, text="Modifier", font=(
    "Arial", 14), bg="black", fg="white")
btnModifier.place(x=270, y=450, width=200)

btnSupprimer = Button(fenetre, text="Supprimer", font=(
    "Arial", 14), bg="black", fg="white")
btnSupprimer.place(x=270, y=500, width=200)

table = ttk.Treeview(fenetre, columns=(1, 2, 3),
                     height=5, show="headings")
table.place(x=600, y=150, width=760, height=450)

table.heading(1, text="NOM")
table.heading(2, text="PRENOM")
table.heading(3, text="TELEPHONE")

table.column(1, width=50)
table.column(2, width=150)
table.column(3, width=150)
fenetre.mainloop()
