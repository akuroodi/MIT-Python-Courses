# Simple bubble sort algorithm to measure time complexity as list grows in size

# Note the Python shorthand code for swapping variables

def bubbleSort (L):
    """
    Input: an unsorted list L of arbitrary length

    Output: a sorted copy of L

    """
    done = False
    while (not done):
        done = True                      # if you traverse L w/o any swaps, sorting is done
        for i in range(len(L)-1):
            if (L[i] > L[i+1]):
                done = False
                L[i], L[i+1] = L[i+1], L[i]     # shorthand swap two elements
        
    return L[:]

L = [2, 4, 6, 1, 3, 6, 8, 3,5, 4,56]
print("Unsorted L: " + str(L))
bubbleSort(L)
print("Sorted L: " + str(L))
