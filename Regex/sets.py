import re

# [:] Coincide con cualquier caracter dentro de los corchetes
"""
username = "rub.$ius_69+"
pattern = r"^[\w._$%+-]+$"

match = re.search(pattern, username)
if match:
  print("El nombre de usuario es válido: ", match.group())
else:
  print("El nombre de usuario no es válido")

# Buscar todas las vocales de una palabra
text = "Hola mundo de"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches)

# Una Regex para encontrar las palabras man, fan y ban
# pero ignora el resto
text = "man ran fan ñan ban"
pattern = r"[mfb]an"

matches = re.findall(pattern, text)
print(matches)


# Ejercicio:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
text = "omniman fanatico man bandana"
pattern = r"\b[mfb]an"
matches = re.findall(pattern, text)
print(matches)
# \b 

text = "22"
pattern = r"[4-9]"

matches = re.findall(pattern, text)
print(matches)
"""

# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
#email_1 = "lo.que+sea$@shopping.online."
email_2 = "michael@gov.co.uk"
pattern = r"\b[\w._%$+-]+@[\w.-]+\.[a-zA-Z]{2,}$"
match = re.findall(pattern, email_2)
if match:
  print("Email válido: ", match)
else:
  print("Email no válido")
# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
print("-----------------------------------")
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)