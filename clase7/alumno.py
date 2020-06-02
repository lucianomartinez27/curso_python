#!/usr/bin/env/ python3
#-*- coding: utf-8 -*-

"""Ejercicio: Hacer un nuevo módulo, llamado alumno.py que tenga como atributos un
número de legajo, tres notas parciales y una nota promedio. Hacer un método que permita
calcular y mostrar el promedio del alumno según las tres calificaciones parciales. Realizar
otro método que permita mostrar el estado del alumno según la calificación promedio
(menor que 6 es alumno libre, entre 6 y 8 alumno regular y mayor a 8 alumno
promocionado)."""

class Alumno:
    """Objeto de tipo Alumno, debe inicializarse con número de legajo, 
    además de tres notas parciales"""
    def __init__(self, nlegajo, n1, n2, n3):
        self.nlegajo = nlegajo
        self.notas_parciales = (n1, n2, n3)
        self.promedio = self.nota_promedio()
    def nota_promedio(self):
        total = 0
        for i in self.notas_parciales:
            total += i
        return total/len(self.notas_parciales)
    def estado_alumno(self):
        if self.promedio < 6:
            print(f'Alumno con legajo {self.nlegajo}: libre')
        elif self.promedio <= 8:
            print(f'Alumno con legajo {self.nlegajo}: regular')
        else:
            print(f'Alumno con legajo {self.nlegajo}: promocionado')
