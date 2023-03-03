# -*- coding= utf-8 -*-
from math import pi

def area(r):

    if type(r) not in [float, int]:
        raise TypeError("Solo se pueden usar numeros enteros y flotantes")

    if  r<0:
        raise ValueError("No se permiten valores negativos")

    areaC=pi*(r**2)
    return areaC

def sum(x,y):
    #result= x+y
    return x+y
