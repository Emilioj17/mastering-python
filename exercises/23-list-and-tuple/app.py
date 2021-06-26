numeros= [34,67,55,33,12,98]
def suplicio(numeros):
    newLista=[]
    for x in numeros:
        newLista.append(str(x))

    return newLista

print(suplicio(numeros))



"""
34,67,55,33,12,98
output: '34', '67', '55', '33', '12', '98'
"""