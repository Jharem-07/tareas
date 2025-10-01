# Crear un diccionario con información ficticia
informacion_personal = {
    "nombre": "Carlos Pérez",
    "edad": 25,
    "ciudad": "Quito",
    "profesion": "Estudiante"
}

# Acceder y modificar valores
# Cambiamos el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor "profesion" (ya existe, así que la actualizamos)
informacion_personal["profesion"] = "Ingeniero en Software"

# Verificar existencia de la clave "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999999999"  # Número ficticio

# Eliminar la clave "edad"
informacion_personal.pop("edad", None)

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)
