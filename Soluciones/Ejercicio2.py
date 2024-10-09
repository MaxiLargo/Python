def imprimir_saludo(nombre:str)->str:
    return "Hola "+ nombre

print(imprimir_saludo("hola"))

def raizcuadrada(numero:int)->float:
    return numero**(1/2)

print(raizcuadrada(2))

def fahrenheit_a_celsius(temp_far:float)->float:
    return ((temp_far-32)*5)/9

print(fahrenheit_a_celsius(1))

def imprimir_dos_veces(estribillo:str) -> str:
    return estribillo*2

print(imprimir_dos_veces("hola "))


def es_multiplo_de(n:int,m:int)->bool:
    return n%m == 0

print(es_multiplo_de(8,3))

def es_par(numero:int)->bool:
    return es_multiplo_de(numero,2)

print(es_par(5))

def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int)->int:
    return (comensales*min_cant_de_porciones)/comensales
