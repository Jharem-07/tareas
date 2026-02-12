# main.py

from modelos.producto import Producto
from servicios.inventario import Inventario


def menu():
    print("\n===== SISTEMA DE GESTIÓN DE INVENTARIOS =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = input("Ingrese ID: ")
                nombre = input("Ingrese nombre: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))

                producto = Producto(id_producto, nombre, cantidad, precio)
                if inventario.añadir_producto(producto):
                    print("Producto añadido correctamente.")
                else:
                    print("Error: El ID ya existe.")

            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad y precio.")

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            if inventario.eliminar_producto(id_producto):
                print("Producto eliminado correctamente.")
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")

            try:
                cantidad = input("Nueva cantidad (dejar vacío si no desea cambiar): ")
                precio = input("Nuevo precio (dejar vacío si no desea cambiar): ")

                nueva_cantidad = int(cantidad) if cantidad else None
                nuevo_precio = float(precio) if precio else None

                if inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio):
                    print("Producto actualizado correctamente.")
                else:
                    print("Producto no encontrado.")

            except ValueError:
                print("Error: Valores inválidos.")

        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
