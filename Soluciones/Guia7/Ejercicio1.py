def pertenece (s:list,e:int)->bool:
    res:bool = False
    if e in s:
        res = True
    return res


def pertenece1 (s:list,e:int)->bool:
    res:bool = False
    for numero in s:
        if e == numero:
            res = True
    return res


def pertenece2 (s:list,e:int)->bool:
    res:bool = False
    while len(s) > 0:
        if e == s[len(s)-1]:
            res = True
            s.remove(len(s))
        else:
            s.remove(len(s))
    return res


def divide_a_todos(s:list,e:int)->bool:
    i:int = 0
    res:bool = False
    scopy:list = s.copy()
    for k in scopy:
        if k % e == 0:
            i+=1
    if len(s) == i:
        res = True
    return res


def suma_total(s:list)->int:
    i:int=0
    for k in s:
        i=k+i
    return i 



def maximo(s:list)->int:
    i:int=0
    for k in s:
        if k>i:
            i=k
    return i



def minimo(s:list)->int:
    i:int=s[0]
    for k in s:
        if k<i:
            i=k
    return i

def ordenados(s:list)->bool:
    lista:list = []
    lista2:list = s.copy()
    res:bool = False
    for i in s:
        lista.append(minimo(lista2))
        lista2.remove(minimo(lista2))

    if lista == s:
        res = True
    return res


def pos_maximo(s:list)->int:
    res:int = -1

    for i in range(len(s)):
        if i == maximo(s):
            res = i 
    
    return res

print(pos_maximo([1,1,2,3,1,5]))

def pos_minimo(s:list)->int:
    res:int = -1

    for i in range (len(s)):
        if i == minimo(s):
            res = i
    return res 

def mayor(s:list[str])->bool:
    res:bool = False

    for i in s:
        if len(i) > 7:
            res = True
    return res 


def hay3repetidos(s:list)->bool:
    res:bool = False

    for i in range(len(s)-2):
        if s[i] == s[i+1] and s[i] == s[i+2]:
            res = True
    return res 

print(hay3repetidos([3,4,3,5,4,1,1,1,3,4]))


def hay3vocalesdistintas(palabra:str)->bool:
    res:bool = False
    k:int = 0
    vocales:list = ["a","e","i","o","u"]
    for i in palabra:
        if i in vocales:
            vocales.remove(i)
            k+=1
    if k >= 3:
        res = True
    return res

print(hay3vocalesdistintas("Mamutuuuuui"))


def secuenciamaslarga(s:list)->bool:
    