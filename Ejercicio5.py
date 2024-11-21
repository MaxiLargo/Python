# 1
# 2) Posición umbral [2 puntos]

# Durante una noche en un restaurant pasan varios grupos de diversa cantidad de personas. Para llevar control de esto, el dueño va anotando en su libreta cuánta gente entra y sale. Para hacerlo rápido decide que la mejor forma de llevarlo adelante es escribir un número al lado del otro, usando números positivos para los grupos que entran y negativos para los que salen. Gracias a estas anotaciones el dueño es capaz de hacer análisis del flujo de clientes. Por ejemplo, le interesa saber en qué momento de la noche superó una determinada cantidad de clientes totales que ingresaron (sin importar cuántos hay en el momento en el local).

# Implementar la función pos_umbral, que dada una secuencia de enteros (puede haber negativos) devuelve la posición en la cual se supera el valor de umbral, teniendo en cuenta sólo los elementos positivos. Se debe devolver -1 si el umbral no se supera en ningún momento

# problema pos_umbral (in s: seq⟨Z⟩, in u: Z) : Z {
#   requiere: u ≥ 0
#   asegura: {res=-1 si el umbral no se supera en ningún momento }
#   asegura: {Si el umbral se supera en algún momento, res es la primera posición tal que la sumatoria de los primeros res+1 elementos (considerando solo aquellos que son positivos) es estrictamente mayor que el umbral u }

# Por ejemplo, dadas
# s = [1,-2,0,5,-7,3]
# u = 5
# se debería devolver res = 3
# 3) Columnas repetidas [3 puntos]

# Implementar la función columnas_repetidas, que dada una matriz no vacía de m columnas (con m par y m ≥ 2) devuelve True si las primeras m/2 columnas son iguales que las últimas m/2 columnas. Definimos a una secuencia de secuencias como matriz si todos los elementos de la primera secuencia tienen la misma longitud.

# problema columnas_repetidas(in mat:seq⟨seq⟨Z⟩⟩ ) : Bool {
#   requiere: {|mat| > 0}
#   requiere: {todos los elementos de mat tienen igual longitud m, con m > 0 (los elementos de mat son secuencias)}
#   requiere: {todos los elementos de mat tienen longitud par (la cantidad de columnas de la matriz es par)}
#   asegura: {(res = true) <=> las primeras m/2 columnas de mat son iguales a las últimas m/2 columnas}
# }

# Por ejemplo, dada la matriz
# m = [[1,2,1,2],
#      [-5,6,-5,6],
#      [0,1,0,1]]
# se debería devolver res = true

# TIP: para dividir un número entero x por 2 y obtener como resultado un número entero puede utilizarse la siguiente instrucción: int(x/2)
# 4) Rugby 4 naciones [3 puntos]

# Desde hace más de 10 años existe en el mundo del rugby un torneo que disputan anualmente 4 selecciones del sur global (Argentina, Australia, Nueva Zelanda y Sudáfrica). Este torneo se llama "The rugby championship" o comunmente "4 naciones", ya que suplantó al viejo "3 naciones".

# Implementar la función cuenta_posiciones_por_nacion que dada la lista de naciones que compiten en el torneo, y el diccionario que tiene los resultados de los torneos anuales en el formato año:posiciones_naciones, donde año es un número entero y posiciones_naciones es una lista de strings con los nombres de las naciones, genere un diccionario de naciones:#posiciones, que para cada Nación devuelva la lista de cuántas veces salió en esa posición.

# Tip: para crear una lista con tantos ceros como naciones se puede utilizar la siguiente sintaxis lista_ceros = [0]*len(naciones)

# problema cuenta_posiciones_por_nacion(in naciones: seq⟨String⟩, in torneos: dict⟨Z,seq⟨String⟩⟩: dict⟨String,seq⟨Z⟩⟩ {
#   requiere: {naciones no tiene elementos repetidos}
#   requiere: {Los valores del diccionario torneos son permutaciones de la lista naciones (es decir, tienen exactamente los mismos elementos que naciones, en cualquier orden posible)}
#   asegura: {res tiene como claves los elementos de naciones}
#   asegura: {El valor en res de una nación es una lista de |naciones| elementos que indica en la posición i cuántas veces salió esa nación en la i-ésima posición.}
# }

# Por ejemplo, dados
# naciones= ["arg", "aus", "nz", "sud"]
# torneos= {2023:["nz", "sud", "arg", "aus"],
#                  2022:["nz", "sud", "aus", "arg"]}
# se debería devolver res = {"arg": [0,0,1,1], "aus": [0,0,1,1], "nz": [2,0,0,0], "sud": [0,2,0,0]} 


def umbral(lista,umbral):
    res=-1
    acumulador=0
    for k in range(len(lista)):
        if acumulador<=umbral and lista[k]>0:
            acumulador+=lista[k]
            if acumulador > umbral:
                res=k

    return res

s = [1,-2,0,5,-7,3]
u = 5

print(umbral(s,u))

# def transpuesta(x:list[list[int]]):
#     res=[]
#     for i in range(len(x[0])):
#         resaux=[]
#         for j in range(len(x)):
#             resaux.append(x[j][i])
#         res.append(resaux)
#     return res

# print(transpuesta())

def columnas_repetidasaux(mat:list[int])->bool:
    resaux1=[]
    resaux2=[]
    for p_mitad in range(0,len(mat)//2):
        resaux1.append(mat[p_mitad])
    
    for p_mitad in range(len(mat)//2,len(mat)):
        resaux2.append(mat[p_mitad])
    
    if resaux1 == resaux2:
        return True
    else:
        return False
    
def columnas_repetidas(mat:list[list[int]])->bool:
    for i in range(len(mat)):
        if not columnas_repetidasaux(mat[i]):
            return False
    
    return True


m = [[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]

print(columnas_repetidas(m))

def cuenta_posiciones_por_nacion(naciones:list[str],torneos:dict)->dict:
    diccionario={}
    for nacion in naciones:
        if not nacion in diccionario.keys():
            diccionario[nacion]=[0]*len(naciones)
    for año,nacion in torneos.items():
        for pais in range(len(nacion)):
            diccionario[nacion[pais]][pais]+=1
            

    return diccionario

naciones= ["arg", "aus", "nz", "sud"]
torneos= {2023:["nz", "sud", "arg", "aus"],
                 2022:["nz", "sud", "aus", "arg"]}

print(cuenta_posiciones_por_nacion(naciones,torneos))