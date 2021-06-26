lista="UP 5 DOWN 3 LEFT 3 RIGHT 2"
class Suplicio:
    def __init__(self, listeilor):
        self.listeilor=listeilor
    
    def Ordenacion (self):
        dX=0
        dY=0
        self.listeilor=self.listeilor.split()
        for x,y in enumerate(self.listeilor):
            if y == "UP":
                dY=dY+int(self.listeilor[x+1])
            elif y =="DOWN":
                dY=dY-int(self.listeilor[x+1])
            elif y =="LEFT":
                dX=dX-int(self.listeilor[x+1])
            elif y=="RIGHT":
                dX=dX+int(self.listeilor[x+1])
            else:
                pass
        distancia=(((dX)**(2))+((dY)**(2)))**(1/2)

        return(int(distancia))


p1=Suplicio(lista)
print(p1.Ordenacion())