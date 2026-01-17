class GestorPersonas:
    """
    Clase encargada de gestionar personas y estudiantes.
    """

    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def mostrar_todos(self):
        for persona in self.personas:
            print(persona.mostrar_info())
