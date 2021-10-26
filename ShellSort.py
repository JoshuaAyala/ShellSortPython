#!/usr/bin/python
#coding: utf-8

# Filename  : ShellSort.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/PyMath
# pep8: 100%

def ShellSort(lista, l):

    k = l // 2
    while(k > 0):
        for i in range(k, l):
            x = lista[i]
            y = i
            while(y >= k and lista[y - k] > x):
                lista[y] = lista[y - k]
                y -= k

            lista[y] = x

        k = k // 2
    return lista


c = int(input("¿Cuántos datos deseas ingresar?\n >: "))
lista = []
for i in range(0, c):
    lista.append(int(input("Introduce un dato >: ")))
print("\n   +- Lista dada: ", lista)
l = len(lista)
print("\n   +- Lista ordenada: ", ShellSort(lista, l))