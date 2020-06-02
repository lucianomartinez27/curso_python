#! /usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Trabaje con los operadores relacionales en el lenguaje Python. Cree un
módulo nuevo (ejercicio12.py) con el siguiente código:
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

# Comparación igual ==
cinco == cinco
# Comparación distinto !=
cuatro != seis
# Comparación mayor >
cinco > cuatro
# Comparación menor <
nueve < siete
# Comparación menor igual <=
cinco <= ocho
# Comparación mayor igual >=
siete >= siete

"""
Pruebe el funcionamiento y luego haga que se muestre el resultado de las
comparaciones por pantalla
"""

print('5 == 5:', cinco == cinco,
      '\n4 != 6:', cuatro != seis,
      '\n5 > 4:', cinco > cuatro,
      '\n9 < 7:', nueve < siete,
      '\n5 <= 8:', cinco <= ocho,
      '\n7 >= 7:', siete >= siete)
