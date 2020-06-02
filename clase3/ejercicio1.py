#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Crear un módulo nuevo indicando el shebang (#! /usr/bin/env python) y la
codificación en utf8. Guardar el archivo con el nombre ejercicio1.py. Dentro del módulo se
debe crear una lista con las nueve primeras palabras claves del lenguaje Python (primera
columna).
"""

palabras_clave = "False None True and asassert break class continue".split()

"""
Modificar el módulo del primer ejercicio y agregar las siguientes nueve palabras
claves del lenguaje Python (segunda columna). Puede utilizar el método append() o
extend().
"""

palabras_clave.extend("def del elif else except finally for from global".split())

"""
Modificar el módulo del ejercicio anterior para ordenar la lista y luego mostrar la
misma por pantalla.
"""
palabras_clave.sort()

print(palabras_clave)

"""
Editar el módulo del ejercicio anterior para invertir los elementos de la lista.
Luego mostrar por pantalla
"""
palabras_clave.reverse()

print(palabras_clave)

"""
Editar el módulo del ejercicio anterior para obtener el número de índice de al
menos tres palabras claves de la lista. Utilizar el método index()
"""
palabras_clave.index("def")
palabras_clave.index("None")
palabras_clave.index("else")

"""
Nuevamente editar el módulo de ejercicio anterior para eliminar el último
elemento de la lista. Mostrar el contenido de la lista. Luego volver a insertar el elemento a
la lista. Mostrar la lista por pantalla.
"""
pc = palabras_clave.pop(-1)
palabras_clave.insert(-1, pc)
print(palabras_clave)

"""
Nuevamente modificar el módulo de ejercicio anterior para copiar la lista de
palabras reservadas. Luego vaciar la lista original. Mostrar el contenido de las dos listas
por pantalla. Finalmente, vuelva los elementos a la lista inicial de palabras claves.
"""
copia_pc = palabras_clave.copy()
del palabras_clave[:]
print(palabras_clave)
print(copia_pc)
