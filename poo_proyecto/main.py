from modelos.persona import Persona
from modelos.estudiante import Estudiante
from servicios.gestor_personas import GestorPersonas


def main():
    # Crear gestor
    gestor = GestorPersonas()

    # Crear instancias (objetos)
    persona1 = Persona("Andrés", 30)
    estudiante1 = Estudiante("Julissa", 20, "Ingeniería en Sistemas")

    # Agregar al gestor
    gestor.agregar_persona(persona1)
    gestor.agregar_persona(estudiante1)

    # Mostrar información (polimorfismo en acción)
    gestor.mostrar_todos()


if __name__ == "__main__":
    main()
