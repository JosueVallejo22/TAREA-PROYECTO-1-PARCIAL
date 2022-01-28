# import os
# os.system("cls")
class Helper:
    def __init__(self):
        pass
    def menu(self,opciones,titulo):
        print(titulo)
        for opcion in opciones:
            print(opcion)
        opc = input("Elija una opcion del (1 al {}): ".format(len(opciones)))
        return opc