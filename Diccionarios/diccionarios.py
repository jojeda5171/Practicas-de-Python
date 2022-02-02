diccionario = {"Alemania": "Berlin", "Francia": "Paris",
               "Reino Unido": "Londres", "España": "Madrid"}
diccionario["Italia"] = "Lisboa"
print(diccionario["Alemania"])
print(diccionario)
diccionario["Italia"] = "Roma"
print(diccionario)
del diccionario["Reino Unido"]
print(diccionario)
