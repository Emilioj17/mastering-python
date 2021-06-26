class Suplicio:
    def __init__(self, margen1, margen2):
        self.margen1=margen1
        self.margen2=margen2
    
    def Ordenacion (self):
        listaVacia=[]        
        for x in range(self.margen1, self.margen2+1):
            york=str(x)
            acumulador=0
            for yey in york:
                yey=int(yey)
                if yey==0:
                    pass
                elif yey%2==0:
                    acumulador=acumulador+1
                    acumulador=0
                else:
                    acumulador=acumulador+1
            if acumulador>3:
                listaVacia.append(x)
        return(listaVacia)

p1=Suplicio(1000,3000)
print(p1.Ordenacion())

"""
 find all such numbers between 1000 and 3000 (both included) 
 such that each digit of the number is an even number. 

 numbers obtained should be printed in a comma-separated sequence on a single line.

"""