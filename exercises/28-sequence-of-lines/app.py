class Suplicio:
    def __init__(self, listeilor):
        self.listeilor=listeilor
    
    def Ordenacion (self):
        x = self.listeilor.upper()
        return(x)

lista= "Hello world Practice makes perfect"
p1=Suplicio(lista)
print(p1.Ordenacion())
"""
input: Hello world Practice makes perfect
Output: Same shit, but UPPERCASE
"""