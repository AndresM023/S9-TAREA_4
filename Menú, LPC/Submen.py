class SubMenu:
    def __init__(self):
        pass
    
    def menu(self, opciones, título):
        print("*"*10,título,"*"*10)
        for i in opciones:
            print(i)
        alt = input("Elija una opción[1...{}]: ".format(len(opciones)))
        return alt

    