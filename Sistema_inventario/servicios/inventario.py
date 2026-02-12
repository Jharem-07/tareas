# servicios/inventario.py

from modelos.producto import Producto


class Inventario:
    """
    Clase encargada de gestionar todos los productos.
    Utiliza una lista como estructura principal de almacenamiento.
    """

    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        """
        Añade un producto validando que el ID no esté repetido.
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                return False  # ID repetido

        self.productos.append(producto)
        return True

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto por su ID.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                return True
        return False

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza cantidad o precio de un producto por ID.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                return True
        return False

    def buscar_por_nombre(self, nombre):
        """
        Permite búsqueda parcial de productos por nombre.
        """
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def mostrar_inventario(self):
        """
        Muestra todos los productos registrados.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)
