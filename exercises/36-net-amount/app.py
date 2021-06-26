lista="D 300 D 300 W 200 D 100"

class Suplicio:
    def __init__(self, listeilor):
        self.listeilor=listeilor
    
    def Ordenacion (self):
        final=0
        yey=self.listeilor.split()
        for x,i in enumerate(yey):
            if i=="D":
                final=final+int(yey[x+1])
            elif i=="W":
                final=final-int(yey[x+1])
            else:
                pass
        return(final)


p1=Suplicio(lista)
print(p1.Ordenacion())

"""
D:DEposito, W:Sacar
-->D 300 D 300 W 200 D 100
--> 500
"""