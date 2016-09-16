def annuity(interest,amount,months):
    annuitypayment = amount*(interest/(1-(1+interest)**(1-months)))
    totalpayment = annuitypayment * months
    print totalpayment

interest = 0.01
amount = int(raw_input("What credit amount do you want to borrow?: "))
timeborr = int(raw_input("On what term (months) do you want to borrow?: "))

annuity(interest,amount,timeborr)

