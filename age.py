quantity = raw_input ("How many people are there is your group?: ")
quantityint = int(quantity)
names = []
for number in range(0,quantityint):
    name = raw_input ("What is your name?: ")
    names.append(name)

total=0
for name in names:
    agestr = raw_input ("How old is "+name+"? ")
    age = int(agestr) 
    total=total+age

print total/quantityint