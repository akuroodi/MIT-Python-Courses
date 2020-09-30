# Write a quick function to calculate std. dev of the lenghts of strings in list L

def stdDevStrings(L):
    lengthSum = 0
    x = 0

    if len(L) == 0: return float("NaN")
    for word in L:
        lengthSum += len(word)
    
    meanlen = lengthSum / len(L)

    for word in L:
        x += (len(word) - meanlen)**2
    
    x /= len(L)
    x = x**0.5

    return float(x)
    
        
def stdDev(L):
    mean = sum(L) / len(L)
    sums = 0

    for l in L:
        sums += (l-mean)**2

    sums /= (len(L))

    sums = sums**0.5
    
    return float(sums)
    
  

   
L2 = [1,2,3,4]
L = ['apples', 'oranges', 'kiwis', 'pineapples']

print(stdDev(L2))