class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        self.values = []
        self.keys = [] 
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        if k not in self.keys:
            self.keys.append(k)
            self.values.append(v)
        else:
            index = self.keys.index(k)
            self.values[index] = v      # update value if key already in dictionary
        
    def getval(self, k):
        """ k, immutable object  """ 
        try:
            index = self.keys.index(k)
            return self.values[index]

        except ValueError:
            print("The key " + str(k) + " does not exist in dictionary.")
    
    def delete(self, k):
        """ k, immutable object """   
        try:
            index = self.keys.index(k)
            del self.values[index]
            self.keys.remove(k)
        
        except ValueError:
            #print("The key " + str(k) + " does not exist in dictionary.")
            raise KeyError

