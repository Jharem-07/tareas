class Libro:
    def __init__(self, titulo, autor):
        # Constructor: inicializa los atributos del objeto
        self.titulo = titulo
        self.autor = autor
        print(f"📘 Libro creado: {self.titulo}")

    def __del__(self):
        # Destructor: se ejecuta cuando el objeto deja de existir
        print(f"🗑️ Libro eliminado: {self.titulo}")
