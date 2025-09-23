
informacion_personal = {
    "nombre": "Jonathan De La Ese",
    "edad": 17,
    "ciudad": "Santa Lucía, Guayas",
    "profesion": "Estudiante"
}


informacion_personal["ciudad"] = "Santa Lucía"


informacion_personal["profesion"] = "Ingeniero en Tecnologias de la Información"
informacion_personal["edad"] = 17

if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999999999"


informacion_personal.pop("edad", None)


print("Diccionario final:", informacion_personal)
