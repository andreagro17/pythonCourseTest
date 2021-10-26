import json

persona = '{"nombre": "Andrea", "lenguajes": ["Python", "js"]}'
print(persona)

persona_dic = json.loads(persona)
print(persona_dic['lenguajes'])

persona_json = json.dumps(persona_dic)
print(persona_json)

# Leer un fichero json
with open('ejemplo_json.json') as fichero:
  # loads (decode) toma un string como input y devuelve un diccionario
  datos = json.loads(fichero.read())
print(datos)

with open('ejempl2_json.txt', 'w') as json_fichero:
  json.dump(datos, json_fichero)