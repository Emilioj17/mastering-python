#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):
  decenas = int(digit/10)
  unidades = digit-(decenas*10)
  return (decenas, unidades)
   


#Invoke the function with any interger as its argument.
print(two_digits(81))

"""
Example input

79
Example output

(7, 9)
"""
