# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

from os import system
if system("clear") != 0: system("cls")

print("Ejercicio 1: Añadir y modificar elementos", "\n")
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
"""
lista_numeros = [1, 2, 3, 4, 5]
lista_numeros.append(6)
print(lista_numeros, "\n")
lista_numeros.insert(2, 10)
print(lista_numeros, "\n")
lista_numeros[0] = 0
print(lista_numeros, "\n")

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear()..
lista_a.extend(lista_b)
print("extend() =", lista_a, "\n")
lista_a.remove(1)
print("remove(1) =", lista_a, "\n")
elemento_eliminado = lista_a.pop(3)
print("pop(3) =", elemento_eliminado, "=", lista_a, "\n")
lista_b.clear()
print("clear() =", lista_b, "\n")

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista original: ", lista_numeros, "\n")
del lista_numeros[2:4]
print("Resultado: ", lista_numeros, "\n")

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

lista_numeros = [5, 2, 8, 1, 9, 4, 2]
print(f"Lista original: {lista_numeros}\n")
lista_numeros.sort()
print(f"Lista ordenada: {lista_numeros}\n")
print(f"¿Cuántas veces aparece el número 2 en la lista? {lista_numeros.count(2)}")
print(f"¿El numero 7 está en la lista? {7 in lista_numeros}\n")

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original
referencia[0] = 10
"""
# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ["Manzana", "pera", "BANANA", "naranja"]
frutas.sort(key=str.lower)
print(frutas)
