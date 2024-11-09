    # 1. Mayor de Tres Números: Cargar tres números distintos por teclado y mostrar cuál es el mayor
    
print("Cálcular de tres números distintos cual es el mayor\n")

def mayor_de_tres_numeros():
    try:
        
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        num3 = float(input("Introduce el tercer número: "))

        if num1 == num2 or num1 == num3 or num2 == num3:
            print("Los números deben ser distintos. Inténtalo de nuevo.")
            return

        mayor = max(num1, num2, num3)
        print(f"El mayor de los tres números es: {mayor}")

    except ValueError:
        print("Error: Por favor, introduce solo números válidos.")

mayor_de_tres_numeros()

    # 2. Clasificación de Números: Ingresar un número entero y mostrar si es positivo, negativo o nulo (cero)
    
print("\nVerifica si un número es positivo o negativo o nulo.")
def clasificar_numero():
    try:
        
        num = float(input("Introduce un número: "))
        
        if num == 0:
            print("El valor es cero")
            return
        
        if num > 0:
            print("El valor es positivo")
            return
        
        if num < 0:
            print("El valor es negativo")
            return
        
    except ValueError as e:
        print(f"Error: {e}. Por favor, introduce un valor válido.")
        return None
    
clasificar_numero()

    #Verificar Navidad: Crear un programa que pida una fecha y verifique si corresponde a Navidad (25 de diciembre)
    
from datetime import datetime

print("\nVerificar si la fecha es navidad en Colombia")
def verifica_si_es_navidad():
    
    try:

        fecha = input("Intruduce una fecha formato dd/mm/yyyy: ")
        
        print(fecha)
        
        fecha_bus = datetime.strptime(fecha, "%d/%m/%Y")
        
        if fecha_bus.month == 12 and fecha_bus.day == 25:
            print("¡Sí! La fecha corresponde a Navidad.")
        else:
            print("No, la fecha no corresponde a Navidad.")
        
    except ValueError:
        print("Error: Formato de fecha inválido. Asegúrate de usar dd/mm/yyyy.")
        
verifica_si_es_navidad()

    # 4. Menores a Diez: Ingresar tres números. Si todos son menores a 10, imprimir "Todos los números son menores a diez". 
    # Si al menos uno es menor a 10, imprimir "Alguno de los números es menor a diez".
    
print("\nVerificar si los números son menores a 10")
def verificar_numeros():
    
    try:
        
        numeros = []
        for i in range(3):
            num = float(input(f"Ingrese el número {i + 1}: "))
            numeros.append(num)

        
        todos_menores = all(num < 10 for num in numeros)
        alguno_menor = any(num < 10 for num in numeros)

        
        if todos_menores:
            print("Todos los números son menores a diez.")
        elif alguno_menor:
            print("Alguno de los números es menor a diez.")
        else:
            print("Todos los números son 10 o mayores.")

    except ValueError:
        print("Error: no se pueden ingresar valores nulos")


verificar_numeros()


    # 5. Contador hasta un Número: Codificar un programa que solicite un valor positivo e imprima los números del 1 hasta ese valor.
    
print("\nContador de números")
def contador_hasta_numero():
    try:
        
        valor = int(input("Introduce un número positivo: "))
        
        
        if valor <= 0:
            print("Por favor, ingresa un número positivo.")
            return
        
        
        for i in range(1, valor + 1):
            print(i)

    except ValueError:
        print("Error: Por favor, ingresa un número entero válido.")

contador_hasta_numero()

    # 6. Suma y Promedio de Valores: Desarrollar un programa que pida la carga de 10 valores y luego muestre la suma y el promedio de esos valores.
    
print("\nSuma y Promedio de Valores")
def suma_y_promedio():
    try:
        valores = []
        
        for i in range(10):
            num = float(input(f"Ingrese el valor {i + 1}: "))
            valores.append(num)
        
        suma = sum(valores)
        promedio = suma / len(valores)
 
        print(f"La suma de los valores es: {suma}")
        print(f"El promedio de los valores es: {promedio}")

    except ValueError:
        print("Error: No se pueden ingresar valores nulos")

