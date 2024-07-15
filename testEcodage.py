# coding:utf-8

import random

chaine = input("entrer votre message : ")

print(" ")

code = []
for i in chaine:

    code.append(ord(i))


def estpremier(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def pgcd(a, b):
    r = a % b
    while r != 0:
        r = a % b
        a = b
        b = r

    return a


nombre = 2
cpt = choix = []
while nombre < 1000:

    if estpremier(nombre):
        cpt.append(nombre)
        choix.append(random.choice(cpt))

    nombre += 1


p = random.choice(choix)
q = random.choice(choix)

n = p * q

euler = (p-1)*(q-1)

choixEntier = 1
while True:
    choixEntier += 1

    if 1 < choixEntier < euler and pgcd(euler, choixEntier) == 1:
        break

e = choixEntier

dCalcul = 0
while True:
    dCalcul += 1

    if (dCalcul*e) % euler == 1:
        break
d = dCalcul
affiche = []
for char in chaine:
    c = ord(char)**e % n
    affiche.append(c)
    print(f"{char} ---> c = {ord(char)}^{e} mod {n} = {c} ")
# print(code)
print(" ")

print("le message chiffré est donc : ", affiche)

print(" ")

dAffiche = []
for caractere in chaine:
    c = ord(caractere)**e % n

    print(f"{ord(caractere)**e % n} ---> caractere = {ord(caractere)**e % n}^{d} mod {n} = {c**d % n} (correspondant à {chr(c**d % n)})")
    dAffiche.append(chr(c**d % n))

print(" ")
print("le message déchiffré est donc : " + " ".join(dAffiche))
