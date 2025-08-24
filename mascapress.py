# ===========================================
# Empresa: "Masca Press"
# ===========================================

print("===== Bienvenido a Masca Press =====")

# Banner con bordes y símbolos ASCII
print("\n" + "="*50)
print("|| [HOSPITAL] [MASCARILLA] Masca Press [MASCARILLA] [HOSPITAL] ||")
print("="*50 + "\n")

# Precio del producto
precio_mascarilla = 500
print(f"--- Producto ---")
print(f"Mascarilla lavable: ${precio_mascarilla} [MASCARILLA]\n")

# Cantidad de mascarillas
cant_mascarillas = int(input("Ingrese la cantidad de mascarillas que desea comprar: "))

# Subtotal
subtotal = cant_mascarillas * precio_mascarilla
print(f"\nSubtotal: ${subtotal} [DINERO]")

# Envío
if subtotal > 15000:
    envio = 0
    print("! Envío gratis por compras sobre $15.000 !")
else:
    print("\nOpciones de envío:")
    print("1. Misma comuna ($1.000) [CASA]")
    print("2. Comuna aledaña ($2.000) [CAMION]")
    print("3. Otra comuna ($3.000) [AVION]")
    opcion_envio = int(input("Seleccione opción de envío (1-3): "))

    if opcion_envio == 1:
        envio = 1000
    elif opcion_envio == 2:
        envio = 2000
    else:
        envio = 3000

# Total con IVA
total = (subtotal + envio) * 1.19

# Resumen con bordes
print("\n" + "="*50)
print("||           RESUMEN DE SU COMPRA           ||")
print("="*50)
print(f"|| Cantidad de mascarillas: {cant_mascarillas} [MASCARILLA]")
print(f"|| Subtotal: ${subtotal}")
print(f"|| Envío: ${envio}")
print(f"|| IVA (19% incluido) -> Total a pagar: ${round(total)} [TOTAL]")
print("="*50)

print("\nGracias por comprar en 'Masca Press' [HOSPITAL]")

# Pausa final para que no se cierre la ventana
input("\nPresiona Enter para salir...")
