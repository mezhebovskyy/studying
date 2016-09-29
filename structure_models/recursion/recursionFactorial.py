def factorN(n):
    if n == 0:
        return 1
    else:
        return n * factorN(n - 1)

number = int(raw_input("Enter a number: "))
print factorN(number)