# Programa 1: Mayor de tres números (con menú, muestra empates)
# Compatible con Python 3.8

def marco(texto: str, ancho: int = 44):
    linea = "═" * ancho
    print("╔" + linea + "╗")
    print("║" + texto.center(ancho) + "║")
    print("╚" + linea + "╝")

def leer_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("✗ Eso no es un número entero. Intenta nuevamente.")

def mostrar_resultado(a: int, b: int, c: int):
    valores = [("A", a), ("B", b), ("C", c)]
    mayor = max(v for _, v in valores)
    etiquetas_mayor = [etq for etq, v in valores if v == mayor]

    marco(" Resultado ")
    print(f"A = {a}\nB = {b}\nC = {c}\n")
    if len(etiquetas_mayor) == 1:
        print(f"✔ El mayor es {mayor} (número {etiquetas_mayor[0]}).")
    else:
        juntos = ", ".join(etiquetas_mayor)
        print(f"✔ El mayor es {mayor} (empate entre: {juntos}).")
    print("─" * 48)

def ayuda():
    marco(" Ayuda ")
    print("• Opción 1: Ingresa tres enteros (A, B, C) y muestra el mayor.")
    print("• Indica empates si los hay.")
    input("\nENTER para volver al menú...")

def main():
    while True:
        marco(" Comparador de Tres Números ")
        print("1) Ingresar números y ver el mayor")
        print("2) Ayuda")
        print("0) Salir")
        print("─" * 48)
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            marco(" Ingreso de Números ")
            a = leer_entero("Ingresa A: ")
            b = leer_entero("Ingresa B: ")
            c = leer_entero("Ingresa C: ")
            print()
            mostrar_resultado(a, b, c)
            input("ENTER para volver al menú...")
        elif opcion == "2":
            ayuda()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("✗ Opción inválida.\n")

if __name__ == "__main__":
    main()
