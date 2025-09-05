import numpy as np
import pandas as pd

ciudades = ["Quito", "Guayaquil", "Cuenca"]
semanas = 4
dias_por_semana = 7

rng = np.random.default_rng(42)
datos = rng.integers(low=12, high=31, size=(len(ciudades), dias_por_semana, semanas))

promedios_ciudad_semana = np.mean(datos, axis=1)
columnas = [f"Semana {i+1}" for i in range(semanas)]
df_promedios = pd.DataFrame(promedios_ciudad_semana, index=ciudades, columns=columnas).round(2)
df_promedios["Promedio General"] = np.mean(datos, axis=(1,2)).round(2)

# Guardar
df_promedios.to_csv("promedios_temperaturas.csv")
# (Opcional) crear detalle y guardarlo
tuplas = []
valores = []
for i, ciudad in enumerate(ciudades):
    for s in range(semanas):
        for d in range(dias_por_semana):
            tuplas.append((ciudad, f"Semana {s+1}", f"Día {d+1}"))
            valores.append(datos[i,d,s])
df_matriz = pd.DataFrame(tuplas, columns=["Ciudad","Semana","Día"])
df_matriz["Temperatura"] = valores
df_matriz.to_csv("matriz_temperaturas_detalle.csv", index=False)
