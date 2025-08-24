# Programa: Sistema de ventas - Tienda de Limpieza Sanitaria
# Autor: [Byron Linco]
# Descripción:
# Calcula el total a pagar considerando artículos, descuentos e IVA.
# Ahora incluye una opción de "seguir comprando o finalizar compra".

# ==========================
# Datos de la empresa
# ==========================
EMPRESA = "🧴 Limpieza Total S.A."
IVA = 0.19  # 19% IVA

# ==========================
# Lista de artículos y precios
# ==========================
articulos = {
    1: ("Mascarillas clínicas", 1000),
    2: ("Guantes clínicos", 1000),
    3: ("Delantal clínico", 2000),
    4: ("Amonio Cuaternario", 3000),
}

# ==========================
# Función para mostrar listado de precios
# ==========================
def mostrar_listado():
    print(f"\n===== {EMPRESA} =====")
    print("Listado de precios:")
    for codigo, (nombre, precio) in articulos.items():
        print(f"{codigo}. {nombre:20} $ {precio}")

# ==========================
# Función para calcular total
# ==========================
def calcular_total(compra, descuento):
    subtotal = 0
    print("\nResumen de la compra:")
    for codigo, cantidad in compra.items():
        nombre, precio = articulos[codigo]
        total_item = precio * cantidad
        subtotal += total_item
        print(f"- {nombre:20} x {cantidad} = $ {total_item}")

    # Aplicar descuento
    if descuento > 0:
        descuento_monto = subtotal * (descuento / 100)
        subtotal -= descuento_monto
        print(f"\nDescuento aplicado: {descuento}% (-${int(descuento_monto)})")

    # Calcular IVA
    iva_monto = subtotal * IVA
    total_final = subtotal + iva_monto

    print(f"\nSubtotal: ${int(subtotal)}")
    print(f"IVA (19%): ${int(iva_monto)}")
    print(f"TOTAL A PAGAR: ${int(total_final)}\n")

# ==========================
# Programa principal
# ==========================
def main():
    mostrar_listado()
    compra = {}

    # Ingreso de productos
    while True:
        try:
            codigo = int(input("\nIngrese el código del artículo: "))
            if codigo not in articulos:
                print("❌ Código inválido. Intente nuevamente.")
                continue

            cantidad = int(input(f"Ingrese la cantidad de '{articulos[codigo][0]}': "))
            if cantidad <= 0:
                print("❌ La cantidad debe ser positiva.")
                continue

            # Guardar en compra
            if codigo in compra:
                compra[codigo] += cantidad
            else:
                compra[codigo] = cantidad

            # Preguntar si desea seguir comprando
            print("\n¿Desea agregar más productos?")
            print("1. Sí, agregar más productos")
            print("2. No, finalizar compra")

            opcion = input("Seleccione una opción (1/2): ")

            if opcion == "2":
                break  # Termina el ciclo de compra
        except ValueError:
            print("❌ Entrada inválida. Intente nuevamente.")

    # Verificar si compró algo
    if not compra:
        print("\nNo se ingresaron artículos. Compra cancelada.")
        return

    # Preguntar descuento
    try:
        descuento = float(input("\nIngrese porcentaje de descuento (0 si no tiene): "))
        if descuento < 0 or descuento > 100:
            print("❌ Descuento inválido. Se usará 0%.")
            descuento = 0
    except ValueError:
        print("❌ Entrada inválida. Se usará 0%.")
        descuento = 0

    # Calcular total
    calcular_total(compra, descuento)


# ==========================
# Punto de inicio
# ==========================
if __name__ == "__main__":
    main()
