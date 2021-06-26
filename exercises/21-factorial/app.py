# Your code here
def factorial(numbero):
    numbero=numbero
    numero=1
    for x in range(1,numbero):
        numero=numero*numbero
        numbero=numbero-1
    return numero

print(factorial(6))

"""
8
Then, the output should be:

40320
"""