def factor(n):
    if n < 0:
        print("Sorry, negative numbers don't have factorial.")
    elif n == 0:
        print("The factorial of 0 is 1.")
    else:
        fac = 1
        for i in range(1, n+1):
            fac = fac * i
        print "The factorial of " + str(n) + " is " + str(fac) + "."

number = int(raw_input("Enter a number: "))
factor(number)