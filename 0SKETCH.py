fileName = "sketchcars.txt"

class Car:
    def __init__(self, hp=0, mod=""):
        self.hp = hp
        self.mod = mod


database = []
database.append(Car(125, "jetta"))
database.append(Car(119, "jetta1"))
database.append(Car(111, "jetta2"))
database.append(Car(150, "jetta3"))

f = open(fileName, "a")
for i in database:
    lineToAddIntoFile = "%s,%s" % (i.hp, i.mod)
    f.write(lineToAddIntoFile + '\n')
f.flush()
f.close()

database = []
w = open(fileName, "r")
for line in w:
    hp, mod = fileContent.split(",")
    car = Car(int(hp), mod)
    database.append(car)
w.flush()
w.close()



