from queue import LifoQueue as Pila

# def agrupar_por_longitud(nombre_archivo:str)->dict:
#     archivo=open(nombre_archivo,"r",encoding="utf-8")
#     res:dict={}
#     for linea in archivo:
#         if len(linea) in res.keys():
#             res[len(linea)]+=1
#         else:
#             res[len(linea)]=1
#     archivo.close()  # Cierra el archivo al finalizar
#     return res
# print(agrupar_por_longitud('C:\\Users\\Maxim\\Desktop\\PythonIP\\Python\\Soluciones\\Guia8\\hola.txt'))



def promedio(nombre:str,notas:list[tuple[str,float]])->float:
    repeticion_alumno:int=0
    totalnotas:float=0.0
    for alumno,nota in notas:
        if nombre == alumno:
            repeticion_alumno+=1
            totalnotas=nota+totalnotas
    
    res:float=totalnotas/repeticion_alumno

    return res



def calcular_promedio_por_estudiante(notas:list[tuple[str,float]])->dict[str,float]:
    res:dict={}

    for estudiante,nota in notas:
        if estudiante not in res:
            res[estudiante]=nota
        else:
            res[estudiante]=promedio(estudiante,notas)
    
    return res

notas = [
    ("Juan", 85.0),
    ("Ana", 90.0),
    ("Juan", 78.0),
    ("Ana", 92.0),
    ("Pedro", 76.0)
]

promedios = calcular_promedio_por_estudiante(notas)
print(promedios)


# def la_palabra_mas_frecuente(nombrearchivo:str)->str:
#     archivo=open(nombrearchivo,'r')
#     lineas=archivo.readlines()
#     diccionario:dict={}
#     for linea in lineas:
#         if linea not in diccionario:
#             diccionario[linea]=1
#         else:
#             diccionario[linea]+=1
#     archivo.close()
#     palabramaxima:int = 0
#     palabramasfrecuente:str=""
#     for palabra,frecuente in diccionario.items():
#         if palabramaxima<frecuente:
#             palabramaxima=frecuente
#             palabramasfrecuente=palabra
    
#     return palabramasfrecuente

# print(la_palabra_mas_frecuente('C:\\Users\\Maxim\\Desktop\\PythonIP\\Python\\Soluciones\\Guia8\\hola.txt'))



def visitar_sitio(historiales:dict[str,Pila[str]],usuario:str,sitio:str)->dict[str,Pila[str]]:
    p:Pila[str] = Pila()
    if not usuario in historiales.keys():
        historiales[usuario]=p
        historiales[usuario].put(sitio)
    else:
        historiales[usuario].put(sitio)


    return historiales


def navegar_atras(historiales:dict[str,Pila[str]],usuario:str):
    paux=Pila()
    for i,k in historiales.items():
        if i == usuario:
           sitio1:str=k.get()
           paux.put(sitio1)
           while not k.empty():
            paux.put(k.get())
           while not paux.empty():
               k.put(paux.get())


    return historiales

# historiales = {}
# visitar_sitio(historiales, "Usuario1", "google.com")
# visitar_sitio(historiales, "Usuario1", "facebook.com")
# visitar_sitio(historiales, "Usuario1", "youtube.com")
# navegar_atras(historiales, "Usuario1")
# visitar_sitio(historiales, "Usuario2", "youtube.com")

def pertenece(x,y):
    res=False
    for i in x.keys():
        if i == y:
            res = True
    return res
               
def agregar_producto(inventario:dict[str,dict[float,int]],nombre:str,precio:float,cantidad:int)->dict[str,dict[str,float]]:
    if not pertenece(inventario,nombre):
        inventario[nombre]={"precio": precio, "cantidad": cantidad}

    return inventario



def actualizar_precios(inventario:dict[str,dict[float,int]],nombre:str,precio:float)->dict[str,dict[float,int]]:
    for j,i in inventario.items():
        if j == nombre:
            for k in i.keys():
                if k == "precio":
                    i["precio"] = precio
    return inventario

def actualizar_stock(inventario:dict[str,dict[float,int]],nombre:str,cantidad:float):
    for j,i in inventario.items():
        if j == nombre:
            for k in i.keys():
                if k == "precio":
                    i["cantidad"] = cantidad
    return inventario

def calcular_valor_inventario(inventario:dict[str,dict[float,int]])->float:
    total:float=0.0
    for j,i in inventario.items():
        for x,y in i.items():
            total=(i["precio"]*i["cantidad"]) + total
    return total

inventario = {}
print(agregar_producto(inventario, "Camisa", 20.0, 50))
print(agregar_producto(inventario, "Pantalon", 30.0, 30))
print(actualizar_stock(inventario, "Camisa", 10))
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total) 


