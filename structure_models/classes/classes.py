import math
class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def Greetings(self):
        print "Hello! My name is %s" % self.name
    def PrintParams(self):
        print "Height: \t%d" % self.height
        print "Weight: \t%d" % self.weight
        print "Age:    \t%d" % self.age

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Circle:
    
    def __init__(self, r):
        self.r = r
    def PrintSquare(self):
        print math.pi*(self.r**2)

misha = Person("Misha", 27, 180, 73)
pasha = Person("Babulya", 27, 195, 80)

misha.Greetings()
misha.PrintParams()
pasha.Greetings()
pasha.PrintParams()

# concreteCircle = Circle(20)
# concreteCircle.PrintSquare()
