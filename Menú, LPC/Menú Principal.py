import os
import time
from Submen import SubMenu
from lista import Lista
from pila import Stack
from cola import Cola


sub = SubMenu()
lista1 = Lista()
lista = ["1).Lista ","2).Pila","3).Cola","4).Salir"]
alternativa = ""  
while alternativa != "4":
    os.system("cls")
    alternativa = sub.menu(lista,"Menú Principal")
    if alternativa == "1":
        alternativa1 = ""
        while alternativa1 != "7":
            os.system("cls")
            alternativa1 = sub.menu(["1).Push","2).Pop","3).Show","4).Eliminar","5).Insertar","6).Buscar","7).Salir"],"Menú de Lista")
            os.system("cls")
            if alternativa1 == "1":
                dato = input("Ingrese datos a la lista: ")
                lista1.insertar(dato)
                time.sleep(1)
         
            elif alternativa1 == "2":
                lista1.eliminar()
                time.sleep(2)
                    
            elif alternativa1 == "3":
                lista1.mostrar()
                time.sleep(2)
                    
            elif alternativa1 == "4":
                while True:
                    índice = int(input("Ingrese una posición que se quiere eliminar: "))
                    os.system("cls")
                    valor = lista1.eliminarElemento(índice)
                    if valor == True:
                        break
                    else:
                        print('*'*10,'Índice fuera de los límites','*'*10) 
                        time.sleep(1.5)
                        os.system("cls")
                                
            elif alternativa1 == "5":
                pos = int(input("Ingrese una posición: "))
                dato = input("Ingrese un dato: ")
                lista1.InsertarElemento(pos,dato)
                time.sleep(1.5)
         
            elif alternativa1 == "6": 
                while True:
                    datos = input("Ingrese un dato que se encuentre en la lista: ")
                    os.system("cls")
                    valor = lista1.buscar(datos)
                    if valor == True:
                        break
                    else:
                        print('*'*10,'Este dato no se encuentra en la lista','*'*10) 
                        time.sleep(1.5)
                        os.system("cls")
                    
             
            elif alternativa1 == "7":
                print('*'*10,"Saliendo del menú...",'*'*10)
                time.sleep(1.5)



    if alternativa == "2":
        alternativa1 = ""
        os.system("cls")
        tamaño = int(input("Ingresar un tamaño a la pila: "))
        pila = Stack(tamaño)
        while alternativa1 != "6":
            os.system("cls")
            alternativa1 = sub.menu(["1).Push","2).Pop","3).Show","4).Buscar","5).Longitud","6).Salir"],"Menú de Pila")
            os.system("cls")
            if alternativa1 == "1":
                dato = input("Ingrese un dato: ")
                pila.push(dato)
                time.sleep(1.5)

            elif alternativa1 == "2":
                pila.pop()
                time.sleep(1.5)

            elif alternativa1 == "3":
                pila.show()
                time.sleep(1.5)

            elif alternativa1 == "4":
                while True:
                    buscar = input("Ingrese un dato de la pila para determinar su posición: ")
                    os.system("cls")
                    valor = pila.buscar(buscar)
                    if valor == True:
                        break
                    else:
                        print('*'*10,'Este dato no existe en la pila','*'*10) 
                        time.sleep(1.5)
                        os.system("cls")
                
            elif alternativa1 == "5":
                pila.longitud()
                time.sleep(1.5)

            elif alternativa1 == "6":
                print('*'*10,"Saliendo del menú...",'*'*10)
                time.sleep(1.5)



    if alternativa == "3":
        alternativa1 = ""
        os.system("cls")
        tamaño = int(input("Ingresar un tamaño a la cola: "))
        cola = Cola(tamaño)
        while alternativa1 != "6":
            os.system("cls")
            alternativa1 = sub.menu(["1).Push","2).Pop","3).Show","4).Buscar","5).Longitud","6).Salir"],"Menú de Cola")
            os.system("cls")
            if alternativa1 == "1":
                dato = input("Ingrese un dato: ")
                cola.push(dato)
                time.sleep(1.5)

            elif alternativa1 == "2":
                cola.pop()
                time.sleep(1.5)

            elif alternativa1 == "3":
                cola.show()
                time.sleep(1.5)

            elif alternativa1 == "4":
                while True:
                    buscar = input("Ingrese un dato de la cola para determinar su posición: ")
                    os.system("cls")
                    valor = cola.buscar(buscar)
                    if valor == True:
                        break
                    else:
                        print('*'*10,'Este dato no existe en la cola','*'*10) 
                        time.sleep(1.5)
                        os.system("cls")
                

            elif alternativa1 == "5":
                cola.longitud()
                time.sleep(1.5)

            elif alternativa1 == "6":
                print('*'*10,"Saliendo del menú...",'*'*10)
                time.sleep(1.5)


os.system("cls")
print("Gracias por su atención.")
time.sleep(5)
