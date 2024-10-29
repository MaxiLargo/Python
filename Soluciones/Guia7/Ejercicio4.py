def nombredealumnos()->list[str]:
    res:list = []
    nombre:str = input("Ingrese nombre de estudiante: ")
    while nombre != "" or nombre != "listo":
        res.append(nombre)
    
    return res

print(nombredealumnos())