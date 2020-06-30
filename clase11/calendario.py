#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Genere un módulo que muestre el calendario del mes actual en forma tabular
(calendario.py).
"""

from calendar import month
from time import localtime

# Se toma año y mes de la tupla generada por localtime.
año, mes = (localtime()[0], localtime()[1])

# Imprime el calendario formateado con el mes actual.
calendario = month(año, mes)

print(calendario)

