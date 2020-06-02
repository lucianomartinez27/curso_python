#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Persona:
    def __init__(self, nombre, apellido, profesion, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.profesion = profesion
        self.edad = edad

    def __str__(self):
        return (f"Nombre: {self.nombre}, Apellido: {self.apellido}, Profesión: {self.profesion}, Edad: {self.edad}")

    def mayor_de_edad(self):
        if self.edad > 18:
            print(f'{self.nombre} {self.apellido} es mayor de 18 años.')
        elif self.edad == 18:
            print(f'{self.edad} {self.apellido} tiene 18 años.')
        else:
            print(f'{self.edad} {self.apellido} es menor de 18 años')
