import time
class Lista:

    def __init__(self, datos=[]):
           self.datos = []

    
    def insertar(self,dato):
        self.datos.append(dato)
        print('Se agregó un nuevo número a la lista: {}'.format(self.datos))
    
    
    def eliminar(self):
        print('Por defecto, se elimina el último número, este es: {}'.format(self.datos.pop()))
        print('Lista actualizada: {}'.format(self.datos))
    
    def mostrar(self):
        print('Aquí se muestra como está actualmente la lista: {}'.format(self.datos))
    
     
    def eliminarElemento(self,índice):
        try:
            if índice <= len(self.datos):
                self.datos.pop(índice)
                print('Lista actualizada con el elemento eliminado: {}'.format(self.datos))
                time.sleep(2)
                return True

        except ValueError:
            return False
       
        
    def InsertarElemento(self,pos,dato):
        self.datos.insert(pos,dato)
        print('Se añadió un dato a la lista : {}'.format(self.datos))

    def buscar(self,dato):
        try:
            if dato in self.datos:
                print('El dato seleccionado se encuentra en la posición: {}'.format(self.datos.index(dato)))
                time.sleep(2)
                return True

        except ValueError:
            return False
        
        
    