mass = [5, 1, 10, 16, 2]
for i in range(len(mass)):
    for j in range(len(mass)-1,i,-1):
        if mass[j]<mass[j-1]:
            #mass[j], mass[j-1] = mass[j-1], mass[j]
            temp = mass[j]
            mass[j] = mass[j-1]
            mass[j-1] = temp
        print i
        print j
        print mass