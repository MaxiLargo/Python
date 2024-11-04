from queue import Queue as Cola
import random
from collections import deque

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


# c:Cola = Cola()
# c.put(1)
# c.put(64)
# c.put(3)
# c.put(4)
# c.put(5)

# print(cantidad_elementos(c))

def buscar_el_maximo(c:Cola[int])->int:
    caux:Cola[int]=Cola()
    s=c.get()
    caux.put(s)
    while not c.empty():
        v:int = c.get()
        if v > s:
            s=v
        caux.put(v)
    while not caux.empty():
        c.put(caux.get())

    return s
    

c:Cola = Cola()
c.put(1)
c.put(64)
c.put(3)
c.put(4)
c.put(5)

print(buscar_el_maximo(c))



def buscar_nota_minima(c:Cola[str,int])->int:
    caux:Cola[str,int]=Cola()
    s:int = c.get()
    caux.put(s)
    nota:int = s[1]
    while not c.empty():
        v:int = c.get()
        notamenor:int = v[1]
        if notamenor < nota:
            s=v
            nota=notamenor
        caux.put(v)
    
    while not caux.empty():
        c.put(caux.get())

    return s
        


c:Cola = Cola()
c.put(("Ana", 70))
c.put(("Juan", 85))
c.put(("Luis", 90))
c.put(("Sofia", 75))


print(buscar_nota_minima(c))

def intercalar(c1:Cola,c2:Cola)->Cola:
    caux1:Cola[int]=Cola()
    caux2:Cola[int]=Cola()
    res:Cola[int]=Cola()
    while not c1.empty() and not c2.empty():
        c:int = c1.get()
        v:int = c2.get()

        res.put(c)
        res.put(v)

        caux1.put(c)
        caux2.put(v)
    while not caux1.empty() and not caux2.empty():
        c1.put(caux1.get())
        c2.put(caux2.get())
    
    return res

x:Cola[int] = Cola()
y:Cola[int] = Cola()

x.put(1)
x.put(3)
y.put(2)
y.put(4)

print(intercalar(x,y))


def armar_secuencia_de_bingo()->Cola[int]:
    return generar_nros_al_azar(12,0,99)

print(armar_secuencia_de_bingo())

# def jugar_carton_del_bingo(carton:list,bolillero:Cola[int])->int:
#     jugadas:int=0
#     numeros_marcados:int=0
#     bolillero_aux:Cola[int]=Cola()

#     #Sigo sacando bolillas hasta que marque todos los numeros
#     while numeros_marcados<12:
#         bolilla_sacada=bolillero.get()
#         bolillero_aux.put(bolilla_sacada)
#         if bolilla_sacada in carton:
#             numeros_marcados+=1
#         jugadas+=1

#     #Una vez que marque todos, paso todas las bolillas restantes al bolillero auxiliar
#     while not bolillero.empty():
#         bolilla_sacada:int = bolillero.get()
#         bolillero_aux.put(bolilla_sacada)

#     #Luego las devuelvo del bolillero auxiliar al original, para que quede igual que al principio        
#     while not bolillero_aux.empty():
#         bolilla_sacada:int  = bolillero_aux.get()
#         bolillero.put(bolilla_sacada)

#     return jugadas



# print(jugar_carton_del_bingo([1,20,21,50,71,22,41,28,9,77,51,91],armar_secuencia_de_bingo()))



def n_pacientes_urgentes(c:Cola[tuple[int,str,str]])->int:
    caux:Cola[int,str,str]=Cola()
    prioridad:int=0
    while not c.empty():
        s:int=c.get()
        caux.put(s)
        paciente:int=s[0]
        if paciente >= 1 and paciente <=3:
            prioridad+=1
    
    while not caux.empty():
        c.put(caux.get())
    
    return prioridad
c:Cola[tuple[int,str,str]]=Cola()
c.put((2, "Juan Perez", "Cardiología"))
c.put((5, "Ana López", "Traumatología"))
c.put((1, "Luis Gómez", "Urgencias"))
c.put((4, "Marta Jiménez", "Pediatría"))

# Llamamos a la función
print(n_pacientes_urgentes(c))  # Output esperado: 2



#Problema atencion en el banco

# problema atencion_cliente(in c :Cola[tuple[str,int,bool,bool]]):Cola[tuple[str,int,bool,bool]]
# requiere: {str || int != 0}
# asegura : Para todo x en c, ordena de menor a mayor si hay prioridad es el primero, sino es preferencial y sino el resto

def atencion_a_clientes(c:Cola[tuple[str,int,bool,bool]])->Cola[tuple[str,int,bool,bool]]:
    colaprioridad:Cola[tuple[str,int,bool,bool]]=Cola()
    colapreferencial:Cola[tuple[str,int,bool,bool]]=Cola()
    colaresto:Cola[tuple[str,int,bool,bool]]=Cola()
    caux:Cola[tuple[str,int,bool,bool]]=Cola()
    res:Cola[tuple[str,int,bool,bool]]=Cola()

    while not c.empty():
        v:tuple[str,int,bool,bool]=c.get()
        if v[2]:
            colaprioridad.put(v)
        if v[3] and not v[2]:
            colapreferencial.put(v)
        if not v[2] and not v[3]:
            colaresto.put(v)
        
        caux.put(v)
    
    while not colaprioridad.empty():
        res.put(colaprioridad.get())
    
    while not colapreferencial.empty():
        res.put(colapreferencial.get())
    
    while not colaresto.empty():
        res.put(colaresto.get())
    
    while not caux.empty():
        c.put(caux.get())
    
    return res



# Ejemplo 1: Clientes con diferentes combinaciones de atributos
c1=Cola()
c1.put(("Juan Pérez", 12345678, False, True))      # Cliente con prioridad
c1.put(("Ana López", 87654321, True, False))      # Cliente preferencial
c1.put(("Carlos García", 56781234, False, False))  # Cliente general
c1.put(("María Soto", 34567890, True, True))      # Cliente preferencial con prioridad
c1.put(("Lucía Díaz", 23456789, False, False))     # Cliente general
c1.put(("Pedro Méndez", 34567812, False, True))     # Cliente con prioridad


# Ejecutar la función
print(atencion_a_clientes(c1))  # Debería imprimir True