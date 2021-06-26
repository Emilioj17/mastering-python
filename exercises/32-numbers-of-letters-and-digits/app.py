lista="hello world! 123"

class Suplicio:
    def __init__(self, listeilor):
        self.listeilor=listeilor
    
    def Ordenacion (self):
        letras=0
        numeros=0
        espacios_vacios=0
        for x in self.listeilor:
            if x.isdigit():
                numeros=numeros+1
                # print("Hola")
            elif x.isspace():
                espacios_vacios=espacios_vacios+1
            else:
                letras=letras+1
        return ("LETTERS " + str(letras) +" DIGITS " + str(numeros) + " ESPACIOS VACIOS " + str(espacios_vacios))

p1=Suplicio(lista)
print(p1.Ordenacion())