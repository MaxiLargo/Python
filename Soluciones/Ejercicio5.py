import Ejercicio2 as importado
def devolver_el_doble_si_es_par(numero:int)->int:
    res:int = 0
    if importado.es_par(numero):
        res = numero*2
    else:
        res = numero
    return res

print(devolver_el_doble_si_es_par(6))

def devolver_el_doble_si_es_par(numero:int)->int:
    res:int=0
    if importado.es_par(numero):
        res = numero
    else:
        res = numero + 1

    return res 

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero):
    res:int = 0
    if numero % 3:
        res = numero * 2
    elif numero % 9:
        res = numero * 3
    else:
        res = numero
    return res 

def lindo_nombre(nombre:str)->str:
    res:str = ""
    if len (nombre) >= 5:
        res = "Tu nombre tiene muchas letras!"
    else:
        res = "Tu nombre tiene menos de 5 caracteres"
    return res 

def elRango(numero:int)->str:
    res:str=""
    if numero < 5:
        res = "Menor a 5"
    elif numero>=10 and numero<=20:
        res = "Entre 10 y 20"
    else:
        res = "Mayor a 20"
    return res

def tejubilasono(genero:str,edad:int):
    res:str = ""
    if genero == "F":
        if edad>=60 or edad<=18:
            res = "Anda de vacaciones"
        else:
            res = "Anda a trabajar"
    if genero == "M":
        if edad>=60 or edad <=18:
            res = "Anda de vacaciones"
        else:
            res = "Anda a trabajar"
    return res

