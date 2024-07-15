# coding:utf-8

while True:

    try:
        test = int(input("Entrer le nombre de cas de test: "))

    except ValueError:
        print("something wrong !! ")
        break
    else:
        chaine = []
        if 1 <= test <= 500:
            for i in range(test):

                chaine.append(input(f"Enter Nom {i+1}: "))

        else:
            print("le nombre de cas de test doit etre entre 1 et 500 ")

    for N in chaine:
        if len(N) > 1000 or len(N) < 1:
            print("Error !! votre nom doit etre comprise entre 1 et 1000 ")
            break

        dic = {1: ['a', 'j', 's'], 2: ['b', 'k', 't'],
               3: ['c', 'l', 'u'], 4: ['d', 'm', 'v'],
               5: ['e', 'n', 'w'], 6: ['f', 'o', 'x'],
               7: ['g', 'p', 'y'], 8: ['h', 'q', 'z'],
               9: ['i', 'r']}

        somKeys = 0
        for cle, valeur in dic.items():

            for char in N:
                if char in valeur:

                    somKeys += cle

        def sommeChiffre(valeurTrouver):

            nbre = 10
            while True:
                som = 0
                for i in str(valeurTrouver):

                    som += int(i)
                valeurTrouver = som

                if som < nbre:
                    break
            return som

        def voyelles(valeurEntree):

            voyelles = ['a', 'o', 'i', 'y', 'e', 'u']
            chaine = []

            for caractere in valeurEntree:
                if caractere in voyelles:
                    chaine.append(caractere)

            somkeysVoyelles = 0
            for key, value in dic.items():
                for char in chaine:
                    if char in value:

                        somkeysVoyelles += key
            return sommeChiffre(somkeysVoyelles)

        def consonnes(valeurEntree):

            voyelles = ['a', 'o', 'i', 'y', 'e', 'u']
            chaine = []

            for caractere in valeurEntree:
                if caractere not in voyelles:
                    chaine.append(caractere)

            somkeysConsonnes = 0
            for key, value in dic.items():
                for char in chaine:
                    if char in value:

                        somkeysConsonnes += key
            return sommeChiffre(somkeysConsonnes)

        defintion = {0: 'ouroboros', 1: 'individualite', 2: 'interaction', 3: 'completude',
                     4: 'stabilite', 5: 'instabilite', 6: 'harmonie', 7: 'empathie', 8: 'succes', 9: 'completude2'}

        print(N.replace(" ", ""), defintion[sommeChiffre(somKeys)],
              defintion[voyelles(N)], defintion[consonnes(N)])

    try:
        choix = int(
            input("Voulez-vous effectuer un autre test  ? \n 1. Oui \n 2. Non \n"))

    except ValueError:
        print("something wrong !! ")
        break
    else:
        if choix != 1 and choix != 2:
            print("something wrong !! ")
            break
        elif choix == 2:
            print(" Au revoir ")
            break