suma_y_promedio()

    # 7. Básico: Escribir un programa que imprima los números del 1 al 50.
    
print("\nImprime valores del 1 al 50")
def imprimir_numeros():
    for i in range(1, 51):
        print(i)

imprimir_numeros()

    # 8. Intermedio: Desarrollar un programa que solicite la carga de 5 números e imprima la suma de los números ingresados.
    
def suma_de_numeros():
    try:
        
        suma = 0 
        
        for i in range(5):
            num = float(input(f"Ingrese el número {i + 1}: "))
            suma += num  
        
        print(f"La suma de los números ingresados es: {suma}")

    except ValueError:
        print("Error: Por favor, ingrese solo números válidos.")

suma_de_numeros()

    # 9. Avanzado: Crear un programa que lea n pares de datos (base y altura) de triángulos, 
    # e informe la superficie de cada triángulo y cuántos tienen una superficie mayor a 12.
   
print("\nCrear un programa que lea n pares de datos (base y altura)") 
def calcular_superficie_triangulos():
    try:
        
        n = int(input("¿Cuántos triángulos deseas ingresar? "))
        contador_mayores_a_12 = 0

        for i in range(n):
            base = float(input(f"Ingrese la base del triángulo {i + 1}: "))
            altura = float(input(f"Ingrese la altura del triángulo {i + 1}: "))
            
            
            superficie = (base * altura) / 2
            
            
            print(f"La superficie del triángulo {i + 1} es: {superficie}")
            
            
            if superficie > 12:
                contador_mayores_a_12 += 1

        
        print(f"Número de triángulos con superficie mayor a 12: {contador_mayores_a_12}")

    except ValueError:
        print("Error: Por favor, ingrese solo números válidos.")

calcular_superficie_triangulos()

    # 10. Básico: Crea una lista con 5 enteros y calcula la suma de todos sus elementos.
    
print("\nLista con 5 enteros y sumarlos")
def suma_de_enteros():
    try:
        
        numeros = []
        
        for i in range(5):
            num = int(input(f"Ingrese el entero {i + 1}: "))
            numeros.append(num)  

        
        suma = sum(numeros)

        print(f"La suma de los elementos de la lista es: {suma}")

    except ValueError:
        print("Error: Por favor, ingrese solo números enteros válidos.")

suma_de_enteros()


    # 11. Intermedio: Define una lista que contenga los nombres de los primeros cuatro meses del año y muestra solo el primer y el último mes.
    
print("\nDefine una lista que contenga los nombres de los primeros cuatro meses del año \ny muestra solo el primer y el último mes")
def mostrar_meses():
    meses = [] 

    try:
        
        for i in range(4):
            mes = input(f"Ingrese el nombre del mes {i + 1}: ")
            meses.append(mes)  
        
        if len(meses) < 4:
            raise ValueError("Se requieren exactamente 4 meses.")

        primer_mes = meses[0]
        ultimo_mes = meses[-1]

        print(f"El primer mes es: {primer_mes}")
        print(f"El último mes es: {ultimo_mes}")

    except ValueError as e:
        print(f"Error: {e}. Asegúrate de ingresar los nombres correctamente.")

mostrar_meses()

    # 12. Avanzado: Crea una lista que almacene el nombre de un alumno y sus dos notas. Luego, imprime el nombre del alumno y el promedio de sus notas.
    
print("\nCrea una lista que almacene el nombre de un alumno y sus dos notas. \nLuego, imprime el nombre del alumno y el promedio de sus notas.")
def calcular_promedio():
    try:
        
        nombre = input("Ingrese el nombre del alumno: ")

        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))

        promedio = (nota1 + nota2) / 2
        
        print(f"El alumno {nombre} tiene un promedio de: {promedio:.2f}")

    except ValueError:
        print("Error: Por favor, ingrese solo números válidos para las notas.")

calcular_promedio()








