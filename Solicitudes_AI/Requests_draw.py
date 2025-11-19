def procesar_sistema(data):
  # 1) Eliminar usuarios inactivos (excepto admins)
  data['users'] = {
    user: info
    for user, info in data['users'].items()
      if info['activo'] or info['rol'] == 'admin'
  }
 
  # 2) Actualizar rol de usuarios específicos
  if 'Carlos' in data['users']:
    data['users']['Carlos'].update({'rol': 'user'})
 
  # 3) Añadir nueva configuración
  data['config'].setdefault('version', '2.0')
 
  return data
 
sistema = {
  'users': {
    'Ana': {
      'rol': 'admin',
      'activo': False
    },
    'Carlos': {
      'rol': 'guest',
      'activo': True
    },
    'Luisa': {
      'rol': 'user',
      'activo': False
    }
  },
  'config': {
    'debug': True
  }
}
 
resultado = procesar_sistema(sistema)
print(resultado)

"""
import requests
 
url = 'https://jsonplaceholder.typicode.com/posts/'
query_params = {
   'title': "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
}
 
response = requests.get(url, params=query_params)
data = response.json()
print(data)"""