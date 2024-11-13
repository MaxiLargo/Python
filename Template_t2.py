from queue import Queue as Cola


def pertenece(x:str,y:dict[str, list[tuple[str,int]]])->bool:
    res:bool = False
    for i in y.keys():
        if x == i:
            res=True
    return res




# Ejercicio 1
def gestion_ventas(ventas_empleado_producto: list[tuple[str, str, int]]) -> dict[str, list[tuple[str,int]]]:
    ventas:dict[str,list[tuple[str,int]]]={}
    for empleado,producto,cantidad in ventas_empleado_producto:
        if not pertenece(empleado,ventas):
            ventas[empleado]=[(producto,cantidad)]
        else:
            ventas[empleado].append((producto,cantidad))
    
    return ventas

print(gestion_ventas([("Juan","A",10),("Mateo","B",5),("Juan","B",5)])) 
 

def hallardigitos(x:int)->int:
    contador:int=0
    while not x == 0:
        digito:int=x%10
        if not digito%2 ==0:
             contador+=1
        x=x//10
    return contador

print(hallardigitos(1354))


# Ejercicio 2
def cantidad_digitos_impares(numeros: list[int])->int:
    res:int=0
    for i in numeros:
        res=hallardigitos(i)+res
    return res

print(cantidad_digitos_impares([57, 2383, 812, 246]))


# Ejercicio 3


def reordenar_cola_primero_numerosas(carpetas: Cola[tuple[str,int]], umbral:int) -> Cola[tuple[str,int]]:

    colamayorqueumbral=Cola()
    colamenorigualqueumbral=Cola()
    colaaux=Cola()
    res=Cola()
    while not carpetas.empty():
        pagina=carpetas.get()
        if pagina[1]>umbral:
            colamayorqueumbral.put(pagina)
        else:
            colamenorigualqueumbral.put(pagina)
        colaaux.put(pagina)
    while not colamayorqueumbral.empty():
        res.put(colamayorqueumbral.get())
    while not colamenorigualqueumbral.empty():
        res.put(colamenorigualqueumbral.get())
    while not colaaux.empty():
        carpetas.put(colaaux.get())
    
    return res

c=Cola()
c.put(("id1",35))
c.put(("id2",5))
c.put(("id3",65))
c.put(("id4",1))
c.put(("id5",44))


# Ejercicio 4

def maximodelista(x:list[int])->int:
    maximo:int=x[0]
    for i in x:
        if i>maximo:
            maximo=i
    return maximo

def transformada(x:list[list[int]])->list[list[int]]:
    res=[]
    
    for i in range(len(x)):
        res1=[]
        for j in range(len(x)):
            res1.append(x[j][i])
        res.append(res1)
    return res

# [[9,2,3],[1,1,2],[2,2,1]]
def matriz_cuasi_decreciente(matriz: list[list[int]]) -> bool:
    res:bool = True
    lista=matriz.copy()
    transformada(lista)
    for i in range(len(lista)-1):
        for _ in range(len(lista[i])-1):
            if not maximodelista(lista[i]) > maximodelista(lista[i+1]):
                res=False
    return res
