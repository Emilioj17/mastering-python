#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  decenas = int(num/10)
  unidades = num-(decenas*10)
  return (str(unidades) + str(decenas))
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(85))

