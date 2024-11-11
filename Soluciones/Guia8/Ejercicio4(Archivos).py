def contar_lineas(nombre_archivo:str)->int:
    archivo=open(nombre_archivo,"r",encoding="utf-8")
    longitud:int = 0
    for _ in archivo:
        longitud+=1
    archivo.close()

    return longitud

print(contar_lineas("C:\\Users\Maxim\\Desktop\\PythonIP\\Python\\Soluciones\\Guia8\\hola.txt"))


def existe_palabra(palabra:str,nombre_archivo:str)->bool:
    res:bool = False
    archivo=open(nombre_archivo,"r",encoding="utf-8")
    lista = archivo.readlines()
    for i in lista:
         if palabra == i.strip():
             res=True
    archivo.close()

print(existe_palabra("hola","C:\\Users\Maxim\\Desktop\\PythonIP\\Python\\Soluciones\\Guia8\\hola.txt"))



def cantidad_apariciones(nombre_archivo:str,palabra:str)->int:
    res:int = 0
    archivo=open(nombre_archivo,"r",encoding="utf-8")
    contenido = archivo.read()
    lista = contenido.split()
    for i in lista:
         if palabra == i.strip():
             res+=1
    archivo.close()

print(cantidad_apariciones("C:\\Users\Maxim\\Desktop\\PythonIP\\Python\\Soluciones\\Guia8\\hola.txt","hola"))


def clonar_sin_comentarios(nombre_archivo:str)->None:
    archivo=open(nombre_archivo,"r",encoding="utf-8")
    contenido = archivo.readlines()
    archivo2 = open("C:\\Users\Maxim\\Desktop\\PythonIP\\Python\\Soluciones\\Guia8\\sincomentarios.txt","w",encoding="utf-8")
    escomentario:bool=False
    for i in contenido:
        palabra:str=""
        for caracter in i:
            if caracter == "#" and i[0] == "#":
                print("Quitando caracter")
            else:
                palabra+=caracter
        archivo2.writelines(palabra)
    archivo.close()
    archivo2.close()

print(clonar_sin_comentarios("C:\\Users\Maxim\\Desktop\\PythonIP\\Python\\Soluciones\\Guia8\\textoconcomentarios.txt"))


def invertir_lineas(nombre_archivo:str):
    archivo=open(nombre_archivo,"r",encoding="utf-8")
    contenido = archivo.readlines()
    archivo2 = open("C:\\Users\Maxim\\Desktop\\PythonIP\\Python\\Soluciones\\Guia8\\reverso.txt","w",encoding="utf-8")
    for i in range(0,len(contenido)):
        palabraaescribir:str=""
        palabraaescribir=contenido[len(contenido)-1]
        palabraaescribir+="\n"
        contenido.pop(len(contenido)-1)
        archivo2.write(palabraaescribir)
    archivo.close()
    archivo2.close()
print(invertir_lineas("C:\\Users\Maxim\\Desktop\\PythonIP\\Python\\Soluciones\\Guia8\\invertirlineas.txt"))


def agrega_frase_al_final(nombre_archivo:str,frase:str):
    archivo=open(nombre_archivo,"r",encoding="utf-8")
    contenido = archivo.read()
    archivo=open(nombre_archivo,"w",encoding="utf-8")
    archivo.writelines(contenido + "\n" + frase)

print(agrega_frase_al_final("C:\\Users\Maxim\\Desktop\\PythonIP\\Python\\Soluciones\\Guia8\\hola.txt","jajaxd"))


def agrega_frase_al_principio(nombre_archivo:str,frase:str):
    archivo=open(nombre_archivo,"r",encoding="utf-8")
    contenido = archivo.read()
    archivo=open(nombre_archivo,"w",encoding="utf-8")
    archivo.writelines(frase + "\n" + contenido)
print(agrega_frase_al_principio("C:\\Users\Maxim\\Desktop\\PythonIP\\Python\\Soluciones\\Guia8\\hola.txt","12344555555"))


def lista_palabras_de_archivo(nombre_archivo:str):
    archivo=open(nombre_archivo,"rb")
    contenido = archivo.readlines()
    palabraslegibles=[]
    for palabra in contenido:
        for byte in palabra:
            palabraleida=""
            if chr(byte) == chr(32) or chr(48)<=chr(byte)<=chr(57) or chr(48)<=chr(byte)<=chr(57) or chr(65)<=chr(byte)<=chr(90) or chr(97)<=chr(byte)<=chr(122):
                    palabraleida+=chr(byte)
        if len(palabraleida)>=5:
            palabraslegibles.append(palabraleida)
    archivo.close()
    return palabraslegibles
print(lista_palabras_de_archivo("C:\\Users\Maxim\\Desktop\\PythonIP\\Python\\Soluciones\\Guia8\\leerbinario.txt"))
