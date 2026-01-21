from modelos.libro import Libro
from servicios.biblioteca_service import BibliotecaService

def main():
    biblioteca = BibliotecaService()

    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
    libro2 = Libro("El principito", "Antoine de Saint-Exupéry")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    biblioteca.mostrar_libros()

if __name__ == "__main__":
    main()
