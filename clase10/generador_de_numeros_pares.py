#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Escribir una función generadora de números pares en un nuevo módulo de
nombre generador_de_numeros_pares.py. Probar la función generadora
"""

def generador_numeros_pares(cantidad):
    """función que genera la cantidad de numeros pares que se pase como paramatro"""
    for i in range(cantidad):
        yield  (i+1) * 2

if __name__ == "__main__":
    pares = generador_numeros_pares(10)
    for i in pares:
        print(i)
