class Suplicio:
    def __init__(self, listeilor):
        self.listeilor=listeilor
    
    def Ordenacion (self):
        x = self.listeilor.split()
        x.sort()
        x = " ".join(x)
        return(x)

lista= "hello world and practice makes perfect and hello world again"
p1=Suplicio(lista)
print(p1.Ordenacion())

"""
-->hello world and practice makes perfect and hello world again 
-->again and hello makes perfect practice world
"""