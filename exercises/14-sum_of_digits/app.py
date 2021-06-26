#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
  return int((str(num))[0])+int((str(num))[1])+int((str(num))[2])


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))

"""
Example input 123

Example output 6
"""