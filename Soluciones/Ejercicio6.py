def del1al10():
    n=1
    while n<10:
        print(n)
        n+=1
    return n 

print(del1al10())

def numerospares():
    n=10
    while n<40:
        if n%2 == 0:
            print(n)
            n+=1
        else:
            n+=1
    return n 

print(numerospares())

def eco()->str:
    n=0
    res = ""
    while n<9:
        res = "Eco"
        print(res)
        n+=1
    return res

print(eco())


def viaje_en_el_tiempo(partida:int,llegada:int)->str:
    res:str = ""
    if partida>llegada:
        return "error"
    while partida < llegada:
        partida+=1
        print("Viajando al año " + str(partida))
print(viaje_en_el_tiempo(2004,2010))
    

