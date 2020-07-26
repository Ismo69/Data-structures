import random
import numpy  
  

A = [] 
B = [] 


def DotProduct(N, ListA, ListB): 
  
    
  
    # Loop for calculating dot product 
    for i in range(N):  
        first = random.randint(1, 1000)  
        ListA.append(first)  
    for j in range(N):  
        second = random.randint(1, 1000)  
        ListB.append(second)  


    value = numpy.dot(ListA, ListB)  

    
    print("List A:", ListA)
    print("List B:", ListB)
    print("The size of the array is:", N)
    print("Dot Product:", result)  


DotProduct(, A, B)  
DotProduct(, A, B)
