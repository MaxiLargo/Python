def alguno_es_0(numero1, numero2):
    return numero1 == 0 or numero2 == 0

print(alguno_es_0(1,0))

def ambos_son_0(numero1, numero2):
    return numero1 == 0 and numero2 == 0

print(ambos_son_0(1,0))

def es_nombre_largo(nombre:str):
    longitud:int = len(nombre)
    return longitud > 3 and longitud <= 8

print(es_nombre_largo("hola"))

def es_bisiesto(año:int):
    return (año%400 == 0) or (año%4 == 0 and año%100!=0)

print(es_bisiesto(2021))

