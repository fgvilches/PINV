#Funciones
def readfile(nombrearchivo,extension):
    archivo = open(nombrearchivo + "." + extension, "r")
    lineas = archivo.readlines()
    archivo.close()
    return lineas

def writefile(nombrearchivo,extension,line,posicion):
    if line >= 0:
        archivo = open(nombrearchivo + "." + extension, "r")
        lineas = archivo.readlines()
        archivo.close()
        lineas[posicion] = line
        archivo = open(nombrearchivo + "." + extension, "w")
        archivo.writelines(lineas)
        archivo.close()
        return True
    else:
        return False

def choiceExtractor(lista):
    choices = []
    for line in lista:
        aux_line = [line,line]
        aux_tuple = tuple(aux_line)
        choices.append(aux_tuple)
    return choices
