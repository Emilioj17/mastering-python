lista=[1,2,3,4,5,6,7,8,9]

class Suplicio:
    def __init__(self, listeilor):
        self.listeilor=listeilor
    
    def Ordenacion (self):
        newList = [x for x in self.listeilor if x%2!=0]
        return(newList)

p1=Suplicio(lista)
print(p1.Ordenacion())

"""
Use a list comprehension to square each odd number in a list
1,2,3,4,5,6,7,8,9 Then, the output should be: 1,3,5,7,9
"""