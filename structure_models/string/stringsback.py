stroka = raw_input("Type this bitch: ")

backwards = ""
for i in range(len(stroka)-1,-1,-1):
    backwards = backwards + stroka[i]

print backwards