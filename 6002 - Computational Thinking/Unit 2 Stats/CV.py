# Write a quick function to calculate coefficent of variance for a list L

def CV(L):
    mean = sum(L) / len(L)
    sums = 0

    for l in L:
        sums += (l-mean)**2
    
    sums /= (len(L))

    sums = sums**0.5

    sums /= mean

    return float(sums)

    
L = [10, 4, 12, 15, 20, 5]


print(CV(L))





