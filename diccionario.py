captura=True
import time
import os
c = ("cls")
os.system(c)
diccionario ={}
while captura == True:
    try:
        dato = int(input("ingrese la cantidad de datos que ingresara en el Diccionario : "))
        if dato > 0:
            print("")
            print(f"cargaremos {dato} datos en Diccionario")
            captura = False
        else:
            print("")
            print("ingrese un valor numerico mayor a 0")
    except ValueError:
        print("")
        print("ingrese un valor numerico entero")
        time.sleep(1.6)
        os.system(c)
for x in range(dato):
    usuario = input("ingrese el nombre de usuario : ")
    diccionario[usuario] = input("ingrese la contraseña del usuario : ")
    print("")
print(diccionario)
time.sleep(1.6)
os.system(c)
print("Inicie - Seccion ")
usuario = input("ingrese el nombre de usuario : ")
if diccionario.get(usuario, 'Usuario NO existe') == 'Usuario NO existe':
    print('Usuario no existe')
while captura == False: 
    print("1-Ver diccionario")
    print("2-Ingresar dato a el diccionario")
    print("3-Salir")
    print("")

    try:
        opc = int(input("Ingrese la opcion que quiere realizar: "))
        if opc > 0:
                  print("")
        else:
            print("")
            print("ingrese una opcion valida")
    except ValueError:
        print("")
        print("ingrese un valor numerico entero")
    if opc == 1:
         print("")
         print(diccionario)
    if opc == 2:
         print("")
         usuario = input("ingrese el nombre de usuario : ")
         diccionario[usuario] = input("ingrese la contraseña del usuario : ")
    if opc == 3:
         print("")
         captura = True
         break
    else:
         print("")


