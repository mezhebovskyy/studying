def numbers(a, b):
    if a >= b:
        if(a == b):
            return a
        return str(a) + " " + str(numbers(a - 1, b))
    if a <=b:
        if(a == b):
            return b
        return str(a) + " "  + str(numbers(a + 1, b))

first = int(raw_input("Enter first number: "))
last = int(raw_input("Enter last number: "))
print numbers(first, last)