#! /usr/bin/env/ python3
# -*- coding: utf-8 -*-

class Mate:
    """El objeto de tipo mate describe las características como también
    el funcionamiento de la infusión rioplatense"""

    def __init__(self, n):
        self.cebadas_disponibles = n
        self.lleno = False
    
    def cebar(self):
        if self.lleno:
            print('¡Cuidado! ¡Te quemaste!')
        else:
            self.lleno = True
            print('Cebando')
    
    def beber(self):
        if self.lleno:
            if self.cebadas_disponibles == 0:
                print('Advertencua: El mate está lavado')
            else:
                self.lleno = False
                self.cebadas_disponibles -= 1
                print('Qué rico mate')
        else:
            print('El mate está vacío!')

    def arreglar(self, cebadas_adicionales):
        """ Agrega a las cebadas disponibles la cantidad que se pase como parámetro"""
        self.cebadas_disponibles = cebadas_adicionales

    def __str__(self):
        """Muestra el estado del mate"""
        return 'Te quedan {} cebadas y el mate está {}'.format(self.cebadas_disponibles, ('lleno' if self.lleno else 'vacio'))

    def __eq__(self, otro_mate):
        return self.cebadas_disponibles == otro_mate.cebadas_disponibles \
               and self.lleno == otro_mate.lleno

    def __ne__(self, otro_mate):
        return self.cebadas_disponibles != otro_mate.cebadas_disponibles \
               or self.lleno != otro_mate.lleno
    
    def __lt__(self, otro_mate):
        return self.cebadas_disponibles > otro_mate.cebadas_disponibles \
                or self.lleno > otro_mate.lleno


