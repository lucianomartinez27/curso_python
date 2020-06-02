#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Codifique un nuevo módulo con el nombre ejercicio12.py. Cree dentro del
módulo un diccionario con al menos diez códigos postales de localidades de la provincia
Entre Ríos. Listado de localidades y códigos:
"""

cp_entre_rios = {3150:'NOGOYA', 3138:'ALCARAZ', 3142:'BOVRIL', 3116:'CRESPO',\
                 3105:'DIAMANTE', 3206:'FEDERACIÓN', 3164:'GENERAL RAMÍREZ', \
                 3281:'PUEBLO LIEBIG', 3107:'SAN BENITO', 3100:'PARANÁ'}

"""
Codifique el módulo del ejercicio anterior para mostrar en pantalla el listado de
índices y el listados de valores del diccionario.
"""

print(cp_entre_rios.keys())
print(cp_entre_rios.values())

"""
Modifique el módulo del ejercicio anterior para agregar una nueva localidad
(3114 ALDEA MARIA LUISA) en el diccionario
"""
cp_entre_rios[3114] = 'ALDEA MARIA LUISA'

"""
Modificar nuevamente el módulo del ejercicio anterior para crear un nuevo
diccionario de localidades y códigos. 
"""
nuevos_cp = {3101:'ALDEA SALTO', 2826:'ALDEA SAN ANTONIO'}

"""
Después de crear el nuevo diccionario debe agregar el mismo al diccionario ya
creado con las localidades anteriores. Puede utilizar el método update(). Finalmente, debe
mostrar los elementos del diccionario.
"""
cp_entre_rios.update(nuevos_cp)
print(cp_entre_rios)

"""
Modificar nuevamente el módulo del ejercicio anterior para copiar el
diccionario y luego borrar los elementos del diccionario original. Para terminar debe
mostrar los elementos de ambos diccionarios.
"""
copia_dic = cp_entre_rios.copy()
cp_entre_rios.clear()
print(cp_entre_rios)
print(copia_dic)
