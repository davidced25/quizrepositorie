#El director de un hotel desea implementar una sistema de administración para saber la disponibilidad y asignación de habitaciones. 
# Para asignar, registra el número de cédula y el nombre de cada cliente a medida que llega al hotel, 
# junto con el número de habitación que ocupa (el antiguo libro de entradas).
# Clase que representa cada habitacion como nodo de una lista enlazada
class Habitacion:
    def __init__(self, num):
        self.num = num                  # Numero de la habitacion
        self.estado = "Libre"           # Estado actual
        self.ced = None                 # Cedula del huesped
        self.nom = None                 # Nombre del huesped
        self.hr = None                  # Hora de llegada
        self.siguiente = None           # Apuntar al siguiente nodo


# Clase principal del hotel
class Hotel:
    def __init__(self):
        self.cabeza = None              
        self.ent = []                   # Lista entradas
        self.sal = []                   # Lista Salidas

    # Crea y agrega habitacion al final de la lista
    def agregar_habitacion(self, num):
        nueva = Habitacion(num)

        if self.cabeza is None:
            self.cabeza = nueva
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva

    # Asignar una habitacion libre
    def asignar_habitacion(self):
        ced = input("Ingrese cedula: ")
        nom = input("Ingrese nombre: ")
        hr = input("Ingrese hora de llegada: ")

        actual = self.cabeza

        while actual:
            if actual.estado == "Libre":

                actual.estado = "Ocupado"
                actual.ced = ced
                actual.nom = nom
                actual.hr = hr

                # guandamos la informacion en entradas 
                self.ent.append({
                    "Cedula": ced,
                    "Nombre": nom,
                    "Habitacion": actual.num,
                    "Hora": hr
                })

                print("Habitacion asignada:", actual.num)
                return

            actual = actual.siguiente

        print("No hay habitaciones disponibles.")

    # quita cedula y nombre de la habitacion y tambien cambia el estado a libre
    def liberar_habitacion(self):
        ced = input("Ingrese cedula del huesped que sale: ")
        actual = self.cabeza

        while actual:
            if actual.ced == ced:

                # Guarada informacion en salidas 
                self.sal.append({
                    "Cedula": actual.ced,
                    "Nombre": actual.nom,
                    "Habitacion": actual.num,
                    "Hora de entrada": actual.hr
                })

                actual.estado = "Libre"
                actual.ced = None
                actual.nom = None
                actual.hr = None

                print("Habitacion liberada correctamente.")
                return

            actual = actual.siguiente

        print("Cedula no encontrada.")

    # Buscar por cedula
    def buscar_cedula(self):
        ced = input("Ingrese cedula a buscar: ")
        actual = self.cabeza

        while actual:
            if actual.ced == ced:
                print("Habitacion:", actual.num)
                print("Nombre:", actual.nom)
                print("Hora de llegada:", actual.hr)
                return
            actual = actual.siguiente

        print("No existe un huesped activo con esa cedula.")

    # Para mostrar habitaciones libres
    def mostrar_libres(self):
        print("Habitaciones libres:")
        actual = self.cabeza
        hay = False

        while actual:
            if actual.estado == "Libre":
                print("Habitacion", actual.num)
                hay = True
            actual = actual.siguiente

        if not hay:
            print("No hay habitaciones libres.")

    # Para mostrar habitaciones ocupadas
    def mostrar_ocupadas(self):
        print("Habitaciones ocupadas:")
        actual = self.cabeza
        hay = False

        while actual:
            if actual.estado == "Ocupado":
                print("Habitacion:", actual.num,
                      "Cedula:", actual.ced,
                      "Nombre:", actual.nom,
                      "Hora:", actual.hr)
                hay = True
            actual = actual.siguiente

        if not hay:
            print("No hay habitaciones ocupadas.")

    # Mostrar las entradas registradas
    def mostrar_entradas(self):
        print("Entradas:")
        if len(self.ent) == 0:
            print("No hay registros.")
        else:
            for r in self.ent:
                print(r)

    # Mostrar las salidas registradas
    def mostrar_salidas(self):
        print("Salidas:")
        if len(self.sal) == 0:
            print("No hay registros.")
        else:
            for r in self.sal:
                print(r)


# Menu principal
hotel = Hotel()

cant = int(input("Ingrese numero de habitaciones del hotel: "))

for i in range(1, cant + 1):
    hotel.agregar_habitacion(i)
Nombre = input("Ingrese Nombre del hotel: ")
while True:
    print("\nBienvenidos al hotel", Nombre)
    print("1. Asignar habitacion")
    print("2. Liberar habitacion")
    print("3. Mostrar habitaciones libres")
    print("4. Mostrar habitaciones ocupadas")
    print("5. Buscar huesped por cedula")
    print("6. Entradas")
    print("7. Salidas")
    print("8. Salir")

    opc = int(input("Seleccione una opcion: "))

    if opc == 1:
        hotel.asignar_habitacion()
    elif opc == 2:
        hotel.liberar_habitacion()
    elif opc == 3:
        hotel.mostrar_libres()
    elif opc == 4:
        hotel.mostrar_ocupadas()
    elif opc == 5:
        hotel.buscar_cedula()
    elif opc == 6:
        hotel.mostrar_entradas()
    elif opc == 7:
        hotel.mostrar_salidas()
    elif opc == 8:
        print("Saliendo.... Adios")
        break
    else:
        print("Opcion no valida.")
# este codigo fue creado por David Cediel con un poco de ayuda de IA para ciertas parte 87/100


#Igualmente cuando un huésped se retira del hotel se actualiza la disponibilidad de las habitaciones, 
# el libro de entradas y el libro de salida.


#El director desea en un momento dado contar con la siguiente información:

#Consultas vigentes por huésped: (1) Individual y (2) total. Las consultas (2) totales pueden ser: (1) Por cédula y (2) por orden de llegada.
#Para cualquiera de las consultas entregar toda la información asociada al huésped.

#Consulta de habitaciones: (1) Lista de habitaciones disponibles y (2) Lista de habitaciones ocupadas.






