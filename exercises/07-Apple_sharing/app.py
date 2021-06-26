def apple_sharing(n,k):
  tomadas=0
  resto=0
  if k>0:
    resto=k%n
    tomadas=int(((k-resto)/n))
  return (tomadas, resto)
 
    

print(apple_sharing(6,50))

"""
Example input

(6, 50)
Example output

(8, 2)
"""