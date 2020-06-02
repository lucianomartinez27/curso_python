#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ejercicios: 

 1) Crear un módulo con la definición de una clase llamada Persona que tendrá
como atributos (variables) nombres, apellido y profesión. Por otro lado, se deberá definir
un método que mostrará en la pantalla los nombres y los apellidos de la persona
separados por coma. Guardar el archivo del módulo con el nombre persona.py.

 2) Modificar el módulo del primer ejercicio para establecer la edad de la persona y
agregar un método que permita saber si la persona es mayor de edad (debe informar si la
edad es mayor o igual a 18 años).

 3) Agregar un nuevo atributo denominado numero_documento a la clase Persona
definida en el punto 1 de la presente práctica. Incorporar el método especial __init__()
para inicializar el estado de cualquier objeto Persona con el número de documento.
Finalmente, se propone agregar un nuevo método que permita imprimir por pantalla el
número de documento de la persona.
"""


class Persona:
    """ Crea un objeto de tipo persona, con los atributos nombre,
        apellido, edad, profesion. Debe inicializarse con un número
        de documento """

    nombre = 'Default'
    apellido = 'Default'
    profesion = 'Default'
    edad = 0

    def __init__(self, documento):
        self.documento = documento

    def __str__(self):
        return (f"Nombre: {self.nombre}, Apellido: {self.apellido}, Profesión: {self.profesion}, Edad: {self.edad}")

    def mayor_de_edad(self):
        if self.edad > 18:
            print(f'{self.nombre} {self.apellido} es mayor de 18 años.')
        elif self.edad == 18:
            print(f'{self.edad} {self.apellido} tiene 18 años.')
        else:
            print(f'{self.edad} {self.apellido} es menor de 18 años')
    def ver_dni(self):
        print(f'El DNI de {self.nombre} {self.apellido} es: {self.documento}')
