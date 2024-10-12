print("Binebenidos al conversor de millas a kilometros")
print("Escribe un número en millas")
millas = input() #string

print('Millas tipo:', type(millas))
# convertir un string a nuúmeros
millas = float(millas)
print('Millas tipo:', type(millas))

# 1 milla = 1.609
kilometros = millas * 1.609

print("Las millas ingresadas:", millas)
print('Kilometros:', kilometros)