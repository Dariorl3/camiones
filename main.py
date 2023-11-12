import os

opc = 0
contar = 1
resp = "S"
contra = ""
rs = ""
cargo = ""
pas1 = ""
cod1 = ""
pas2 = ""
cod2 = ""
ndeorden = 0
fecha = ""
kilometrajerecorrido = 0
petroleoconsumido = 0
horadeinicoruta = ""
horadetermineruta = ""

cod1 = 'sup1'
pas1 = 'hola'
cod2 = 'op1'
pas2 = 'chao'

while resp.lower() == "s" and contar < 3:
    os.system('clear' if os.name == 'posix' else 'cls')  # Limpiar Pantalla

    print("Menú principal")
    print("Sistema ingreso información con clave")
    print("A continuación podrá ver información de supervisor o bien ingresar datos de operador")
    print("Ingrese Opción 1 para supervisor o 2 para operario")
    opc = int(input())

    if opc == 1:
        print('Ingrese código')
        cargo = input()
        if cargo == cod1:
            print('Usted es supervisor')
            print('Ingrese contraseña')
            contra = input()
            if contra == pas1:
                print('Supervisor válido')
                print('Ver total kilometraje registrado (última semana):', kilometrajerecorrido * 7)
                print('Ver total petróleo consumido (última semana):', petroleoconsumido * 7)
                print('Ver promedio hora de inicio (última semana):', "07:49")
                print('Ver promedio hora de término (última semana):', "08:00")
                print('Desea ver información de operario S/N')
                rs = input()
                if rs.lower() == 's':
                    print('Ingrese código operario')
                    cargo = input()
                    if cargo == cod2:
                        print('Operario válido')
                        print('Ingrese número de orden')
                        ndeorden = int(input())
                        print('Ingrese fecha')
                        fecha = input()
                        print('Ingrese kilometraje recorrido')
                        kilometrajerecorrido = int(input())
                        print('Ingrese petróleo consumido')
                        petroleoconsumido = int(input())
                        print('Ingrese hora de inicio de ruta')
                        horadeinicoruta = input()
                        print('Ingrese hora de término de ruta')
                        horadetermineruta = input()
                    else:
                        print('Operario no existe')
            else:
                print("Contraseña incorrecta")
        else:
            print("Código de supervisor incorrecto")
    elif opc == 2:
        print('Ingrese código')
        cargo = input()
        if cargo == cod2:
            print('Usted es operario')
            print('Ingrese contraseña')
            contra = input()
            if contra == pas2:
                print('Operario válido')
                print('Ingrese número de orden')
                ndeorden = int(input())
                print('Ingrese fecha')
                fecha = input()
                print('Ingrese kilometraje recorrido')
                kilometrajerecorrido = int(input())
                print('Ingrese petróleo consumido')
                petroleoconsumido = int(input())
                print('Ingrese hora de inicio de ruta')
                horadeinicoruta = input()
                print('Ingrese hora de término de ruta')
                horadetermineruta = input()
            else:
                print("Contraseña incorrecta")
        else:
            print("Código de operario incorrecto")
    else:
        print("Seleccione una opción válida")

    print("Desea continuar S/N")
    resp = input()
    contar += 1