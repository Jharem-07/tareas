class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        return "El vehículo está encendido"

class Auto(Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)
        self.puertas = puertas

    def informacion(self):
        return f"Auto marca {self.marca} con {self.puertas} puertas."
