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

#Mal
def pertenece2 (s:list,e:int)->bool:
    res:bool = False
    while len(s) > 0:
        if e == s[len(s)-1]:
            res = True
            s.remove(len(s))
        else:
            s.remove(len(s))
    return res

def pertenecev2 (s:list,e:int)->bool:
    res:bool=False
    i:int=0
    while i < len(s):
        if s[i] == e:
            res = True
        i+=1
    return res

print(pertenece([1,2,3,4,4,5,4,4,3],5))




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


#EJ2 eliminar repetidos

def pertenece(s:str,c:chr)->str:
    res:bool = False
    if c in s:
        res = True
    return res

print(pertenece("holaaa","a"))

def eliminar_repetidos(s:str)->str:
    res:str  = ""
    for i in s:
        if pertenece(s,i) and (not pertenece(res,i)):
            res+=i
    return res

print(eliminar_repetidos("Hola"))


def promedio(s:list[int])->float:
    sumapromedio:int=0
    for i in s:
        sumapromedio = sumapromedio + i
    
    promediofinal:float = sumapromedio/len(s)
    
    return promediofinal



def resultadoMateria(notas:list[int])->int:
    notasmayoresque4:bool = True
    res:int= 0
    for i in notas:
        if i < 4:
            notasmayoresque4 = False
            res = 3
    if promedio(notas) >=7 and notasmayoresque4:
        res = 1
    elif promedio(notas) >=4 or promedio(notas) < 7:
        res = 2
    else:
        res = 3
    return res


def historialmovimientos(cuenta:list[tuple])->int:
    res:int = 0

    for (movimiento,dinero) in cuenta:
        if movimiento == "I":
            res=res+dinero
        elif movimiento == "R":
            res=res-dinero
    return res

print(historialmovimientos([("I",
2000), ("R", 20),("R", 1000),("I", 300)]))
        

