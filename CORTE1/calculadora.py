class Calculadora:
    def __init__(self):
        pass

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: No se puede dividir por cero"

# Función principal
def main():
    calc = Calculadora()

    while True:
        print("\n=== Calculadora ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción (1/2/3/4/5): ")

        if opcion == '5':
            print("¡Adiós!")
            break

        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            print(f"Resultado: {calc.sumar(num1, num2)}")
        elif opcion == '2':
            print(f"Resultado: {calc.restar(num1, num2)}")
        elif opcion == '3':
            print(f"Resultado: {calc.multiplicar(num1, num2)}")
        elif opcion == '4':
            print(f"Resultado: {calc.dividir(num1, num2)}")
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Llamamos directamente a la función principal
main()
