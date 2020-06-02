#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Crear un nuevo módulo de nombre ejercicio10.py que almacene en una
variable la cadena “Aprendiendo el lenguaje Python”. Utilizando los índices obtenga y
muestre el primer carácter de cada palabra de la cadena de texto.
"""

cadena = "Aprendiendo el lenguaje Python"

cadena = cadena.split()

print(cadena[0][0], cadena[1][0], cadena[2][0], cadena[3][0])


"""
 Modifique el módulo anterior para obtener y mostrar mediante rebanadas
(slices) cada una de las palabras de la cadena de texto.
"""
cadena = "".join(cadena)

print(cadena[0:11], cadena[11:13], cadena[13:21], cadena[21:])

