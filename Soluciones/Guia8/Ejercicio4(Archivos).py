def contar_lineas(nombre_archivo:str)->int:
    archivo=open(nombre_archivo,"r",encoding="utf-8")
    archivo.readline()
    longitud:int = 0
    for i in archivo:
        longitud+=1
    
    return longitud

print(contar_lineas(""))
