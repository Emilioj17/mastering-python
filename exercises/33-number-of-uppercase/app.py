lista="Hello world!"

class Suplicio:
    def __init__(self, listeilor):
        self.listeilor=listeilor
    
    def Ordenacion (self):
        minuscula=0
        mayuscula=0
        for x in self.listeilor:
            if x.islower():
                minuscula=minuscula+1
            elif x.isupper():
                mayuscula=mayuscula+1
            else:
                pass
        return ("UPPER CASE " + str(mayuscula) +" LOWER CASE " + str(minuscula))

p1=Suplicio(lista)
print(p1.Ordenacion())