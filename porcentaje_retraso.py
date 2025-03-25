#Hecho por Brayan David Ladino Rodriguez 
print("Bienvenido al programa")

dias_asignados = int(input("Ingrese los dias asigandos para el desarrollo de las tareas: "))
dias_retraso = int(input("Ingrese los dias de retraso: "))

if dias_asignados > 0 and dias_retraso > 0:
        porcentej_retraso = (dias_retraso/dias_asignados) * 100
        print (f"El porcentaje de retraso es de: {porcentej_retraso}%")
else:
        print("Error: Los dias asignados deben ser mayores que el 0")
        print("Volver a intentarlo")

