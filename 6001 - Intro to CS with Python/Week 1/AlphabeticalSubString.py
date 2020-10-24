# Assume s is a string of lower case characters.

# Write a program that prints the longest alphabetical substring of s 
# For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. 

s = 'abcbcd'

longstring = s[0]              # start with first char as longest substring
longcopy = ''

length = len(s)
sindex = 0

while (sindex < length - 1):   # Iterate up until the last char in string s 
    if (s[sindex] <= s[sindex+1] ):
        longstring += s[sindex+1]
        sindex += 1
        continue
    
    if (len(longstring) > len(longcopy)):
        longcopy = longstring
    
    
    sindex += 1
    longstring = s[sindex]
    
       
if (len(longstring) > len(longcopy)): print("Longest substring in alphabetical order is: " + longstring)
else: print("Longest substring in alphabetical order is: " + longcopy)