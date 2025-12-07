class Instrumento:
    def tocar(self):
        pass

class Guitarra(Instrumento):
    def tocar(self):
        return "Sonido de guitarra"

class Piano(Instrumento):
    def tocar(self):
        return "Sonido de piano"

def reproducir(sonido):
    print(sonido.tocar())
