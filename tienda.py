print("*******************************************")
print("*********       BIENVENIDO A      *********")
print("*********   TIENDA DE MASCOTAS    *********")
print("*******************************************")

num_perros = 10
num_gatos = 8
num_pajaros = 25
total = num_perros + num_pajaros + num_gatos

print('\nPor favor ingresa tu nombre')
nombre = input()
print('\nPor favor ingresa tu apellido')
apellido = input()

# Concatenación
nombre_completo = nombre + ' ' + apellido

print('Gracias por visitarnos,', nombre_completo)

print("Actualmente contamos con:")
print(" Perros:", num_perros, "\n", "Gatos:", num_gatos, "\n", "Pajaros:", num_pajaros)
print(" En total tenemos", total, "animales")