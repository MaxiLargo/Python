def CerosEnPosicionesPares(s:list[int]):
    for i in range(len(s)):
        if i % 2 == 0:
            s[i]=0

print(CerosEnPosicionesPares([1,3,4,1,12,2,1]))

def CerosEnPosicionesPares2(s:list[int]):
    listanueva:list = s.copy()
    for i in range(len(listanueva)):
        if i % 2 == 0:
            listanueva[i]=0
    return listanueva

print(CerosEnPosicionesPares2([1,3,4,1,12,2,1]))

def cadenasinvocales(s:str)->str:
    cadenanueva:str= ""
    vocales:list=["a","e","i","o","u"]
    for i in s:
        if i not in vocales:
            cadenanueva+=i
    
    return cadenanueva

print(cadenasinvocales("Hola"))

def remplazavoacles(s:str)->str:
    cadenanueva:str= ""
    vocales:list=["a","e","i","o","u"]
    for i in s:
        if i not in vocales:
            cadenanueva+=i
        else:
            cadenanueva+="_"
    
    return cadenanueva

print(remplazavoacles("Hola"))

def da_vuelta_str(s:str)->str:
    scopia:str = ""
    scopia1:str = s
    for i in range(len(s)-1,-1,-1):
        scopia+=s[i]

    return scopia

print(da_vuelta_str("Hola"))


