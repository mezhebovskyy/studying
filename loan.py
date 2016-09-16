def function(a,b,c):
    return a * b * c + b

interest = 0.01
sum = int(raw_input("What credit amount do you want to borrow?: "))
timeborr = int(raw_input("On what term (months) do you want to borrow?: "))

print function(sum,interest,timeborr)