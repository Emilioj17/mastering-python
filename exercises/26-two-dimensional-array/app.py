class Suplicio:
    def __init__(self, dig1, dig2):
        self.dig1=dig1
        self.dig2=dig2
    
    def Caos(self):
        list1=[]
        for xex in range(self.dig1):
            list2=[]
            for yey in range(self.dig2):
                list2.append(xex*yey)
            list1.append(list2)
        return(list1)


p1=Suplicio(7,5)
print(p1.Caos())



"""
input: 3,5 
Output: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Note: i=0,1.., X-1; j=0,1,¡­Y-1
"""