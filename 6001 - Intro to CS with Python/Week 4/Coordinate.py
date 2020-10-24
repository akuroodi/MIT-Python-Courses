class Coordinate (object):
    def __init__ (self, x, y):              # initializing method, always run auto when an instance made
        self.x = x
        self.y = y

    def distance (self, other):             # regular method run when called on Coordinate object
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        
        x_diff *= x_diff
        y_diff *= y_diff

        return (x_diff + y_diff) ** 0.5

    def __sub__ (self, other):
        return Coordinate (self.x - other.x , self.y - other.y)        #overrides default subtract operation for Coordinate objects

origin = Coordinate (0,0)
z = Coordinate(3,4)

print (z.distance(origin))      # assumes z = self

print (origin.distance(z))      # assumes origin = self

print (Coordinate.distance(z, origin))      # direct call to Coordinate instance, needs both params





class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        #return "Number(" +str(self.value)+ ")"
        return "Number(%s)" % (self.value)          #note the 2 ways you can print the string rep


num = Number(2)
print(repr(num))