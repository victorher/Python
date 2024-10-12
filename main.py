# Actividad 4: Ejercicio 1: Crear Variables
# En este ejercicio, se te pide creae variables para almacenar datos personales.
# Deberas definir:
# 1, Tu edad como un número entero (int).
# 2. Tu altura en metros como en número de punto flotante (float)
# 3. Tu nombre completo como una cadena de texto (str).
# 4. Un valor booleano que indique si tienes mascota (bool).
# 5. Una lista que contenga los nombres de tres amigos (list).

print('Actividad 4:\nTipos de variables \n')
edad = 35
altuta = 1.79
nombres = 'Victor Hernandez'
tiene_mascota = True
amigos = ['Pedro', 'Pablo', 'Jacinto', 'Jose']

print('Edad', type(edad))
print('Altura', type(altuta))
print('Nombres', type(nombres))
print('Tiene_Mascota', type(tiene_mascota))
print('amigos', type(amigos))

# Actidad 5:
print("\nActividad 5\nRealiza un if donde determine si una persona es mayor de edad o no\n")

print('Ingresa tu edad')
i_edad = int(input())

if i_edad < 18:
    print("Menor de edad\n")
else:
    print('Mayor de edad\n')


