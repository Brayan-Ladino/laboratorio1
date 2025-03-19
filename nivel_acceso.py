import datetime

print("Bienvenido al programa")
#Datos de los trabajadores 
usuario1 = "Brandon", 
nivel1 = 1
trabajadorN1_contraseña = 123, 
fecha_cambio1 = datetime.datetime(2025, 2, 15)
targeta1 = True

usuario2 = "Andres"
nivel2 = 2
trabajadorN2_contraseña = 1234
fecha_cambio2 = datetime.datetime(2025, 1, 15)
targeta2 = False

usuario3 = "Adrian"
nivel3 = 3
trabajadorN3_contraseña = 12345 
fecha_cambio3=datetime.datetime(2025, 2, 25)
targeta3 = True

usuario4 = "Diego"
nivel4 = 4
trabajadorN4_contraseña = 123456
fecha_cambio4=datetime.datetime(2025, 2, 19)
targeta4 = True

usuario5 = "Samuel"
nivel5 = 5
trabajadorN5_contraseña = 1234567
fecha_cambio5=datetime.datetime(2025, 2, 10)
targeta5 = True


#Datos asignados de los trabajadores
while True:
        usuario = input("Ingrese su nombre de Usuario: ")
        contraseña = int(input("Ingrese su contraseña: "))

#Revision de datos
        #Inisiar variables por defecto

        if contraseña == trabajadorN1_contraseña and usuario1 == usuario: 
                nivel_acceso = nivel1
                fecha_cambio=fecha_cambio1
                targeta_activada = targeta1
        elif contraseña == trabajadorN2_contraseña and usuario == usuario2: 
                nivel_acceso = nivel2
                fecha_cambio = fecha_cambio2
                targeta_activada = targeta2
        elif contraseña == trabajadorN3_contraseña and usuario == usuario3: 
                nivel_acceso = nivel3
                fecha_cambio=fecha_cambio3
                targeta_activada=targeta3
        elif contraseña == trabajadorN4_contraseña and usuario == usuario4: 
                nivel_acceso = nivel4
                fecha_camnio = fecha_cambio4
                targeta_activada = targeta4
        elif contraseña == trabajadorN5_contraseña and usuario == usuario5: 
                nivel_acceso = nivel5
                fecha_cambio = fecha_cambio5
                targeta_activada = targeta5
        else:
                print("Contraseña o usurio incorreto. Aceso denegados")
                
        #Verificar si han pasado 30 dias sin cambiar la contraseña
        dias_transcurridos = (datetime.datetime.today() - fecha_cambio).days
        if dias_transcurridos >= 30:
                print("Han pasado mas de 30 dias desde el último cambio de contraseña. ")
                print("Por favor, actualícela")
                nueva_contraseña = int(input("Ingrese nueva contraseña: "))
                print("Contraseña actualizada correctamente.")
        #Verificar acceso
        if targeta_activada:
                print(f"Bienvenido {usuario} tiene acceso a nivel: {nivel_acceso} ")
                if nivel_acceso == 1:
                        print("Acceso a: Almacenamiento, matenimiento y area de vitantes")
                if nivel_acceso == 2:
                        print ("Acceso a: Seguidad y area de empleados")
                if nivel_acceso == 3:
                        print ("Acceso a: Area de administrativos y jefes")
                if nivel_acceso == 4:
                        print ("Aceso a: Directores y gerentes")
                if nivel_acceso == 5:
                        print("Aceso a todas las areas de las empresa")
        else:
                print("Acesso denegado: Su targeta no esta activida")
