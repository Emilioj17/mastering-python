lister="Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85"

def orden(lista):
    lista=lista.split()
    lista.sort()
    lista= [(x,) for x in lista]
    return(lista)

print(orden(lister))


"""
1: Sort based on name; 
2: Then sort based on age; 
3: Then sort by score. 

The priority is that name > age > score.

--> Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85
--> [('John', '20', '90'),('Jony', '17', '91'),('Jony', '17', '93'),
('Json', '21', '85'),('Tom', '19', '80')]

"""