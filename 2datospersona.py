# Programa 2: Mostrar datos según género (con menú)
# Compatible con Python 3.8

def marco(texto: str, ancho: int = 50):
    linea = "═" * ancho
    print("╔" + linea + "╗")
    print("║" + texto.center(ancho) + "║")
    print("╚" + linea + "╝")

def leer_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("✗ Ingresa un número válido (solo dígitos).")

def leer_texto(mensaje: str) -> str:
    while True:
        t = input(mensaje).strip()
        if t:
            return t
        print("✗ No puede quedar en blanco.")

def normalizar_genero(txt: str):
    t = txt.strip().lower()
    if t in ("m", "masculino", "varon", "varón", "hombre"):
        return "M"
    if t in ("f", "femenino", "mujer"):
        return "F"
    return None

def ingresar_y_mostrar():
    marco(" Ingreso de datos ")
    nombre = leer_texto("Nombre: ")
    edad   = leer_entero("Edad (en años): ")

    while True:
        genero_bruto = leer_texto("Género (M/F o describa): ")
        genero = normalizar_genero(genero_bruto)
        if genero in ("M", "F"):
            break
        print("✗ Género no reconocido. Usa M/F, 'varón' o 'mujer'.")

    celular = leer_texto("Número de celular (puede incluir +56): ")

    marco(" Resultado ")
    if genero == "M":
        print(f"Nombre: {nombre}\nEdad:   {edad} años")
    else:
        print(f"Nombre:  {nombre}\nCelular: {celular}")
    print("─" * 54)

def ayuda():
    marco(" Ayuda ")
    print("• Opción 1: pide nombre/edad/género/celular y muestra según M o F.")
    input("\nENTER para volver al menú...")

def main():
    while True:
        marco(" Registro de Persona ")
        print("1) Ingresar datos y mostrar")
        print("2) Ayuda")
        print("0) Salir")
        print("─" * 54)
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            ingresar_y_mostrar()
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
