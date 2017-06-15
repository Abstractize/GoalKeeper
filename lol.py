def elementos(string):
    if isinstance(string,str):
        return elementos_aux(string,"",[])
    else:
        return"Error"
def elementos_aux(string,nombre,lista):
    if string=="":
        return lista
    else:
        if string[0]==" ":
            lista.append(nombre)
            return(string[1:],"",lista)
        else:
            nombre+=string[0]
            return(string[1:],nombre,lista)
