from queue import LifoQueue as Pila

import random
def generar_nros_al_azar(cantidad : int,desde : int, hasta : int) -> Pila[int]:
    p:Pila = Pila()
    for _ in range(0,cantidad):
        valor:int = random.randint(desde, hasta)
        p.put(valor)
    return p

print(generar_nros_al_azar(10,1,20))

def cantidad_elementos(p : Pila)->int:
    paux:Pila = Pila()
    longitud:int = 0
    while not p.empty():
        longitud+=1
        v=p.get()
        paux.put(v)
    while not paux.empty():
        p.put(paux.get())
    
    return longitud

# p:Pila = Pila()
# p.put(1)
# p.put(2)
# p.put(3)
# p.put(4)
# print(cantidad_elementos(p))


def maximo(m:list[int])->int:
    x:int=m[0]
    for i in m:
        if i>x:
            x=i
    return x


def buscar_el_maximo(p:Pila[int])->int:
    paux:Pila[int] = Pila()
    res:list[int]=[]
    while not p.empty():
        x=p.get()
        res.append(x)
        paux.put(x)
    while not paux.empty():
        p.put(paux.get())
    
    return maximo(res)

# print(buscar_el_maximo(p))



def buscar_nota_maxima(p:Pila[tuple[str,int]]):
    paux:Pila[tuple[str,int]] = Pila()
    listaaux:list[tuple[str,int]]=[]
    notas: list[int] = []

    while not p.empty():
        valor:tuple[str,int] = p.get()
        listaaux.append(valor)
        notas.append(valor[1])  # Añadimos solo la nota
        paux.put(valor)
    
    while not paux.empty():
        valor:tuple[str,int] = paux.get()
        p.put(valor)
    
    nota_maxima = maximo(notas)

    for nombre,nota in listaaux:
        if nota == nota_maxima:
            return nombre,nota

p = Pila()
p.put(("Ana", 70))
p.put(("Juan", 85))
p.put(("Luis", 90))
p.put(("Sofia", 75))

# Llamar a la función y mostrar el resultado
print(buscar_nota_maxima(p))  # Debería imprimir: ('Luis', 90)

def esta_bien_balanceada(s: str) -> bool:
    p: Pila[str] = Pila()  # Creamos una pila
    for char in s:
        if char == '(':
            p.put(char)  # Apilamos cada paréntesis abierto
        elif char == ')':
            if p.empty():
                return False  # Si encontramos un paréntesis cerrado sin paréntesis abierto, no está balanceado
            p.get()  # Desapilamos el último paréntesis abierto cuando encontramos uno cerrado

    return p.empty()  # Verificamos que no queden paréntesis abiertos


def evaluar_expresion(s:str)->float:
    operandos:list[str]=["+","-","*","/"]
    p:Pila[str]=Pila()
    for i in s:
        if i not in operandos and i != " ":
            p.put(float(i))
        elif i != " ":
            v1=p.get()
            v2=p.get()
                        # Aplicamos el operador adecuado
            if i == "+":
                p.put(v1 + v2)
            elif i == "-":
                p.put(v1 - v2)
            elif i == "*":
                p.put(v1 * v2)
            elif i == "/":
                p.put(v1 / v2)

    resultado = p.get()
    return resultado


expresion = "3 4 + 5 * 2 -"
resultado = evaluar_expresion(expresion)
print(resultado) # Deber ́ıa devolver 33



