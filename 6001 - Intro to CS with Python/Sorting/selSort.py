# Simple selection sort algorithm to measure time complexity as list grows in size

def selSort(L):
    """
    Input: an unsorted list L of arbitrary length

    Output: a sorted copy of L

    """

    for i in range(len(L)-1):
        j = i+1                 # pointer to the next element
        while (j < len(L)):     # For each i, walk down rest of L and replace if jth is smaller
            if (L[i] > L[j]):
                L[i], L[j] = L[j], L[i]
            j+=1




L = [2, 4, 6, 1, 3, 6, 8, 3,5, 4,56]

print("Unsorted L: " + str(L))
selSort(L)
print("Sorted L: " + str(L))