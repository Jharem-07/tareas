# descuento.py

# Función que calcula el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a una compra.

    Parámetros:
        monto_total (float): Monto total de la compra.
        porcentaje_descuento (float): Porcentaje de descuento a aplicar (por defecto 10%).

    Retorna:
        tuple: (monto_descuento, monto_final)
    """
    monto_descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - monto_descuento
    return monto_descuento, monto_final


# Llamadas a la función
if __name__ == "__main__":
    # Caso 1: solo monto total (usa el descuento por defecto del 10%)
    descuento1, total1 = calcular_descuento(200)
    print(f"Compra 1 -> Descuento: ${descuento1:.2f}, Total a pagar: ${total1:.2f}")

    # Caso 2: monto total + porcentaje específico
    descuento2, total2 = calcular_descuento(500, 20)
    print(f"Compra 2 -> Descuento: ${descuento2:.2f}, Total a pagar: ${total2:.2f}")
