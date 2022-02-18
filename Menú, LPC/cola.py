import os
import time
os.system("cls")

class Cola:
              
    def __init__(self,tamaño):
        self.lista = []
        self.tope = 0
        self.size = tamaño
     
    def empty(self):
        return self.tope == 0
    
    def push(self,dato):
        
            if  self.tope < self.size:
                self.lista += [dato]
                self.tope += 1
                print("La cola actualizada es: {}".format(self.lista))
            else:
                print('*'*10,"La cola está llena",'*'*10)
                
                
    def pop(self):
        if self.empty():
            print ('*'*10,"Lista Vacía",'*'*10)
        else:
            top = self.lista[0]                           
            self.tope -= 1                               
            self.lista = self.lista[1:]                
            print("El elemento eliminado es: {}".format(top))
            print('Cola actualizada: {}'.format(self.lista))
            
        
    def show(self):
        if self.empty():                                    
            print('*'*10,"Cola vacía",'*'*10)
        else:                                                           
            for i in range(0,self.tope):                
                print("[{}]".format(self.lista[i]))
                print() 
    
    def buscar(self,buscar):
        try:
            if buscar in self.lista:
                print('El dato seleccionado se encuentra en la posición: {}'.format(self.lista.index(buscar)))
                time.sleep(2)
                return True

        except ValueError:
            return False
        
  
   
    def longitud(self):
        print('La longitud de la cola es: {}'.format(self.tope))
