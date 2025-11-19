###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales


"""number_1 = float(input("Introduce el primer número: "))
number_2 = float(input("Introduce el segundo número: "))

if number_1 > number_2:
    print(f"El número {number_1} es mayor que {number_2}.")
elif number_1 < number_2:
    print(f"El número {number_2} es mayor que {number_1}.")
else:
    print(f"Los números {number_1} y {number_2} son iguales.")"""

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

number_1 = float(input("Introduce el primer número: "))
number_2 = float(input("Introduce el segundo número: "))
operation = input("Introduce la operación (+, -, *, /): ")

if operation == "+":
    result = number_1 + number_2
    print(f"El resultado de {number_1} + {number_2} es {result}.")
elif operation == "-":
    result = number_1 - number_2
    print(f"El resultado de {number_1} - {number_2} es {result}.")
elif operation == "*":
    result = number_1 * number_2
    print(f"El resultado de {number_1} * {number_2} es {result}.")
elif operation == "/":
        result = number_1 / number_2
else:
    print("Error: Operación no válida.")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

year = int(input("Introduce un año: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"El año {year} es bisiesto.")
else:
    print(f"El año {year} no es bisiesto.")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)


edad = int(input("Introduce una edad: "))
if edad >= 0 and edad <= 2:
    print("Bebé")
elif edad >= 3 and edad <= 12:
    print("Niño")
elif edad >= 13 and edad <= 17:
    print("Adolescente")
elif edad >= 18 and edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")