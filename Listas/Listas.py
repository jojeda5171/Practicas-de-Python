print("Ejemplo de listas")
nombres=["José", "Luis", "Ojeda", "Carrasco"]
print (nombres)
print (nombres[1])
print (nombres[0:3])
nombres.append("Denis")
print(nombres)
nombres.insert(0,"Jadira")
print(nombres)
nombres.extend(["Jimenez", "Viteri"])
print(nombres)
print(nombres.index("José"))
print("elemento" in nombres)
nombres.remove("José")
print(nombres)
nombres.pop()
print(nombres)

apellidos=["Reinoso", "Sanchez"]
nombresCompletos=nombres+apellidos
print(nombresCompletos)