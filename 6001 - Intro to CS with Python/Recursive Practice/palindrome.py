# Write a recursive function to check if a number is a palindrome

import string
def isPalindrome (s):
    """ 
    Input: Assume s is a string representing a nonnegative integer

    Output: True if palindrome, False if not
    """

    if len(s) == 0: return False

    if len(s) == 1: return True             # Base case where any single digit is a palindrome
    
    if s[0] == s[-1]:                       # if first and last digits are the same, strip them and check substring
        if len(s) == 2: return True         # unless string is only 2 digits long
        return isPalindrome(s[1:len(s) -1])

    else:
        return False

print (isPalindrome("020"))