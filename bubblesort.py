def bubblesort(l):
    for i in range(len(l)):
        for j in range(len(l)-1,i,-1):
            if l[j]<l[j-1]:
                #l[j], l[j-1] = l[j-1], l[j]
                temp = l[j]
                l[j] = l[j-1]
                l[j-1] = temp

def checkifdot(stroka):
    return stroka == "."
    
mass = []
while(True):
    num = raw_input("Please enter a digit: ")
    if (checkifdot(num)):
        break
    intnum = int(num)
    mass.append(intnum)


bubblesort(mass)
print mass   