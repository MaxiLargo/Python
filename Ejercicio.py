def minimotuplas(listatuplas:list[tuple[str,int]],producto:str):
    valorminimo:int = 0
    for i,j in listatuplas:
        if producto == i:
                valorminimo=j
    for i,j in listatuplas:
         if producto == i:
              if j<valorminimo:
                   valorminimo=j
    return valorminimo
         

def maximotuplas(listatuplas:list[tuple[str,int]],producto:str):
    valormaximo:int = 0
    for i,j in listatuplas:
        if producto == i:
                valormaximo=j
    for i,j in listatuplas:
         if producto == i:
              if j>valormaximo:
                   valormaximo=j
    return valormaximo

def stock_productos(stock_cambios:list[tuple[str,int]])->dict[str,tuple[int,int]]:
    diccionario:dict = {}
    for producto,stock in stock_cambios:
         if not producto in diccionario:
              diccionario[producto]=(minimotuplas(stock_cambios,producto),minimotuplas(stock_cambios,producto))
         else:     
              diccionario[producto]=(minimotuplas(stock_cambios,producto),maximotuplas(stock_cambios,producto))
         
    return diccionario



sc1 = [("galletita", 12),("galletita", 10),("galletita", 1),("hueso",120),("hueso",3),("hueso",10)] #{"galletita":(1,12), "hueso":(3,120)}
print(stock_productos(sc1))
sc2 = [("pato", 12),("pato",0),("pato",13),("collar",300),("collar",20),("collar",17),("comida",100),("comida",29)]
#{"pato":(0,13), "collar":(17,300), "comida": (29,100)}
print(stock_productos(sc2))
sc3 = [("correa", 10),("comida",140),("comida",49),("shampoo",2),("shampoo",39),("shampoo",50)]
#{"correa": (10,10), "comida":(49,140), "shampoo": (2,50)}
print(stock_productos(sc3))

def esprimo(x:int)->bool:
    res:bool = True
    if x <=1:
         return False
    for i in range(2,x):
         if x%i == 0:
              res=False
    return res

def sonlosultimosprimos(x:int)->bool:
     ult_3digitos:int=x%1000
     return esprimo(ult_3digitos)

def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
     res:list[int]=[]
     for i in codigos_barra:
          if sonlosultimosprimos(i):
               res.append(i)

     return res


# codigos_barra = [123456789, 987654321, 555555107, 444004109]
# El resultado debería ser [555555107, 444004109]
# 107 y 109 son números primos

codigos_barra = [111111000, 222222002, 333333004, 444444006]
# # El resultado debería ser [222222002]
# # Solo el número 002 (2) es primo; los demás no lo son.

# codigos_barra = [555555011, 666666013, 777777017]
# # El resultado debería ser [555555011, 666666013, 777777017]
# # 011, 013 y 017 son todos números primos.

# codigos_barra = [111111100, 222222200, 333333400]
# # El resultado debería ser []
# # 100, 200 y 400 no son primos.
# codigos_barra = [123123007, 456456031, 789789151, 101101157, 202202191]
# # El resultado debería ser [123123007, 456456031, 789789151, 101101157, 202202191]
# # 007, 031, 151, 157 y 191 son todos números primos de tres dígitos.
# codigos_barra = [101101101, 202202202, 303303303, 404404107, 505505113]
# # El resultado debería ser [404404107, 505505113]
# # 107 y 113 son números primos, los demás no lo son.

print(filtrar_codigos_primos(codigos_barra))


# 3) Matriz de responsables por turnos [2 puntos]

# Las personas responsables de los turnos están anotadas en una matriz donde las columnas representan los
# días, en orden de lunes a domingo, y cada fila a un rango de una hora. Hay cuatro filas para los turnos 
# de la mañana (9, 10, 11 y 12 hs) y otras cuatro para la tarde (14, 15, 16 y 17).

# Para hacer más eficiente el trabajo del personal de la veterinaria, se necesita analizar si quienes 
# quedan de responsables, están asignadas de manera continuada en los turnos de cada día.

# Para ello se pide desarrollar una función en Python que, dada la matriz de turnos, devuelva una lista
# de tuplas de Bool, una por cada día. Cada tupla debe contener dos elementos. El primer elemento debe ser
# True sí y solo sí todos los valores de los turnos de la mañana para ese día son iguales entre sí. El 
# segundo elemento debe ser True sí y solo sí todos los valores de los turnos de la tarde para ese día 
# son iguales entre sí. Siempre hay una persona responsable en cualquier horario de la veterinaria.

# problema un_responsable_por_turno(in grilla_horaria: seq<seq<String>>): seq<(Bool x Bool)> {
# requiere: {|grilla_horaria| = 8}
# requiere: {Todos los elementos de grilla_horaria tienen el mismo tamaño (mayor a 0 y menor a 8)}
# requiere: {No hay cadenas vacías en las listas de grilla_horaria}
# asegura: {|res| = |grilla_horaria[0]|}
# asegura: {El primer valor de la tupla en res[i], con i:Z, 0 <= i < |res| es igual a True <==> los primeros
# 4 valores de la columna i de grilla_horaria son iguales entre sí}
# asegura: {El segundo valor de la tupla en res[i], con i:Z, 0 <= i < |res| es igual a True <==> los últimos
# 4 valores de la columna i de grilla_horaria son iguales entre sí}
# }
