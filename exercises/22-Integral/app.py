def suplicio(numbero):
    retorno={}
    for x in range(1,numbero+1):
        retorno[x]= x*x
    return retorno

print(suplicio(8))
"""
8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""