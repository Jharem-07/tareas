# Clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}"


# Clase Cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def comprar(self, producto, cantidad):
        total = producto.precio * cantidad
        return (
            f"Cliente: {self.nombre}\n"
            f"{producto.mostrar_info()}\n"
            f"Cantidad: {cantidad}\n"
            f"Total a pagar: ${total}"
        )


# Programa principal
producto1 = Producto("Cuaderno", 2.50)
cliente1 = Cliente("María López")

print(cliente1.comprar(producto1, 4))
