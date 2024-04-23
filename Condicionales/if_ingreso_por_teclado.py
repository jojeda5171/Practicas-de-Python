print("Ingrese la nota del alumno: ")
notaAlumno = input()


def evaluacion(nota):
    valoracion = "Sprobado"
    if (nota < 5):
        valoracion = "Suspenso"
    return valoracion


print(evaluacion(int(notaAlumno)))
