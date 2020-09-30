def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    
    guess = 1
    negGuess = -1*guess

    # Zero is best case answer, quickly check if it's a solution
    if test(0): return 0
    
    while (test(guess) != True and test(negGuess) != True):
    
        negGuess -= 1
        guess += 1
    
    if test(guess): return guess
    else: return negGuess





#### This function checks if x = 3 somehow
# Edit: simply makes a list, and indexes the xth element from the end from it -_-
def f(x):
    return [1,2,3][-x] == 1 and x != 0





print(solveit(f))