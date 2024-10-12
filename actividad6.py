# Actividad 6
print('\nActividad 6')
""" 
Nivel básico:
Verificar si un número es positivo, negativo o cero
Descripción: Crea un programa que pida al usuario un número y verifique si es positivo, negativo o cero.

Determinar si un estudiante aprobó o no
Descripción: Crea un programa que pida la calificación de un estudiante y determine si ha aprobado (60 o más) o no.


Nivel intermedio:
Comprobar si un número es par o impar
Descripción: Crea un programa que pida al usuario un número y determine si es par o impar.

Verificar si un número está dentro de un rango
Descripción: Crea un programa que pida al usuario un número y verifique si está en el rango de 1 a 10 (inclusive). 


Nivel Avanzado:

Clasificación de Números
    Descripción: Crea una función que reciba una lista de números enteros y clasifique cada número como "positivo", "negativo" o "cero". La función debe devolver un diccionario que contenga el conteo de cada categoría.

    Requisitos:

    Utilizar if, elif y else para clasificar los números.
    Deberá considerar si el número es impar o par, y agregar esta información al diccionario.

Cálculo de Tarifas de Envío
    Descripción: Diseña una función que calcule la tarifa de envío basada en el peso del paquete y el destino. La tarifa debe ser calculada usando las siguientes reglas:

    Menos de 1 kg: $5
    De 1 a 5 kg: $10
    Más de 5 kg: $20
    Si el destino es internacional, sumar un recargo del 50% al costo total.
    Requisitos:

Usa if y else para determinar el costo según el peso.
Usa if adicional para comprobar si el envío es internacional y calcular el recargo correspondiente.
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
  
#######################################################################  
print('\nVerificar si un número está dentro de un rango')
def verifica_numero_en_rango(num):
    if 1 <= num <= 10:
        return 'En número está en el rango de 1 a 10'
    else:
        return 'El número no está en el rango de 1 a 10'
    
val = int(input('Ingresa un número: '))
print(verifica_numero_en_rango(val))