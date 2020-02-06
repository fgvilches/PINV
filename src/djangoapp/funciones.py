#Funciones

def readfile(nombrearchivo,extension):
    #archivos a leer deben estar en la misma carpeta
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
        choices.append((text[line]).upper(),str(text[line]))
    return choices
