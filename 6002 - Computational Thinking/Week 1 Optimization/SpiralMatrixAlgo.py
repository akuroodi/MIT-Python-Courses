import random
width, height = 4,4

room = [[random.randint(0,5) for i in range(width)] for j in range(height)] 


for row in range(height):
    print(room[row])

print()



def spiralRoom2(room):
    """ 
    Given an m x n matrix, outputs the elements in a spiral fashion

    Uses fact that in Python the "room" matrix is composed of list of lists
    
    Traverses the outer boundary of the matrix while peeling those numbers away

    Continues until no items remain

    """
    
    result = []

    while (True):
        # If the matrix is empty or only contains an empty list we're done
        if not room or not room[0]: break
        
        # If it has just one item remaining, tack it on to the result
        if len(room) == 1:
            result += room[0]
            break
        
        # Grab the first (top) row and last (bottom) row
        
        result += room[0]
        lastRow = room[-1]      # save this to add later
        firstcol = []

        # Step through each "row" excluding first and last
        # First adds the "rightmost" column (while popping it off)
        # Then stores/pops "leftmost" column as firstcol 
        for row in room[1:-1]:          
            result.append(row.pop())
            if len(row) != 0:               # If matrix has only 1 column, your row is empty by this stage
                firstcol.append(row.pop(0))

        # Trim your matrix by peeling off the first and last rows
        room.pop(0)
        room.pop()

        # Add in the bottom row and left column (in reverse order of course)
        result += lastRow[::-1]

        result += firstcol[::-1]

    return result

print(spiralRoom2(room))