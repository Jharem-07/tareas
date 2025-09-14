# Función para calcular la temperatura promedio por ciudad
def calcular_promedio_temperaturas(datos_ciudades):
    """
    Calcula la temperatura promedio de cada ciudad a partir de sus registros semanales.

    Parámetros:
        datos_ciudades (dict): Un diccionario donde la clave es el nombre de la ciudad
                               y el valor es una lista de listas con las temperaturas
                               semanales.

                               Ejemplo:
                               {
                                   "Quito": [[20, 22, 19, 21], [18, 20, 19, 22]],
                                   "Guayaquil": [[28, 30, 29, 31], [27, 28, 29, 30]]
                               }

    Retorna:
        dict: Un diccionario con la ciudad como clave y su temperatura promedio como valor.
    """
    promedios = {}

    for ciudad, semanas in datos_ciudades.items():
        # "flatten" para unir todas las semanas en una sola lista
        temperaturas = [temp for semana in semanas for temp in semana]

        # Calcular promedio
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = round(promedio, 2)  # redondeo a 2 decimales

    return promedios


# ---------------- PRUEBA DE LA FUNCIÓN ----------------
if __name__ == "__main__":
    datos = {
        "Quito": [
            [20, 22, 19, 21],
            [18, 20, 19, 22],
            [21, 23, 20, 22],
            [19, 21, 20, 22]
        ],
        "Guayaquil": [
            [28, 30, 29, 31],
            [27, 28, 29, 30],
            [29, 31, 30, 32],
            [28, 29, 30, 31]
        ],
        "Cuenca": [
            [15, 16, 17, 16],
            [14, 15, 16, 17],
            [16, 17, 15, 16],
            [15, 16, 17, 15]
        ]
    }

    resultados = calcular_promedio_temperaturas(datos)
    print("Temperaturas promedio por ciudad:")
    for ciudad, promedio in resultados.items():
        print(f"{ciudad}: {promedio} °C")
