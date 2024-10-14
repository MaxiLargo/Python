def fibonorecursivo(n:int)->int:
    if n<=1:
        return n
    un_fibo:int = 0 
    un_fibo_sig:int = 1
    i : int = 2
    while i<=n:
        aux:int = un_fibo + un_fibo_sig
        un_fibo = un_fibo_sig
        un_fibo_sig = aux 
        i+=1
    return un_fibo

print(fibonorecursivo(4))


def es_primo(n:int)->bool:
    cant_divisores:int = 0
    i :int = 2 #debe ser 2

    while i<n and cant_divisores <2:
        if n % i == 0:
            cant_divisores += 1
            i+=1
        else:        #lo agregue yo
            i+=1     #lo agregue yo   
    return cant_divisores < 2 and i == n

    print(es_primo(6))


def buscar_nesimo_primo(n:int)->int:
    cant_primos:int = 0
    i:int = 2 # esto ??? 
    while cant_primos< n: 
        if es_primo(i):
            cant_primos+=1
    return i

print(buscar_nesimo_primo(3))


def suma_matriz_fila_col(f:int,c:int):
    res = 0
    for k in range(1,c+1,1):
        for j in range(1,f+1,1):
            res+=k+j
    return res 

print(suma_matriz_fila_col(1,5))


def piramide_de_numeros(n:int):
    for a in range(1,n+1):
        print(" " * (n-a), end = " ")
        for j in (1,a+1):
            print(j, end = "")
        for z in range(a-1,0,-1):
            print(z,end = "")
        print()

print(piramide_de_numeros(4))