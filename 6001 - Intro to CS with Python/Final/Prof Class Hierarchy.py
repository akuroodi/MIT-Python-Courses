class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  # explicitly uses Person version of say method

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def lecture(self, stuff): 
        return 'It is obvious that ' + Person.say(self,stuff)
    
    def say(self, stuff):
        return Person.say(self,"") + 'It is obvious that ' + Person.say(self,stuff)

x = Person("floof")
print( x.say("wabba") )

y = Lecturer("floof")
print( y.say("wabba") )
print(y.lecture("wabba"))

print()

z = Professor("floof")
print( z.say("wabba"))
print(z.lecture("wabba"))


u = ArrogantProfessor("Woz")
print(u.say("wabba"))
print( u.lecture("wabba") )


