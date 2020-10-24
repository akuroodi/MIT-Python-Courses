# Simple merge sort algorithm to measure time complexity as list grows in size


def merge(left, right):
    """
    Inputs: Two lists that are sorted in ascending order

    Output: Merged version of the two lists

    """
    result = []         
    i, j = 0,0                  # pointers to both lists
    
    while i < len(left) and j < len(right):
        # Check first elements of each list, add smaller one to result
        # Move along each list as you take the smaller element
        if (left[i] < right[j]):            
            result.append(left[i])
            i+=1
        
        else:
            result.append(right[j])
            j+=1

    # Gone through one of the lists, now append rest of remaining list to result

    while (i < len(left)):          
        result.append(left[i])
        i+=1
    
    while (j < len(right)):
        result.append(right[j])
        j+=1
    
    return result

        

def mergeSort(L):
    """
    Input: an unsorted list L of arbitrary length
    Uses the merge() function defined above

    Output: a sorted copy of L

    """

    if len(L) < 2: return L[:]      # a list of 0 or 1 elements is already sorted

    # For larger lists,  recursively divide and conquor

    mid = len(L) // 2

    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])

    return merge(left, right)


L = [2, 4, 6, 1, 3, 6, 8, 3,5, 4,56]
print("Unsorted L: " + str(L))
print (mergeSort(L))
