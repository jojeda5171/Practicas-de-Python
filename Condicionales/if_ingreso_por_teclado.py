print("Ingrese la nota del alumno: ")
notaAlumno = input()


def evaluacion(nota):
    valoracion = "aprobado"
    if (nota < 5):
        valoracion = "suspenso"
    return valoracion


print(evaluacion(int(notaAlumno)))
