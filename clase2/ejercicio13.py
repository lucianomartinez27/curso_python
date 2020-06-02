#! /usr/bin/env python4
# -*- coding: utf-8 -*-


"""
Trabaje con los operadores lógicos en el lenguaje Python. Cree un módulo
nuevo (ejercicio13.py) con el siguiente código:
"""

# Número entero cuatro
cuatro = 4
# Número entero cinco
cinco = 5
# Número entero sesis
seis = 6
# Número entero siete
siete = 7
# Número entero ocho
ocho = 8
# Número entero nueve
nueve = 9

# Operación lógica conjunción
conjuncion = (cinco + ocho) > cuatro and cinco > siete
# Operación lógica disyunción
disyuncion = (cinco + ocho) > cuatro or nueve > siete
# Operación lógica de negación
negacion = not (cuatro + cinco == nueve)

print('(5 + 8) > 4 and 5 > 7:', conjuncion,
      '\n(5 + 8) > 4 or 5 > 7:', disyuncion,
      '\nnot (4 + 5 == 9):', negacion)
