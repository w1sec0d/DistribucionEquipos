# Definicion de estructuras de datos necesarias para trabajar
class Cola():
    def __init__(self, lista=[]):
        self.lista = lista

    def añadir(self, elemento):
        self.lista.append(elemento)

    def extraer(self):
        if len(self.lista) > 0:
            return self.lista.pop(0)
        else:
            return ""

    def __str__(self):
        return(str(self.lista))


class Pila():
    def __init__(self, lista=[]):
        self.lista = lista

    def añadir(self, elemento):
        self.lista.append(elemento)

    def extraer(self):
        if len(self.lista) > 0:
            return self.lista.pop()
        else:
            return ""

    def __str__(self):
        return(str(self.lista))

# Distribución principal


casos = int(input())

for caso in range(0, casos):  # Para cada caso, se piden inputs y se reparten electrodomesticos

    electrodomesticos = int(input())
    listaElectrodomesticos = input().split(" ")
    tiendas = int(input())
    electrodomesticosATiendas = input().split(" ")
    electrodomesticosATiendas = [int(element)
                                 for element in electrodomesticosATiendas]  # Se convierte a lista de enteros

    # Se convierten las listas a pilas y colas
    pilaElectrodomesticos = Pila()
    for electrodomestico in reversed(listaElectrodomesticos):
        pilaElectrodomesticos.añadir(electrodomestico)

    colaElectrodomesticosATiendas = Cola()
    for electrodomesticoATienda in electrodomesticosATiendas:
        colaElectrodomesticosATiendas.añadir(electrodomesticoATienda)

    # Repartición principal
    tiendaARepartir = 1

    # Recorre cada tienda mientras haya inventario
    while tiendaARepartir <= tiendas:
        if electrodomesticos != 0:
            electrodomesticosRepartidos = 0
            electrodomesticosARepartir = colaElectrodomesticosATiendas.extraer()

            inventarioTienda = Cola([])
            while electrodomesticosARepartir > electrodomesticosRepartidos:
                inventarioTienda.añadir(pilaElectrodomesticos.extraer())
                electrodomesticosRepartidos += 1
                electrodomesticos -= 1

            # Se imprime lo que se repartió en la tienda
            print("[", end="")
            itemTienda = inventarioTienda.extraer()

            stringLista = ""
            while itemTienda != "":
                stringLista += itemTienda + " "
                itemTienda = inventarioTienda.extraer()
            # Remueve el ultimo espacio innecesasrio
            stringLista = stringLista[0:-1]
            print(stringLista, end="")

            print("]")

            tiendaARepartir += 1
        else:
            print("[]")
            tiendaARepartir += 1
