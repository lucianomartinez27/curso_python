#!/usr/bin/env python3
#-*- coding: utf-8 -*- 

"""
Codificar una clase de nombre InvertirCadena que permita iterar la cadena de
forma invertida (del último carácter al primero). Recuerde debe lanzar una excepción
(StopIteration) para detener la iteración.
"""

class InvertirCadena:
    """Clase que permite iterar una cadena de forma invertida"""
    def __init__(self, datos):
        if isinstance(datos, str):
            self.datos = datos
            self.indice = len(datos)
        else:
            raise TypeError('El dato a ingresar debe ser de tipo String')
    def __iter__(self):
        return self
    def __next__(self):
        if self.indice == 0:
            raise StopIteration
        self.indice = self.indice - 1
        return self.datos[self.indice]

