def minimotuplas(listatuplas:list[tuple[str,int]],producto:str):
    valorminimo:int = listatuplas[0][1]
    for i,j in listatuplas:
        if producto == i:
            if j < valorminimo:
                valorminimo = j
    return valorminimo

print(minimotuplas([("p1",31),("p2",5),("p1",5)],"p1"))


# def stock_producto(stock_cambios:list[tuple[str,int]])->dict[str,tuple[int,int]]:
#     diccionario:dict = {}
#     for tuplas in stock_cambios:
