# Primer hola mundo
texto = "Primer ejemplo: "
print(texto + "Hola Mundo")

print("Ingresa un valor")
a = input()

# Variables
A = 13
print("Variable: " + str(A))

# Ejecutar numeros pares
numPar = [1,2,3,4,5,6,7,8,9,10]
resPar = [num for num in numPar if num % 2 == 0]
print("Números pares: " + str(resPar))

# Multiplicar cada  número por 2
x = 2
resMul = [num * x for num in numPar]
print("Numeros multiplicados por", x,":", resMul)

# Exponente de numero par
y = 3
resExp = [num ** y for num in numPar if num % 2 == 0]
print("Números pares con exponente", y,":", resExp)