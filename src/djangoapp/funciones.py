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

def choiceExtractor(text):
    choices = []
    for line in text:
        new_line = line.replace("\n","")
        aux_line = [str(new_line),str(new_line)]
        aux_tuple = tuple(aux_line)
        choices.append(aux_tuple)
    return choices
