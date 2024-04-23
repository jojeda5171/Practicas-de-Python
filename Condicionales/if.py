def evaluacion(nota):
    valoracion = "Aprobado"
    if (nota < 5):
        valoracion = "Suspenso"
    return valoracion


print(evaluacion(4))
