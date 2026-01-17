class Persona:
    """
    Clase base que representa a una persona.
    Aplica encapsulación usando atributos privados.
    """

    def __init__(self, nombre, edad):
        self.__nombre = nombre  # atributo privado
        self.__edad = edad      # atributo privado

    # Métodos getters
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Métodos setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def mostrar_info(self):
        """
        Método que será sobrescrito (polimorfismo)
        """
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"
