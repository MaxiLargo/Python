from queue import Queue as Cola
import random

def generar_nros_al_azar(cantidad:int,desde:int,hasta:int)->Cola[int]:
    c=Cola()
    for i in range (cantidad):
        c.put(random.randint(desde,hasta))
    
    return c


def cantidad_elementos(c : Cola) ->int:
    caux:Cola = Cola()
    longitud:int = 0
    while not c.empty():
        longitud+=1
        caux.put(c.get())
    
    return longitud



