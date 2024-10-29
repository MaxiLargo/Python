
def nombreestudiantes():
    res:list[str]=[]
    while 1==1:
        nombre:str = input("nombre alumno ")
        if nombre == "":
            return res
        res.append(nombre)

print(nombreestudiantes())
    
def cargasube():
    res:list[(str,int)] = []
    monedero:int=0
    while 1==1:
        operacion:str = input("Movimiento a hacer ")

        if operacion == "C":
            valor:int=int(input("Valor a cargar "))
            res.append(("C",valor))
        elif operacion == "D":
            valor:int=int(input("Valor a descontar "))
            res.append(("D",valor))
        elif operacion == "X":
            return res

print(cargasube())
>>>>>>> 268a4a32330abb53b799e233ccfcf7021f67bdd8
