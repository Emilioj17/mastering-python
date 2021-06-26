class Suplicio:
    def __init__(self, stringl):
        self.stringl = stringl
    
    def getString(self):
        pass
        # self.stringl= input("Ingresa Nombre: \n")

    def printString(self):
        print("El String ingresado es: " + self.stringl)

emp_1=Suplicio(input("Ingresa Nombre:\n"))

emp_1.printString()




"""
Define a class which has at least two methods: 
getString: to get a string from console input 
printString: to print the string in upper case. 
Also please include simple test function to test the class methods.
"""