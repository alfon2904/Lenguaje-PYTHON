###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
"""
print("\nEjercicio 1:")

for i in range(1, 11):
    print(i)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")

for x in range(1, 21):
    if x % 2 != 0:
        print(x)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")

for y in range(1, 51):
    if y % 5 == 0:
        print(y)

"""
# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
for number in range(10,0,-1):
    print(number)
print("despegue!!!!")


"""
# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
x = 0
for i in range(1, 101):
    x += i
    print(x)
print(x)

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
#print("\nEjercicio 6:")

#number = int(input("Ingrese un número para ver su tabla de multiplicar: "))
#for i in range(1, 11):
#    print(f"{number} x {i} = {number * i}")
"""