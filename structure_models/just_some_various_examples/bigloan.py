def checkthetype(method,interest,amount,timeborr):
    if method == "differential":
        differential(interest,amount,timeborr)
    if method == "annuity":
        annuity(interest,amount,timeborr)

def differential(interest,amount,months):
    totalpayment = []
    current_credit_amount = amount
    for month in range (0,months):
        sum_of_repay = current_credit_amount * interest + amount/months
        credit_left = current_credit_amount - sum_of_repay
        totalpayment.append(sum_of_repay)
        if credit_left < current_credit_amount:
           current_credit_amount = credit_left
    print sum(totalpayment)

def annuity(interest,amount,months):
    annuitypayment = amount * (interest / (1 - (1 + interest) ** (months * (-1))))
    totalpayment = annuitypayment * months
    print totalpayment

def main():
    interest = 0.01
    amount = int(raw_input("What credit amount do you want to borrow?: "))
    timeborr = int(raw_input("On what term (months) do you want to borrow?: "))
    typeofrepay = raw_input("What type of repayment on credit (annuity or differential) do you prefer?: ")
    checkthetype(typeofrepay,interest,amount,timeborr) 

if __name__ == "__main__":
    main()
