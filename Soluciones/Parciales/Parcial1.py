# 1) Última aparición
# problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#   requiere: {e pertenece a s }
#   asegura: {res es la posición de la última aparición de e en s}
# }

# TIP: realizar la iteración mediante índices y no mediante elementos

# Por ejemplo, dados
# s = [-1, 4, 0, 4, 100, 0, 100, 0, -1, -1]
# e = 0
# se debería devolver res = 7

# 2) Elementos exclusivos
# problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#   requiere: -
#   asegura: {res tiene todos los elementos que pertenecen o bien a s o bien a t, pero no a ambas }
#   asegura: {res no tiene elementos repetidos }
# }

# Por ejemplo, dados
# s = [-1, 4, 0, 4, 3, 0, 100, 0, -1, -1]
# t = [0, 100, 5, 0, 100, -1, 5]
# se debería devolver res = [3, 4, 5] ó res = [3, 5, 4] ó res = [4, 3, 5] ó res = [4, 5, 3] ó res = [5, 3, 4] ó res = [5, 4, 3]

# 3) Contar traducciones iguales
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de palabras que tienen la misma traducción en inglés y en alemán.

# problema contar_traducciones_iguales(ing:dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#   requiere: -
#   asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
# }


# Por ejemplo, dados los diccionarios
# aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
# inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
# se debería devolver res = 2
# 4) Convertir a diccionario
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, y sus valores la cantidad de veces que cada uno de esos números aparece en s

# problema convertir_a_diccionario(lista:seq⟨Z⟩) : dicc⟨Z,Z⟩ {
#   requiere: -
#   asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
# }

# Por ejemplo, dada la lista
# lista = [-1, 0, 4, 100, 100, -1, -1]
# se debería devolver res = {-1:3, 0:1, 4:1, 100:2}

# RECORDAR QUE NO IMPORTA EL ORDEN DE LAS CLAVES EN UN DICCIONARIO

def ultima_aparicion(l:list[int],e:int)->int:
    indice=0
    for i in range(len(l)):
        if l[i]==e:
            indice=i
    
    return indice

print(ultima_aparicion([1,2,3,4,5,6,1,1,2,5],1))

def pertenece(l:list,e:int)->bool:
    res=False
    for i in l:
        if e == i:
            res=True
    return res

def elementos_exclusivos(s:list,t:list):
    res=[]
    for i in s:
        if not pertenece(t,i) and not pertenece(res,i):
            res.append(i)
    
    for i in t:
        if not pertenece(s,i) and not pertenece(res,i):
            res.append(i)
    
    return res


def contar_traducciones_iguales(ing:dict[str,str], ale: dict[str,str])->int:
    res=0
    for c,v in ing.items():
        for k,b in ale.items():
            if k==c and b==v:
                res+=1
    return res

aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
print(contar_traducciones_iguales(inglés,aleman))

def pertenececlave(d:dict,s:int)->bool:
    res=False
    for c,v in d.items():
        if c == s:
            res=True

    return res

def convertir_a_diccionario(lista:list[int])->dict[int]:
    res={}
    for i in lista:
        if not pertenececlave(res,i):
            res[i]=1
        else:
            res[i]+=1
    return res

lista = [-1, 0, 4, 100, 100, -1, -1]
print(convertir_a_diccionario(lista))



