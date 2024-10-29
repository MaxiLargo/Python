from queue import LifoQueue as Pila
import random
def generar_nros_al_azar(cantidad : int,desde : int, hasta : int) -> Pila[int]:
    p:Pila = Pila()
    for _ in range(0,cantidad):
        valor:int = random.randint(desde, hasta)
        p.put(valor)
    return p

print(generar_nros_al_azar(10,1,20))

def cantidad_elementos(p : Pila)->int:
    paux:Pila = Pila()
    longitud:int = 0
    while not p.empty():
        longitud+=1
        v=p.get()
        paux.put(v)
    while not paux.empty():
        p.put(paux.get())
    
    return longitud

p:Pila = Pila()
p.put(1)
p.put(2)
p.put(3)
p.put(4)
print(cantidad_elementos(p))