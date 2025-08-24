# Programa: Tabla de multiplicar
# Autor: [Byron Linco]
# Descripción:
# Este programa solicita al usuario ingresar un número positivo
# y luego muestra por pantalla su tabla de multiplicar del 1 al 10.

def tabla_multiplicar(numero):
    """
    Función que imprime la tabla de multiplicar de un número
    desde el 1 hasta el 10.
    """
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):  # Recorre del 1 al 10
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


def main():
    """
    Función principal del programa.
    Pide un número positivo y muestra su tabla de multiplicar.
    Permite al usuario repetir o salir.
    """
    while True:
        try:
            # El usuario debe ingresar un número positivo
            numero = int(input("\nIngrese un número positivo: "))
            
            if numero > 0:
                # Si el número resulta ser positivo, se mostrara la tabla
                tabla_multiplicar(numero)
            else:
                print("❌ El número debe ser positivo. Intente nuevamente.")
                continue  # Al no ingresar un número positvo, el programa solicitara nuevamente ingresar un número

            # Preguntamos si quiere continuar
            opcion = input("\n¿Desea calcular otra tabla? (s/n): ").lower()
            if opcion != "s":
                print("\n✅ Programa finalizado. ¡Gracias por usarlo!")
                break
        except ValueError:
            print("❌ Entrada inválida. Por favor ingrese un número entero.")


# Punto de inicio
if __name__ == "__main__":
    main()
