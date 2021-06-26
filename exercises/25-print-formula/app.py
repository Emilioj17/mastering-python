class Square:
    def __init__(self, ache):
        self.ache= ache
        self.ce = 50
        self.de = 30
        self.square = int(((2*self.ce*self.de)/self.ache)**(1/2))

"""
Q = Square root of [(2 C D)/H]

fixed values of C and H: C is 50. H is 30.

Dado H: 100,150,180

The output of the program should be: 18,22,24
"""

p1=Square(100)
p2=Square(150)
p3=Square(180)
print(p1.square)
print(p2.square)
print(p3.square)