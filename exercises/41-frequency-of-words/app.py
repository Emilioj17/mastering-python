lista="New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"

class Suplicio:
    def __init__(self, listeilor):
        self.listeilor=listeilor
    
    def Ordenacion (self):
        diccionario={}
        self.listeilor=self.listeilor.split()
        newList=self.listeilor
        newList=list(dict.fromkeys(newList))
        newList.sort()
        for x in newList:
            diccionario[x]=self.listeilor.count(x)

        return diccionario      

p1=Suplicio(lista)
print(p1.Ordenacion())

"""
output should be: 2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1

"""