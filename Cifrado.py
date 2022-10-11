# Este programa realiza el cifrado ROT mediante colas, pilas y listas enlazadas
# Realizado por Carlos David Ramírez Muñoz

# Definicion de estructuras de datos necesarias para trabajar
class Cola():
    def __init__(self, lista=[]):
        self.lista = lista

    def añadir(self, elemento):
        self.lista.append(elemento)

    def extraer(self):
        return self.lista.pop(0)

    def __str__(self):
        return(str(self.lista))


class Pila():
    def __init__(self, lista=[]):
        self.lista = lista

    def añadir(self, elemento):
        self.lista.append(elemento)

    def extraer(self):
        return self.lista.pop()

    def __str__(self):
        return(str(self.lista))


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

# Función de cifrado principal


def cifrar(permutaciones: int, mensaje: str) -> str:
    abecedario = list("abcdefghijklmnopqrstuvwxyz")
    mensaje = mensaje.replace("ñ", "o")
    posicionesMensajeInicial = [abecedario.index(letra) for letra in mensaje]

    # Se convierte el abecedario a una cola para realizar las permutaciones
    colaAbecedario = Cola(abecedario)
    for i in range(1, permutaciones+1):
        letraEliminada = colaAbecedario.extraer()
        colaAbecedario.añadir(letraEliminada)

    # Se convirte el abecedario a lista enlazada para realizar el cifrado
    ListaEnlazadaAbecedario = ListaEnlazada()
    for letra in colaAbecedario.lista:
        ListaEnlazadaAbecedario.agregarAlFinal(letra)

    mensajeCifrado = ""
    for posicion in posicionesMensajeInicial:
        nodo = ListaEnlazadaAbecedario.cabeza
        for i in range(1, posicion+1):
            nodo = nodo.siguienteNodo
        mensajeCifrado += nodo.contenido

    # se usan dos pilas para invertir el mensaje
    pilaMensajeCifrado = Pila(list(mensajeCifrado))
    pilaMensajeCifradoInverso = Pila()

    while len(pilaMensajeCifrado.lista) > 0:
        letraExtraida = pilaMensajeCifrado.extraer()
        pilaMensajeCifradoInverso.añadir(letraExtraida)

    return "".join(pilaMensajeCifradoInverso.lista)


t = int(input())
frase = input()
print(cifrar(t, frase), end="")
