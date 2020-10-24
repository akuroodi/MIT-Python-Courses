def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if (len(aStr) == 0):
        return False
   
    index = len(aStr) // 2
    guess = aStr[index-1]

    if (len(aStr) == 1):
        return guess == char

    if (guess == char):
        return True
    
    elif (guess<char):
        aStr = aStr[index:]
        return isIn(char, aStr)
    
    elif (guess > char):
        aStr = aStr[0:index]
        return isIn(char, aStr)


print (isIn('e', 'abcde'))