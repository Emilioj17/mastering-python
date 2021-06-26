lista=["0100","0011","1010","1001"]

class Suplicio:
    def __init__(self, listeilor):
        self.listeilor=listeilor
    
    def Ordenacion (self):
        listaVacia=[]
        listaVacia = list(map(lambda x: int(x, 2), self.listeilor))
        for x,i in enumerate(listaVacia):
            if i%5==0:
                return(self.listeilor[x])

p1=Suplicio(lista)
print(p1.Ordenacion())



"""
Example: 0100,0011,1010,1001 Then the output should be: 1010
check whether they are divisible by 5 or not

print(int('11111111', 2))
print(int('0100', 2))
print(int('1010', 2))


"""