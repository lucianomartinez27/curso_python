#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
- Tomar como base el módulo del punto anterior para mostrar el valor y el tipo de
variable por pantalla (haga uso de type()). Guardar el módulo con el nombre ejercicio6.py.
"""

entero = 2
decimal = 3.5
booleano = True
cadena = 'cadena de texto'
complejo = 2 + 3j

print(entero, 'es de tipo:', type(entero))
print(decimal, 'es de tipo:', type(decimal))
print(booleano, 'es de tipo:', type(booleano))
print(cadena, 'es de tipo:', type(cadena))
print(complejo, 'es de tipo:', type(complejo))


""" Agregar al módulo anterior la posibilidad de mostrar los métodos de cada tipo
de dato utilizando la función integrada dir()."""

print(dir(entero),
      dir(decimal),
      dir(booleano),
      dir(cadena),
      dir(complejo))
