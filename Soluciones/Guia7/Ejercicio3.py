def pertenece_a_cada_uno_version_1(matriz:list[list[int]],e:int)->list[bool]:
    res:bool = False
    lista:list = []
    n:int = 0
    for i in matriz:
        res = False
        n = 0
        if e in i and n == 0:
            res = True
            n  = 1
            lista.append(res)
        elif e not in i:
            res = False
            lista.append(res)
        
    return lista

print(pertenece_a_cada_uno_version_1([[1,2,3],[3,1,2],[4,4,4]],1))


def es_matriz(s:list[list[int]])->bool:
    longitud0:int = len(s[0])
    res:bool = True

    if len(s)>0:
        if len(s[0])>0:
            for i in range(0,len(s)):
                if len(s[0]) != len(s[i]):
                    res = False
    
    return res
print(es_matriz([[1,2,3],[4,3,1],[4,5,2,1]]))

def minimo (s:list):
    i:int = s[0]

    for j in range (0,len(s)):
        if s[j]<i:
            i = s[j]
    return i



def ordenar(s:list)->list:
    res:list = []
    listaaux:list = s.copy()
    for i in range (0,len(listaaux)):
        res.append(minimo(listaaux))
        listaaux.remove(minimo(listaaux))
    return res

print(ordenar([1,5,2,1,5,6,1,7,9,5]))
            

def filas_ordenadas(s:list[list[int]]):
    ordenadas:bool = False
    res:list = []
    if es_matriz(s):
        for i in range(0,len(s)):
            if s[i] == ordenar(s[i]):
                ordenadas = True
                res.append(ordenadas)
            elif s[i] != ordenar(s[i]):
                ordenadas = False
                res.append(ordenadas)
    return res
print(filas_ordenadas([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))

def columna(m:list[list[int]],e:int)->list[int]:
    res:list=[]

    for i in range(0,len(m)):
        for j in range(0,len(m[i])):
            if j == e:
                res.append(m[i][j])
    return res

print(columna([[1,2,3],[1,2,3],[1,1,1]],1))


def columnas_ordenadas(m:list[list[int]])->list[bool]:
    columnaord:bool=False
    res:list=[]
    n:int = 0 
    for i in range(0,len(m)):
        columnaord = False
        n = 0
        for j in range(0,len(columna(m,i))):
            if columna(m,i) == ordenar(columna(m,i)) and n == 0:
                columnaord=True
                res.append(columnaord)
                n = 1
    return res
print(columnas_ordenadas([[1,2,3],[4,98,6],[7,8,9],[10,11,12]]))