# coding:utf-8
from tkinter import *


def ajouter():
    prenom = entryprenom.get()
    nom = entrynom.get()
    telephone = entrytelephone.get()

    with open("/home/papis/myFolders/Documents/codePython/Tkinter/GestionContact/repertoire.txt", "a") as fic:

        fic.write(f"{prenom}\n")
        fic.write(f"{nom}\n")
        fic.write(f"{telephone}\n")

    entryprenom.delete(0, END)
    entrynom.delete(0, END)
    telephone.delete(0, END)


def modifier():
    with open("/home/papis/myFolders/Documents/codePython/Tkinter/GestionContact/repertoire.txt", "r") as fic:

        ligne = fic.readlines()
