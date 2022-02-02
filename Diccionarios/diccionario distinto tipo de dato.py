diccionario = {"Alemania": "Berlin", 23: "Jordan", "Mosqueteros": 3}
print(diccionario)

tupla = ("España", "Francia", "Reino Unido", "Alemania")
diccionario2 = {tupla[0]: "Madrid", tupla[1]: "Paris",
                tupla[2]: "Londres", tupla[3]: "Berlin"}
print(diccionario2)

diccionario3 = {23: "Jordan", "Nombre": "Michael",
                "Equipo": "Chicago", "Anillos": [1991, 1992, 1993, 1996, 1997, 1998]}
print(diccionario3)

print(diccionario.keys())

print(diccionario.values())

print(len(diccionario))