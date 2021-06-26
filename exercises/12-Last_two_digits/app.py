#Complete the function to print the last two digits of an interger greater than 9. 
def last_two_digits(num):
    if num>9:
        num2=str(num)
    return (str(num2[len(num2)-2])+str(num2[len(num2)-1]))

#Invoke the function with any interger greater than 9.
print(last_two_digits(30))

"""
Example input 1234

Example output 34
"""