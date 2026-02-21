import os

# ==============================
# Clase Producto
# ==============================
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"


# ==============================
# Clase Inventario
# ==============================
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()

    # ------------------------------
    # Cargar productos desde archivo
    # ------------------------------
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    id, nombre, cantidad, precio = linea.strip().split(",")
                    self.productos[id] = Producto(id, nombre, int(cantidad), float(precio))
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo automáticamente.")
            open(self.archivo, "w").close()
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    # ------------------------------
    # Guardar productos en archivo
    # ------------------------------
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(str(producto) + "\n")
            print("Cambios guardados correctamente en el archivo.")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar: {e}")

    # ------------------------------
    # Añadir producto
    # ------------------------------
    def añadir_producto(self, id, nombre, cantidad, precio):
        if id in self.productos:
            print("Error: El producto ya existe.")
        else:
            self.productos[id] = Producto(id, nombre, cantidad, precio)
            self.guardar_en_archivo()
            print("Producto añadido exitosamente.")

    # ------------------------------
    # Actualizar producto
    # ------------------------------
    def actualizar_producto(self, id, cantidad, precio):
        if id in self.productos:
            self.productos[id].cantidad = cantidad
            self.productos[id].precio = precio
            self.guardar_en_archivo()
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    # ------------------------------
    # Eliminar producto
    # ------------------------------
    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    # ------------------------------
    # Buscar producto
    # ------------------------------
    def buscar_producto(self, id):
        if id in self.productos:
            producto = self.productos[id]
            print(f"ID: {producto.id}")
            print(f"Nombre: {producto.nombre}")
            print(f"Cantidad: {producto.cantidad}")
            print(f"Precio: ${producto.precio}")
        else:
            print("Producto no encontrado.")


# ==============================
# Menú de Consola
# ==============================
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Buscar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto(id, nombre, cantidad, precio)

        elif opcion == "2":
            id = input("ID del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "3":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "4":
            id = input("ID del producto a buscar: ")
            inventario.buscar_producto(id)

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


# Ejecutar sistema
if __name__ == "__main__":
    menu()