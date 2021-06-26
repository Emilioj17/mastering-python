def car_route(n,m):
  if m%n==0:
    return m/n
  else:
    return int((m/n)+1)
  return None


#Invoke the function with two intergers.
print(car_route(700,14500))

"""
Example input
700
750
Example output
2
"""