from modelos.persona import Persona


class Estudiante(Persona):
    """
    Clase derivada que hereda de Persona.
    Aplica herencia y polimorfismo.
    """

    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def mostrar_info(self):
        """
        Polimorfismo: se redefine el método de la clase base
        """
        return f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, Carrera: {self.carrera}"
