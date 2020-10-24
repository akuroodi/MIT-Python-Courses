def listFlattener1 (inputList):
    return [ inputList[i] for i in range(0, len(inputList))  ]



def listFlattener2 (inputList):
    return [ subList[i] for subList in inputList for i in range(0, len(inputList))  ]

y = [ [1,2,3], [4,5,6], [7,8,9]]

print(listFlattener1(y))             # since only 1 for in your line, doesn't index into nested list

print(listFlattener2(y))