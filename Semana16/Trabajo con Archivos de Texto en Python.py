# Tarea: Trabajo con Archivos de Texto en Python

# 1. Escritura de Archivo de Texto
# Creamos el archivo 'my_notes.txt' y escribimos tres notas personales

with open("my_notes.txt", "w") as archivo:
    archivo.write("Hoy avancé con mis tareas de programación.\n")
    archivo.write("Necesito repasar estructuras de datos.\n")
    archivo.write("Me siento más seguro trabajando con archivos en Python.\n")

# 2. Lectura de Archivo de Texto
# Abrimos el archivo y leemos línea por línea

with open("my_notes.txt", "r") as archivo:
    print("Contenido del archivo línea por línea:\n")
    linea = archivo.readline()
    while linea:
        print(linea.strip())  # .strip() elimina saltos de línea extra
        linea = archivo.readline()

# 3. Cierre del archivo
# No es necesario cerrar manualmente porque usamos 'with',
# que se encarga de cerrar el archivo automáticamente.
