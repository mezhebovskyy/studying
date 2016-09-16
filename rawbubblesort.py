mass = ["SLOVO", "mommy", "ten"]
for i in range(len(mass)):
    for j in range(len(mass)-1,i,-1):
        if len(mass[j])<len(mass[j-1]):
            #mass[j], mass[j-1] = mass[j-1], mass[j]
            temp = mass[j]
            mass[j] = mass[j-1]
            mass[j-1] = temp
        print i
        print j
        print mass