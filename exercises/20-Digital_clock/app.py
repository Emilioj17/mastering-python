#Complete the function to return how many hrs and min are displayed on the 24th digital clock.
def digital_clock(n):
  horas=int(n/60)
  minutos= n-horas*60
  return (horas, minutos)

#Invoke the function with any interger (seconds after midnight)
print(digital_clock(150))

"""Example input 150
Example output (2, 30)"""
