# 1. Introducción a las Clases en Python
# Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase.
# Nos permite agrupar datos (atributos o propiedades) y funciones (métodos) en un solo lugar.

from os import system
if system("clear") != 0: system("cls")

OPENAI_KEY = ""
DEEPSEEK_API_KEY = ""
"""
# Ejemplo básico de una clase
class Coche:
  # atributo de clase (comparte todas las instancias)
  tipo = "vehículo de cuatro ruedas"
  ruedas = 4

  # método especial que es el que construye el objeto
  # se llama automáticamente este método cuando creas la instancia
  def __init__(self, marca, modelo, color):
    # atributos de la instancia
    self.marca = marca
    self.modelo = modelo
    self.color = color

  def arrancar(self):
    print(f"El coche {self.marca} marca {self.modelo} arrancó! 🚗")


mi_coche = Coche("Toyota", "Corolla", "rojo")
mi_coche.arrancar()

print(mi_coche.marca)

coche_de_pheralb = Coche("Ford", "Fiesta", "azul")
coche_de_pheralb.arrancar()

print(coche_de_pheralb.marca)


#Otro ejemplo de clase
class Persona_intro:
  def __init__(self, nombre, edad, profesion, escuela):
    self.nombre = nombre
    self.edad = edad
    self.profesion = profesion
    self.escuela = escuela

  def saludar(self):
    print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion} graduado de {self.escuela}.")
persona1 = Persona_intro("Ana", 30, "ingeniera", "Universidad de Columbia")
persona1.saludar()
persona2 = Persona_intro("Luis", 25, "médico", "Universidad de Harvard")
persona2.saludar()
print(persona1.escuela)
print(persona2.escuela)"""

#Tercer ejemplo: algoritmo calcular área de figuras geométricas

class Area_figuras:
  def __init__(self, base=0, altura=0, radio=0):
    self.base = base
    self.altura = altura
    self.radio = radio
  def area_rectangulo(self):
    print(f"El area del rectángulo es {self.base} * {self.altura}")
  def area_circulo(self):
    print(f"El area del círculo es {3.1416 * (self.radio ** 2)}") #** es potencia
  def area_triangulo(self):
    print(f"El area del triángulo es {(self.base * self.altura) / 2}")
  def area_cuadrado(self):
    print(f"El area del cuadrado es {self.base ** 2}") #** es potencia

cuadrado1 = Area_figuras(4, 0)
cuadrado1.area_cuadrado()
triangulo1 = Area_figuras(4, 5)
triangulo1.area_triangulo()
"""
# Encapsulación: es ocultar los detalles internos de una clase y exponer solo la interfaz pública

# Crear una clase para llamar a la AI de OpenAI, DeepSeek O LO QUE SEA

import requests

class AI_API:
  def __init__(self, api_key, url, model):
    self.api_key = api_key
    self.url = url
    self.model = model

  def call(self, prompt):
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {self.api_key}"
    }
    data = {
      "model": self.model,
      "messages": [{"role": "user", "content": prompt}]
    }

    try:
      response = requests.post(self.url, json=data, headers=headers)
      res_json = response.json()
      print(res_json["choices"][0]["message"]["content"])
    except requests.exceptions.RequestException as e:
      print(f"Error en la solicitud: {e}")
      return None

print("\nOPEN_AI:")
openai_api = AI_API(OPENAI_KEY, "https://api.openai.com/v1/chat/completions", "gpt-4o-mini")

openai_api.call("Escribe un breve poema sobre la programación")

#print("\nDEEPSEEK:")
#deepseek_api = AI_API(DEEPSEEK_API_KEY, "https://api.deepseek.com/chat/completions", "deepseek-chat")

#deepseek_api.call("Escribe un breve poema sobre la programación")"""
