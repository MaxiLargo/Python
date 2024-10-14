def del1al10():
    for i in range(1,11,1):
        print(i)

print(del1al10())

def numerospares():
    for i in range (10,41,2):
        if i%2 == 0:
            print(i)
    

numerospares()

def eco()->str:
    for _ in range (1,11):
        print("Eco")
print(eco())

def viajealespacio():
    for i in range (10,-1,-1):
        if i>=1:
            print(i)
        else:
            print("Despegue")
viajealespacio()

def viaje_en_el_tiempo(partida:int,llegada:int)->str:
    for i in range(partida+1,llegada+1,1):
        print("Viajando al año " + str(i))

print(viaje_en_el_tiempo(2004,2010))
    

