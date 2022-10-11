# Este programa encuentra los bordes de una palabra mediante listas enlazadas
# Realizado por Carlos David Ramírez Muñoz

# Definicion de estructuras de datos necesarias para trabajar

class Nodo():
    def __init__(self, contenido=None, siguienteNodo=None):
        self.contenido = contenido
        self.siguienteNodo = siguienteNodo


class ListaEnlazada():
    def __init__(self, cabeza=None):
        self.cabeza = cabeza

    def __str__(self):
        nodo = self.cabeza
        stringLista = ""
        while(nodo.siguienteNodo != None):
            stringLista += (f"{str(nodo.contenido)} -> ")
            nodo = nodo.siguienteNodo
        stringLista += str(nodo.contenido)

        return stringLista

    def agregarAlFinal(self, elemento):
        ultimoNodo = self.cabeza

        if ultimoNodo == None:
            self.cabeza = Nodo(elemento)
        else:
            while ultimoNodo.siguienteNodo != None:
                ultimoNodo = ultimoNodo.siguienteNodo
            ultimoNodo.siguienteNodo = Nodo(elemento)

    def getLongitud(self):
        nodo = self.cabeza
        longitud = 0
        while nodo.siguienteNodo != None:
            longitud += 1
            nodo = nodo.siguienteNodo
        return longitud

# Funcion principal de calculo de bordes


def calcularBordes(stringListaInicial: str) -> list:
    # Conversión de string de lista a lista
    listaInicial = stringListaInicial.strip("][").split(",")
    # Conversión de la lista inicial a lista enlazada
    listaEnlazadaInicial = ListaEnlazada()
    for letra in listaInicial:
        listaEnlazadaInicial.agregarAlFinal(letra)

    # Se recorre la lista de izquierda a derecha para encontrar los prefijos
    nodo = listaEnlazadaInicial.cabeza
    prefijos = [[listaEnlazadaInicial.cabeza.contenido]]
    prefijoTemporal = [listaEnlazadaInicial.cabeza.contenido]

    while nodo.siguienteNodo != None:
        nodo = nodo.siguienteNodo
        prefijoTemporal.extend(nodo.contenido)
        prefijos.append(list(prefijoTemporal))

    # Se recorre la lista de derecha a izquierda para encontrar los sufijos
    nodoInicial = listaEnlazadaInicial.cabeza
    longitudLista = listaEnlazadaInicial.getLongitud()
    sufijos = []
    sufijoTemporal = []

    for i in range(0, longitudLista+1):
        pasos = longitudLista - i
        nodo = nodoInicial
        for paso in range(pasos):
            nodo = nodo.siguienteNodo
        sufijoTemporal.insert(0, nodo.contenido)
        sufijos.insert(0, list(sufijoTemporal))

    # Se compara la lista de prefijos con la de sufijos para verificar cuales estan en ambas
    bordes = []
    for prefijo in prefijos:
        if prefijo in sufijos:
            bordes.append(prefijo)

    impresionFinal = ""
    # Se convierte cada lista a string y se añade a un string a mostrar al final
    for borde in bordes:
        impresionFinal += "["
        impresionFinal += "".join(str(letra) +
                                  "," for letra in borde)  # anexa la letra con una coma si no es el ultimo elemento
        # Quita la ultima coma innecesaria
        impresionFinal = impresionFinal[:-1]
        impresionFinal += "]"
        # si el borde no es el último, anexa un salto de linea
        if borde != bordes[len(bordes)-1]:
            impresionFinal += "\n"

    return impresionFinal


listaAConsultar = input()
print(calcularBordes(listaAConsultar))
