# Cómo hacer peticiones a APIs con Python
# con y sin dependencias

# 1. Sin dependencias (díficil y sin dependencias)
import urllib.request
import json

from os import system
if system("clear") != 0: system("cls")

"""
api_posts = "https://jsonplaceholder.typicode.com/posts/"

try:
  response = urllib.request.urlopen(api_posts)
  data = response.read()
  json_data = json.loads(data.decode('utf-8'))
  print(json_data[0])
  response.close()
except urllib.error.URLError as e:
  print(f"Error en la solicitud: {e}")



import requests

# 2. Con dependencia (requests)
print("\nGET:")
api_posts = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(api_posts)
response_json = response.json()
print(response_json[0]['title'])

# 3. Un POST
print("\nPOST:")
try:
  response_2 = requests.post(
    "https://jsonplaceholder.typicode.com/posts/",
    json={
      "title": "foo",
      "body": "bar",
      "userId": 1
    })
  print(response.status_code)
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")
"""
import requests
# 4. Un PUT
print("\nPUT:")
try:
  response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={
      "title": "foo",
      "body": "bar",
      "userId": 1,
    })
  data = response.json()
  print(data)
  print(response.status_code)
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")


#PATCH
print("\nPATCH:")
try:
  response = requests.patch(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={
      "title": "foo patched",
    })
  data = response.json()
  print(data)
  print(response.status_code)
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")

## Metodo HTTP query
print("\nHTTP QUERY:")
url = "https://jsonplaceholder.typicode.com/posts/"
query_params = {"id": 1}
response = requests.get(url, params=query_params)
data = response.json()
print(data)

"""
# Usar la API de GPT-4o de OpenAI
# Ref: https://platform.openai.com/docs/api-reference/making-requests

import requests
OPENAI_KEY = "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"

import json

def call_openai_gpt(api_key, prompt):
  url = "https://api.openai.com/v1/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  return response.json()

api_response = call_openai_gpt(OPENAI_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response)

# Llamar a la API de DEEPSEEK

import json

def call_deepseek(api_key, prompt):
  url = "https://api.deepseek.com/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  print(response.json())
  return response.json()

api_response = call_deepseek(DEEPSEEK_API_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])"""
