# coding:utf-8


# Malal DIA             220600
# Souleymane SALL       220651


print("""" _____        .__               .__          __         .__                \n
\_   ___ \_____  |  |   ____  __ __|  | _____ _/  |________|__| ____  ____    \n
/    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \\   __\_  __ \  |/ ___\/ __ \   \n
\     \____/ __ \|  |_\  \___|  |  /  |__/ __ \|  |  |  | \/  \  \__\  ___/   \n
 \______  (____  /____/\___  >____/|____(____  /__|  |__|  |__|\___  >___  >  \n
        \/     \/          \/                \/                    \/    \/  """)

while True:
    try:
        print("-------- CALCULATRICE SCIENTIFIQUE ---------- ")
        print(" ")
        print("1 - Addition/Soustraction")
        print("2 - Modulo ")
        print("3 - Multiplication ")
        print("4 - Division ")
        print("5 - Puissance ")
        print("6 - Factoriel ")
        print("7 - Logarithme Népérien ")
        print("8 - Exponentiel ")
        print("9 - Racine Carrée ")
        print("0 - Quitter ")
        print(" ")
        choix = int(
            input(" Veuillez saisir un numéro correspondant à l'option de votre choix: "))
    except ValueError:
        print("Something wrong !! ")
    else:

        match choix:
            case 1:
                print("---- Addition/Soustraction ---- ")
                print(" ")
                try:
                    nterme = int(
                        input("Entrer le nombre de termes (au moins 2) : "))
                    if nterme < 2:
                        print(
                            "Veuillez entrer un nombre positif et un nombre de termes (au moins 2) ")
                        continue
                except ValueError:
                    print("something wrong !! ")
                    continue
                else:
                    i = 0
                    s = 0
                    while i < nterme:
                        nbre = float(input(f"Entrer nombre {i+1} "))
                        i += 1
                        if nbre > 0:
                            s = s+nbre
                        else:
                            s = s+(nbre)
                print("le résultat est : {}".format(s))

            case 2:
                print("----- Modulo -----")
                print(" ")
                try:
                    dividende = int(input("Entrer le dividende: "))
                    diviseur = int(input("Entrer le diviseur: "))
                except ValueError:
                    print("something wrong !!")
                else:
                    while diviseur == 0:
                        diviseur = int(input(
                            "Error !! le diviseur doit etre different de zéro (Veuillez réessayer svp ) : "))

                    q = dividende//diviseur
                    r = dividende-(q*diviseur)

                    print("le reste est : {}".format(r))

            case 3:
                print("----- Multiplication -----")
                print(" ")

                try:

                    nfacteurs = int(
                        input("Entrer le nombre de facteurs (au moins 2) : "))
                    if nfacteurs < 2:
                        print(
                            "Erreur, entrer un nombre positif et un nombre de termes (au moins 2) ")
                        continue
                except ValueError:
                    print("Something wrong !! ")

                else:
                    m = 1
                    for i in range(1, nfacteurs+1):
                        nbre = float(input(f"Entrer nombre {i}: "))
                        if nbre > 0:
                            m = m*nbre
                        else:
                            m = m*(nbre)
                    print("le résultat est : {}".format(m))

            case 4:
                print("----- Division ----- ")
                print(" ")
                try:
                    dividende = float(input("Entrer le dividende: "))
                    diviseur = float(input("Entrer le diviseur: "))
                except ValueError:
                    print("Something wrong !! ")
                else:
                    while diviseur == 0:
                        diviseur = float(input(
                            "Error !! le diviseur doit etre différent de zéro, Veuillez réessayer svp : "))
                    resultat = dividende/diviseur

                    print("le résultat est : {}".format(resultat))

            case 5:
                print("----- Puissance ----- ")
                print(" ")

                try:
                    x = float(input("Entrer un nombre x: "))
                    n = int(input("Entrer n l'exposant de n: "))

                except ValueError:
                    print("Something wrong !! ")
                else:
                    if n >= 1:
                        p = 1
                        for i in range(1, n+1):

                            p *= x
                        print(f"{x} à la puissance {n} = {p}")
                    elif x != 0 and n == 0:
                        p = 1
                        print(f"{x} à la puissance {n} = {p}")
                    elif x != 0 and n < 0:
                        n = -(n)
                        p = 1
                        for i in range(1, n+1):
                            p *= x

                        print(f"{x} à la puissance -{n} = {1/p}")
                    else:
                        print("impossible Veuillez réessayer svp ")

            case 6:
                print("----- Factoriel ------ ")
                print(" ")

                try:
                    n = int(input("Entrer un nombre: "))
                except ValueError:
                    print("Something wrong !! ")
                else:
                    while n < 0:
                        n = int(
                            input("Error!! Veuillez choisir un nombre supérieur à zéro: "))
                    if n != 0:
                        f = 1
                        for i in range(2, n+1):
                            f *= i
                        print(f"{n}! = {f}")
                    else:
                        print(f"{n}! = 1")

            case 7:
                print("----- Logarithme Népérien ------")
                print(" ")
                while True:

                    try:
                        x = float(input("Entrer un nombre x>0:  "))
                    except ValueError:
                        print("Something wrong !! ")
                    else:

                        if 0 < x <= 2:
                            k = 1
                            s = l = 0
                            while k <= 10:
                                s = (-1)**(k+1)*(x-1)**k/k
                                l = l+s
                                k = k+1
                            print(f"ln({x}) = {l}")
                        elif x > 2:
                            cpt = 0
                            b = 2
                            while cpt <= 2:
                                while True:

                                    q = x/b
                                    x = q
                                    q = x
                                    cpt += 1
                                    if 0 < q and q <= 2:
                                        break
                            k = 1
                            sq = sb = lq = lb = 0
                            b = 2
                            while k <= 10:
                                sq = (-1)**(k+1)*(q-1)**k/k
                                lq += sq
                                sb = (-1)**(k+1)*(b-1)**k/k
                                lb += sb
                                k += 1
                            lqb = lq+(cpt*lb)

                            print(lqb)

                        else:
                            print("Error !! ")
                        if x > 0:
                            break
            case 8:
                print("------ Exponentiel ------- ")
                print(" ")

                try:
                    x = float(input("Entrer un nombre "))
                except ValueError:
                    print("Something wrong !! ")
                else:
                    def fact(n):
                        f = 1
                        for i in range(2, n+1):
                            f *= i
                        return f

                    s = ex = k = 0
                    while k <= 9:
                        s = (x**k)/fact(k)
                        ex += s
                        k += 1
                    print(f"Exp({x}) = {ex}")

            case 9:
                print("------ Racine Carrée -----")
                print(" ")

                k = -1
                while k < 0:
                    try:
                        k = float(
                            input("Entrer un nombre réel supérieur ou égal à zéro: "))

                    except ValueError:
                        print("Something Wrong !! ")
                    else:
                        if k >= 0:
                            def racine(x, x0):
                                y = x-x0
                                if y < 0:
                                    y = -y
                                while y >= 0.00001:
                                    x = 1/2*(x0+(k/x0))
                                    y = x-x0
                                    if y < 0:
                                        y = -y
                                    x0 = x
                                return x

                            if k == 0:
                                x0 = 1/2
                                x = 1

                                print(
                                    f"racine carrée de {k} = {racine(x, x0)}")

                            if k != 0:
                                x0 = k/2
                                x = 2
                                print(
                                    f"racine carrée de {k} = {racine(x, x0)}")

            case 0:
                print(" Au revoir. Merci :) ")

            case _:
                print("Error !! Veuillez un option valide svp ")
    if choix == 0:
        break
