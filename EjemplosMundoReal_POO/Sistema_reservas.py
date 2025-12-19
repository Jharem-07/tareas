# Clase que representa a un Cliente
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_datos(self):
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}"


# Clase que representa una Habitación
class Habitacion:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio
        self.disponible = True

    def reservar(self):
        if self.disponible:
            self.disponible = False
            return "Habitación reservada con éxito."
        else:
            return "La habitación no está disponible."


# Clase que gestiona la Reserva
class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def confirmar_reserva(self):
        if self.habitacion.disponible:
            self.habitacion.reservar()
            total = self.habitacion.precio * self.dias
            return (
                f"{self.cliente.mostrar_datos()}\n"
                f"Habitación N°: {self.habitacion.numero}\n"
                f"Días: {self.dias}\n"
                f"Total a pagar: ${total}"
            )
        else:
            return "No se pudo realizar la reserva."


# Programa principal
cliente1 = Cliente("Jose Rodriguez", "0102030405")
habitacion1 = Habitacion(101, 50)

reserva1 = Reserva(cliente1, habitacion1, 3)
print(reserva1.confirmar_reserva())
