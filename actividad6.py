# Actividad 6
print('\nActividad 6')

"""
Nivel básico:
Verificar si un número es positivo, negativo o cero
Descripción: Crea un programa que pida al usuario un número y verifique
si es positivo, negativo o cero.

Determinar si un estudiante aprobó o no
Descripción: Crea un programa que pida la calificación de un estudiante y
determine si ha aprobado (60 o más) o no.


Nivel intermedio:
Comprobar si un número es par o impar
Descripción: Crea un programa que pida al usuario un número y determine
si es par o impar.

Verificar si un número está dentro de un rango
Descripción: Crea un programa que pida al usuario un número y verifique si
está en el rango de 1 a 10 (inclusive).


Nivel Avanzado:

Clasificación de Números
    Descripción: Crea una función que reciba una lista de números enteros y
    clasifique cada número como "positivo", "negativo" o "cero". La función
    debe devolver un diccionario que contenga el conteo de cada categoría.

    Requisitos:

    Utilizar if, elif y else para clasificar los números.
    Deberá considerar si el número es impar o par, y agregar esta
    información al diccionario.

Cálculo de Tarifas de Envío
    Descripción: Diseña una función que calcule la tarifa de envío basada
    en el peso del paquete y el destino. La tarifa debe ser calculada
    usando las siguientes reglas:

    Menos de 1 kg: $5
    De 1 a 5 kg: $10
    Más de 5 kg: $20
    Si el destino es internacional, sumar un recargo del 50% al costo total.
    Requisitos:

Usa if y else para determinar el costo según el peso.
Usa if adicional para comprobar si el envío es internacional
y calcular el recargo correspondiente.
"""

#######################################################################
print('\nVerificar si un número es positivo, negativo o cero')


def validar_numero(num):
    """_summary_
    Verifica si un número es positivo, negativo o cero.
    Args:
        num (float): El número a verificar
    """
    if num > 0:
        return 'El valor es Positivo'
    elif num < 0:
        return 'El valor es Negativo'
    else:
        return 'El valor es Cero'


resultado = float(input("Introduce un número: "))
print(validar_numero(resultado))

#######################################################################
print('\nDeterminar si un estudiante aprobó o no')


def determinar_calidicacion(num):
    if num >= 60:
        return 'El estudiante aprobó'
    else:
        return 'El estudiante reprobó'


rta = float(input('Ingresa el valor: '))
print(determinar_calidicacion(rta))

#######################################################################
print('\nComprobar si un número es par o impar')
valor = float(input('Ingresa un número: '))
respuesta = valor % 2
if respuesta == 0:
    print('El número es par')
else:
    print('El número es Impar')

# ######################################################################
print('\nVerificar si un número está dentro de un rango')


def verifica_numero_en_rango(num):
    if 1 <= num <= 10:
        return 'En número está en el rango de 1 a 10'
    else:
        return 'El número no está en el rango de 1 a 10'


val = int(input('Ingresa un número: '))
print(verifica_numero_en_rango(val))

# ######################################################################
print('\nVarificar si un número es positivo o negativo')


def clasificar_numeros_extendido(lista):
    conteo = {
        "positivo_impar": 0,
        "positivo_par": 0,
        "negativo_impar": 0,
        "negativo_par": 0,
        "cero": 0
    }
    for num in lista:
        if num > 0:
            if num % 2 == 0:
                conteo["positivo_par"] += 1
            else:
                conteo["positivo_impar"] += 1
        elif num < 0:
            if num % 2 == 0:
                conteo["negativo_par"] += 1
            else:
                conteo["negativo_impar"] += 1
        else:
            conteo["cero"] += 1
    return conteo


entrada = input("Introduce una lista de números separados por comas: ")
lista_numeros = [int(num) for num in entrada.split(",")]
resultado = clasificar_numeros_extendido(lista_numeros)
print(resultado)

#######################################################################
print('\nCálculo de tarifas')


def calcular_tarifa_envio():
    try:
        peso = float(input("Introduce el peso del paquete en kg: "))
        if peso < 0:
            raise ValueError("El peso no puede ser negativo.")

        destino = input(
            "¿El envío es internacional? (sí/no): "
        ).strip().lower()

        if peso < 1:
            costo = 5
        elif 1 <= peso <= 5:
            costo = 10
        else:
            costo = 20

        if destino == "sí":
            costo *= 1.5

        return costo

    except ValueError as e:
        print(f"Error: {e}. Por favor, introduce un valor válido.")
        return None


tarifa = calcular_tarifa_envio()
if tarifa is not None:
    print(f"La tarifa de envío es: ${tarifa:.2f}")

# ################################################################################

print("Cálculo del mayor de tres números")


def mayor_de_tres_numeros():
    try:

        numeros = input(
            "Introduce tres números distintos separados por coma: "
        )

        lista_numeros = [float(num) for num in numeros.split(",")]

        if len(lista_numeros) != 3:
            print("Debes introducir exactamente tres números.")
            return

        if len(set(lista_numeros)) != 3:
            print("Los números deben ser distintos. Inténtalo de nuevo.")
            return

        mayor = max(lista_numeros)
        print(f"El mayor de los tres números es: {mayor}")

    except ValueError:
        print("Error: Por favor, introduce solo números válidos.")
