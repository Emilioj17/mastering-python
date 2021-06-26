#Complete the function to return the first digit to the right of the decimal point.
def first_digit(num):
  num2=str(num)
  posicion= 0
  for x,y in enumerate(num2):
    if y == ".":
      posicion=x
  return num2[posicion+1]


#Invoke the function with a positive real number. ex. 34.33
print(first_digit(6.24))

"""
Example input 1.79

Example output 7
"""