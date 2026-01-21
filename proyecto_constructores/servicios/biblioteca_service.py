class BibliotecaService:
    def __init__(self):
        # Constructor: inicializa la lista de libros
        self.libros = []
        print("📚 Biblioteca iniciada")

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro agregado: {libro.titulo}")

    def mostrar_libros(self):
        print("\n📖 Libros en la biblioteca:")
        for libro in self.libros:
            print(f"- {libro.titulo} | {libro.autor}")

    def __del__(self):
        # Destructor: limpia recursos
        print("🧹 Cerrando biblioteca")
