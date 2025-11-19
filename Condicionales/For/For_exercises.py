###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
"""
print("\nEjercicio 1:")

for i in range(2, 21):
    if i % 2 == 0:
        print(i)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

numeros = [10, 20, 30, 40, 50]
sum = 0
for num in numeros:
    sum += num
print(f"El total es: {sum}")
media = sum / len(numeros)

print("La media de la lista numeros es:", media)

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
numeros = [15, 5, 25, 10, 20]
frutas = ["manzana", "pera", "mandarina"]
max_num = 0
for num in numeros:
  if num > max_num:
    max_num = num
print(f"El número máximo es: {max_num}")

print("\nEjercicio 3:")

numeros = [15, 5, 25, 10, 20]
max_num = numeros[0]
for num in numeros:
    if num > max_num:
        max_num = num
print("El número máximo es:", max_num)"""

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

palabras = ["casa", "arbol", "sol", "elefante", "luna"]
for palabra in palabras:
    if len(palabra) > 5:
        print(palabra)
# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
letras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Introduce una letra: ").upper()
contador = 0
for caracter in letras:
    if caracter[0].upper() == letra:
        contador += 1
print(f"El número de palabras que empiezan con la letra {letra} es: {contador}")
