# intentalo ma;ana desde aqui 

from ast import Try

print("Menu de Opciones")
print(" selecione un numero del 1 al  4 para elejir su opcion")
print("1 Sumar")
print("2 Restar")
print("3 Multi")
print("4 dividir")
print("5 Salir")

seleccion = int(input("seleciones su opcion"))

while True:
        try:
            
            if seleccion == 1:
                print("se sumaran 2 numeros enteros")
                a = int(input("Ingresael 1#"))
                b = int(input("Ingresael 2#"))
                suma = a+b
                print("su valortiotal es:" + str(suma))
                break
            elif seleccion == 2:
                print("Se restaran 2 numeros ")
                a = int(input("Ingresael 1#"))
                b = int(input("Ingresael 2#"))
                print(a-b)
                break
            elif seleccion == 3 :
                print("Se multiplicaran 2 numeros")
                a = int(input("Ingresael 1#"))
                b = int(input("Ingresael 2#"))
                print(a*b)
                break
            elif seleccion == 4 :
                    print("divicion")
                    a = int(input("Ingresael 1#"))
                    b = int(input("Ingresael 2#"))
                    print(a/b)
                    break
            elif seleccion == 5 :
                    print("Saliendo.....")
                    break
        except ValueError:
                    print("Invalido ingresa un valor numerico")

           