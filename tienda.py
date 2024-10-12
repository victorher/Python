print("*******************************************")
print("*********       BIENVENIDO A      *********")
print("*********   TIENDA DE MASCOTAS    *********")
print("*******************************************")

num_perros = 10
num_gatos = 8
num_pajaros = 25
total = num_perros + num_pajaros + num_gatos

nombre = input('Por favor ingresa tu nombre: ')
apellido = input('Por favor ingresa tu apellido: ')

# Concatenación
nombre_completo = nombre + ' ' + apellido

print('\nGracias por visitarnos,', nombre_completo)

print("Actualmente contamos con:")
print("Perros:", num_perros, "\nGatos:", num_gatos, "\nPajaros:", num_pajaros)
print(" En total tenemos", total, "animales")