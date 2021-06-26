class Suplicio:
    def __init__(self, listeilor):
        self.listeilor=listeilor
    
    def Ordenacion (self):
        self.listeilor.sort()
        return self.listeilor

lista= ["without","hello","bag","world"]
p1=Suplicio(lista)
print(p1.Ordenacion())
"""
without,hello,bag,world Then, the output should be: bag,hello,without,world
"""