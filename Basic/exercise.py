###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

"""print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")


#solution
name = input("Ingresa tu nombre: ")
city = input("Ingresa tu ciudad: ")
print(f"tu nombre es {name}")
print(f"Y vives en {city}")"""

### Completa aquí

"""print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))  # int

### Completa aquí


print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")


str_num = "12345"
second_number = 3.99
int_num = int(str_num)
float_num = float(int_num)
int_num_second = int(second_number)

print(int_num)
print(float_num)
print(int_num_second)

#aproximar 3.99 a un entero mas cercano
print(round(second_number))

### Completa aquí

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")


# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"


name = input("Ingresa tu nombre: ")
age = int(input("Ingresa tu edad: "))
height = float(input("Ingresa tu altura: "))

print(f"Hola, mi nombre es {name}, y tengo {age} años, mido {height} metros.")"""


print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi = 3.14159
round_pi = round(pi)
division = round_pi // 2
print(division)  