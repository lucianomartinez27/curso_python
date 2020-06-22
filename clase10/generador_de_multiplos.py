#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Hacer una función generadora que devuelva múltiplos de un número que se le
pasa como parámetro.
"""

def generador_de_multiplos(numero, total_multiplos):
    for i in range(total_multiplos):
        yield numero * (i+1)

if __name__ == "__main__":
    mul = generador_de_multiplos(5, 10)
    for i in mul:
        print(i)

