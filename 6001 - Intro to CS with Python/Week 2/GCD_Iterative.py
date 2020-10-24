def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if (a== 0): return b
    if (b == 0): return a

    return gcdRecur(b,a%b)
    
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    x = min (a,b)

    while (x>0):
        if (x == 1): return x

        if (a%x == 0 and b%x == 0):
            return x
        
        x -= 1
     
          
 

print (gcdIter(72,228))