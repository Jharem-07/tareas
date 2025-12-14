# Programa para calcular el promedio semanal del clima
# usando Programación Tradicional

def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas de los 7 días de la semana
    y las guarda en una lista.
    """
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio semanal a partir de una lista de temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)


def main():
    """
    Función principal del programa.
    """
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")


# Ejecución del programa
main()
