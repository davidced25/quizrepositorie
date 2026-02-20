#El director de un hotel desea implementar una sistema de administración para saber la disponibilidad y asignación de habitaciones. 
# Para asignar, registra el número de cédula y el nombre de cada cliente a medida que llega al hotel, 
# junto con el número de habitación que ocupa (el antiguo libro de entradas).

# Clase Nodo
class huesped:
    def __init__(self):
        self.num = int(input("Ingrese número de habitación: "))
        self.estado = "Libre"
        self.cedula = None
        self.hora = None
        self.nombre = None
        self.siguiente = None 

# Clase Listas enlazada simple
class habitaciones:
    def __init__(self):
        self.cabeza = None
        
    def agg_habt(self):
        nuevo_nodo = huesped()
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def asignar_habt(self):
        cedula_buscada = input("Ingrese cédula del cliente: ")
        actual = self.cabeza
        while actual:
            if actual.estado == "Libre":
                actual.cedula = cedula_buscada
                actual.nombre = input("Ingrese nombre: ")
                actual.hora = input("Ingrese hora de llegada: ")
                actual.estado = "Ocupado"
                print(f"Habitacion {actual.num} asignada.")
                return
            actual = actual.siguiente
        print("No hay habitaciones disponibles.")

    def eliminar_habt(self, cedula):
        actual = self.cabeza
        while actual:
            if actual.cedula == cedula:
                actual.estado = "Libre"
                actual.cedula = None
                actual.nombre = None
                actual.hora = None
                return True
            actual = actual.siguiente
        return False

    def mostrar_habt_disp(self):
        actual = self.cabeza
        print("\nHabitaciones disponibles:")
        while actual:
            if actual.estado == "Libre":
                print(f"Habitacion {actual.num} esta libre")
            actual = actual.siguiente
  
    def mostrar_habt_ocup(self):
        actual = self.cabeza
        print("\nHabitaciones ocupadas:")
        while actual:
            if actual.estado == "Ocupado":
                print(f"Hab: {actual.num} | Cedula: {actual.cedula} | Nombre: {actual.nombre} | Llegada: {actual.hora}")
            actual = actual.siguiente


#Igualmente cuando un huésped se retira del hotel se actualiza la disponibilidad de las habitaciones, 
# el libro de entradas y el libro de salida.


#El director desea en un momento dado contar con la siguiente información:

#Consultas vigentes por huésped: (1) Individual y (2) total. Las consultas (2) totales pueden ser: (1) Por cédula y (2) por orden de llegada.
#Para cualquiera de las consultas entregar toda la información asociada al huésped.

#Consulta de habitaciones: (1) Lista de habitaciones disponibles y (2) Lista de habitaciones ocupadas.

