quantity = int(raw_input ("How many people are there is your group?: "))
names = []
for number in range(0,quantity):
    name = raw_input ("What is your name?: ")
    names.append(name)

total=0
for name in names:
    age = int(raw_input ("How old is "+name+"? "))
    total=total+age

print total/quantity