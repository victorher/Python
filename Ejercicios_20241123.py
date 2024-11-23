# funciones
# ################## clase de python funciones #############

# 1. Escribe una función llamada convertir_celsius_a_fahrenheit que reciba
# un valor en grados Celsius y devuelva su equivalente en fahrenheit


def converti_celsius_a_farehrenheit(celsius):
    try:
        celsius = float(celsius)
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    except ValueError:
        return "Error: por favor ingrese un valor válido."

# 2. Crea una función calcular_promedio que reciba una lista de números y
# devuelva el promedio. Valida que la lista no esté vacía.


def calcular_promedio(numeros):
    if not numeros:
        return "Error: La lista está vacía."

    try:
        suma = sum(numeros)
        cantidad = len(numeros)
        promedio = suma / cantidad
        return promedio
    except TypeError:
        return "Error: La lista debe contener solo números."

# 3. Desarrolla una función llamada calcular_factorial que calcule el factorial
# de un número entero positivo utilizando recursión.
# Asegúrate de manejar casos inválidos.


def calcular_factorial(n):
    if not isinstance(n, int):
        return "Error: El número debe ser un entero."
    if n < 0:
        return "Error: El número debe ser un entero positivo."

    if n == 0 or n == 1:
        return 1

    return n * calcular_factorial(n - 1)

# 4. Escribe una función llamada presentar que reciba un nombre y una edad
# como parámetros, e imprima un mensaje de bienvenida.
# Asegúrate de usar un parámetro por defecto para la edad.


def presentar(nombre, edad=18):
    print(f"¡Bienvenido, {nombre}! Tienes {edad} años.")


# ####################################
# HACER LOS LLAMADOS A LAS FUNCIONES #
# ####################################


def opcion_convertir_celsius_a_fahrenheit():
    celsius = input("Ingrese el valor de grados Celsius: ")
    respuesta = converti_celsius_a_farehrenheit(celsius)
    print(f"La conversión de grados Fahrenheit es: {respuesta}")


def opcion_calcular_promedio():
    numeros = input(
        "Ingrese una lista de números separados por comas: ")
    numeros = [float(num) for num in numeros.split(",")]
    resultado = calcular_promedio(numeros)
    print(f"El promedio de la lista es: {resultado}")


def opcion_calcular_factorial():
    numero = input("Ingrese un número entero positivo: ")
    try:
        numero = int(numero)
        resultado = calcular_factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")


def opcion_presentar():
    nombre = input("Ingrese su nombre: ")
    edad_input = input(
        "Ingrese su edad "
        "(o presione Enter para usar la edad por defecto): ")
    if edad_input:
        try:
            edad = int(edad_input)
        except ValueError:
            print(
                "Error: La edad debe ser un número entero."
                "Usando la edad por defecto de 18.")
            edad = 18
    else:
        edad = 18
    presentar(nombre, edad)

# ##################################
# MENU PARA ACCEDER A CADA FUNCIÓN #
# ##################################


def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Convertir Celsius a Fahrenheit")
        print("2. Calcular promedio")
        print("3. Calcular Factorial")
        print("4. Presentarse")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            opcion_convertir_celsius_a_fahrenheit()
        elif opcion == "2":
            opcion_calcular_promedio()
        elif opcion == "3":
            opcion_calcular_factorial()
        elif opcion == "4":
            opcion_presentar()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor,"
                  "seleccione una opción del 1 al 5.")


menu()
