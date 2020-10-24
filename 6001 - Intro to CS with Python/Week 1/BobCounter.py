# Assume s is a string of lower case characters.

# Write a program that counts up the number of times "bob" appears in the string s. 
# 
# For example, if s = 'azcbobobegghakl', your program should print: 

# Number of times bob occurs is: 2


s = 'bobbbbobob'

numBobs = 0
length = len(s)
sindex = 0


while (sindex < (length-2)):
    
    z = s[sindex] + s[sindex+1] + s[sindex+2]

    if (z == "bob"): numBobs+=1

    sindex +=1
print("Number of times bob occurs is: " + str(numBobs))
    
    