import os

print("My working directory is", os.getcwd())

# Pide al usuario que ingrese un número
x = int(input("Ingrese un número: "))

# Verifica si el número es par o impar
if x % 2 == 0:
    print(x, 'es un número par')
else:
    print(x, 'es un número impar')
