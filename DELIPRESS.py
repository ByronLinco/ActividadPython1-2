# ===========================================
# Empresa: "🥪 Deli Press"
# ===========================================

# --- MENÚ DE SÁNDWICHES CON EMOJIS ---
sandwiches = {
    "🥩 Churrasco": 1500,
    "🌭 Completo": 1000,
    "🥦 Vegetariano": 2000,
    "🧀🍞 Barros Luco 🏥": 3000
}

print("===================================")
print("   🥪 BIENVENIDO A DELI PRESS 🏥")
print("===================================")

print("\n--- 📋 Menú de Sándwiches ---")
for nombre, precio in sandwiches.items():
    print(f"{nombre:<25} ${precio}")

# Cantidades de sándwiches
cant_churrasco = int(input("\n🥩 ¿Cuántos Churrascos quieres?: "))
cant_completo = int(input("🌭 ¿Cuántos Completos quieres?: "))
cant_vegetariano = int(input("🥦 ¿Cuántos Vegetarianos quieres?: "))
cant_barros_luco = int(input("🧀🍞 ¿Cuántos Barros Luco quieres?: "))

# Calcular subtotal
subtotal = (
    cant_churrasco * sandwiches["🥩 Churrasco"] +
    cant_completo * sandwiches["🌭 Completo"] +
    cant_vegetariano * sandwiches["🥦 Vegetariano"] +
    cant_barros_luco * sandwiches["🧀🍞 Barros Luco 🏥"]
)

# Descuento
tiene_descuento = input("\n🎟️ ¿Tienes un código de descuento? (s/n): ").lower()
if tiene_descuento == "s":
    subtotal *= 0.9  # 10% de descuento
    print("✅ Se aplicó un 10% de descuento")

# IVA
iva = subtotal * 0.19
total = subtotal + iva

# 📄 Boleta final
print("\n===================================")
print("          🧾 RESUMEN DE COMPRA")
print("===================================")
print(f"Subtotal: ${round(subtotal)}")
print(f"IVA (19%): ${round(iva)}")
print("-----------------------------------")
print(f"💵 TOTAL A PAGAR: ${round(total)}")
print("===================================")
print("\n🙌 Gracias por su compra en '🥪 Deli Press'")
