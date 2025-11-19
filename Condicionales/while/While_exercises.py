###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
"""print("\nEjercicio 1:")
number = 10
while number > 0:
    print(number)
    number -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
sum_even = 0
x = 1
while x <= 20:
    if x % 2 == 0:
        sum_even += x
    x += 1
print("La suma de los números pares entre 1 y 20 es:", sum_even)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

num = int(input("Introduce un número entero positivo: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print("El factorial es:", factorial)

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")


pasword = input("introduzca una contraseña:")
while len(pasword)<=8:
    pasword = input("La contraseña debe tener al menos 8 caracteres. Inténtalo de nuevo:")
print("Contraseña válida")"""
# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
i = int(input("introduce un número para ver su tabla de multiplicar: ")  )
x = 1
while x <= 10:
    result = i * x
    print(f"{i} x {x} = {result}")
    x += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
