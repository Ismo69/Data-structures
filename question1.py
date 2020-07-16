
n=10

def DotProduct(ListA, ListB): 
  
    product = 0
  
    # Loop for calculate dot product 
    for i in range(0, n): 
        product = product + ListA[i] * ListB[i] 
  
    return product

    print("Dot product:", end =" ") 
    print(dotProduct(ListA, ListB))


    if __name__=='__main__': 
    ListA = [1, 2, 9] 
    ListB = [3, 8, 4] 
  
