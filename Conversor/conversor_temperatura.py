"""
Programa: Conversor de temperatura
Descripción:
Este programa convierte una temperatura ingresada en grados Celsius
a grados Fahrenheit y muestra el resultado en pantalla.
"""

# Solicitar la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Fórmula de conversión
fahrenheit = (celsius * 9 / 5) + 32

# Verificar si la temperatura es mayor al cero absoluto
is_valid_temperature = celsius >= -273.15

# Mostrar resultado
if is_valid_temperature:
    print("La temperatura en grados Fahrenheit es:", fahrenheit)
else:
    print("Error: la temperatura ingresada no es válida.")
