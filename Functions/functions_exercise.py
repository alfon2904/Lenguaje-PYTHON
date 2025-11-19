# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora
'''
# 1. Cuenta regresiva
def cuenta_regresiva(n):
    """Imprime una cuenta regresiva desde n hasta 0."""
    for i in range(n, -1, -1):
        print(i)
    print("¡Despegue!")

cuenta_regresiva(20)

#-----------------------------------------------
#2. tabla de multiplicar del 10
def tabla_de_10(x):
    """Imprime la tabla de multiplicar del número x del 1 al 10."""
    for n in range(1, 11):
        print(f"{n} x {x} = {n * x}")

tabla_de_10(10)
#-----------------------------------------------
#3. operación matematica
def operacion_matematica(a, b, operacion):
    if operacion == '+':
        return a + b
    elif operacion == '-':
        return a - b
    elif operacion == '*':
        return a * b
    elif operacion == '/':
        if b != 0:  
            return a / b
        else:
            return "Error: División por cero"
resultado = operacion_matematica(10, 5, '+')             
print(resultado)
#-----------------------------------------------
#4. Calcular perímetro de un cuadrado
def perimetro_cuadrado(lado):
    """Calcula el perímetro de un cuadrado dado el lado."""
    return lado * 4
perimetro = perimetro_cuadrado(5)
print(f"El perímetro del cuadrado es: {perimetro}")
#-----------------------------------------------
#5. Elevar un número a una potencia
def numero_elevado_a_potencia(numero, potencia):
    """Eleva un número a una potencia dada (por defecto al cuadrado)."""
    return numero ** potencia

resultado = numero_elevado_a_potencia(3, 2)
print(f"El resultado de elevar 3 a la potencia 2 es: {resultado}")
#-----------------------------------------------
#6. Mayor valor en una lista
def mayor_valor_de_lista(lista):
    """Devuelve el mayor valor de una lista de números."""
    if not lista:
        return None  
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor
numeros = [9, 5, 2, 8, 1]
mayor_valor = mayor_valor_de_lista(numeros)
print(f"El mayor valor de la lista es: {mayor_valor}")
#-----------------------------------------------
#7. Área de un triángulo
def area_triangulo(base, altura):
    """Calcula el área de un triángulo dada la base y la altura."""
    return (base * altura) / 2 
area = area_triangulo(4, 5)
print(f"El área del triángulo es: {area}")
#-----------------------------------------------
#8. Validar credenciales
def validar_credenciales(usuario, contraseña):
    """Valida las credenciales de un usuario."""
    if len(contraseña) < 8 or '*' not in contraseña or  usuario != "admin":
        print("Error: La contraseña debe tener al menos 8 caracteres, y contener un asterisco (*) si el usuario es admin.")
    else:
        print("Credenciales válidas.")
resultado = validar_credenciales("pocho", "pass1234*")
#-----------------------------------------------
#9. Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="Pocho", edad=25, ciudad="Madrid", profesion="Desarrollador")
#mostrar_informacion_de(nombre="Tatiana", edad=22, ciudad="Bogota", profesion="Comercial", mascota="perro")'''
#-----------------------------------------------
#10. Validar nota de un estudiante
def validar_nota(nombre: str, notas: list):
    """Valida si un estudiante ha aprobado o no según sus notas."""
    promedio = sum(notas) / len(notas)
    if promedio >= 6:
        print(f"El estudiante {nombre} ha aprobado con un promedio de {promedio:.2f}.")
    else:
        print(f"El estudiante {nombre} no ha aprobado con un promedio de {promedio:.2f}.")
validar_nota("Pocho", [7, 8, 6, 5, 9])
validar_nota("Erika", [4, 5, 3, 6, 2])