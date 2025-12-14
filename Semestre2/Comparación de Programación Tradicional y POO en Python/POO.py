# Programa para calcular el promedio semanal del clima
# usando Programación Orientada a Objetos (POO)

class ClimaSemanal:
    def __init__(self):
        """
        Constructor de la clase.
        Inicializa una lista vacía para las temperaturas.
        """
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas de los 7 días.
        """
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método que calcula el promedio semanal.
        """
        return sum(self.temperaturas) / len(self.temperaturas)


def main():
    """
    Función principal del programa.
    """
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Ejecución del programa
main()