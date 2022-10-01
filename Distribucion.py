# Este programa distribuye los equipos electrónicos de un campus universitario
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


class Facultad():
    def __init__(self, nombre: str, estudiantes=0, computadores=0, laptops=0, tablets=0):
        self.nombre = nombre
        self.estudiantes = estudiantes
        self.equipos = [0, 0, 0]
        self.estudiantesSinEquipo = self.estudiantes - \
            (sum(self.equipos))


class Universidad():
    def __init__(self, facultades: list):
        self.equipos = [0, 0, 0]
        # Array en el que se ordenan las facultades de mayor numero de estudiantes sin equipo a menor numero de estudiantes sin equipo
        self.facultades = sorted(
            facultades, key=lambda x: x.estudiantesSinEquipo, reverse=True)
        self.estudiantesSinEquipo = self.facultades[0].estudiantesSinEquipo + \
            self.facultades[1].estudiantesSinEquipo + \
            self.facultades[2].estudiantesSinEquipo + \
            self.facultades[3].estudiantesSinEquipo


# Función extractora de números de un string


def listarNumeros(mensaje: str) -> list:
    numeros = []
    mensajeSeparado = mensaje.split()

    for cadena in mensajeSeparado:
        if cadena.isdigit():
            numeros.append(int(cadena))

    return numeros


# Funcion principal distribuidora

lotes = Cola()

# Se extraen los datos de estudiantes y se guardan en los objetos facultad y universidad

listaCantidadEstudiantes = listarNumeros(input(""))
Ingenieria = Facultad("Ingenieria", listaCantidadEstudiantes[0])
Humanas = Facultad("Humanas", listaCantidadEstudiantes[1])
Medicina = Facultad("Medicina", listaCantidadEstudiantes[2])
Artes = Facultad("Artes", listaCantidadEstudiantes[3])
universidadPrueba = Universidad([Ingenieria, Humanas, Medicina, Artes])

# While para recibir instrucciones de manera indefinida
while True:
    instruccion = input()
    if instruccion.split()[0] == "Lote":
        lote = listarNumeros(instruccion)
        lotes.añadir(lote)

    elif instruccion == "Distribuir lote":
        lote = lotes.extraer()
        # mientras el lote no esté vacío y los estudiantes sin equipo sean mayores a 1, se sigue repartiendo
        while lote != [0, 0, 0] and universidadPrueba.estudiantesSinEquipo > 0:
            for facultad in universidadPrueba.facultades:
                if facultad.estudiantesSinEquipo == 0 or lote == [0, 0, 0]:
                    break
                # Por cada ciclo se reparte de a un equipo y se revisa la condicion inicial
                while lote != [0, 0, 0] and facultad.estudiantesSinEquipo > 0:
                    for i in range(0, len(lote)):
                        if lote[i] > 0:
                            lote[i] -= 1
                            facultad.estudiantesSinEquipo -= 1
                            universidadPrueba.estudiantesSinEquipo -= 1
                            facultad.equipos[i] += 1
                        if facultad.estudiantesSinEquipo == 0:
                            break
                print(facultad.equipos)
    elif instruccion == "Imprimir":

        print("")
