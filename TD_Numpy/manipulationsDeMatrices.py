# coding:utf-8

import numpy as np

A = np.random.rand(3, 3)
B = np.random.rand(3, 3)

print(f"la somme est : {A+B}")

print(f"le produit est : {A*B}")

produitMatriciel = np.dot(A, B)

determinant = np.linalg.det(A)
if determinant != 0:
    print(f" A est inversible {np.linalg.inv(A)}")
else:
    print("A n'est pas inversible ")
# print(A)
# print(B)
