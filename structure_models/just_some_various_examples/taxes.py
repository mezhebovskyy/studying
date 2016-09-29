months = ["Jan", "Feb", "March"]
amountmass = []
for month in months:
    amountstr = raw_input ("How much money have you earned in "+ month+"?: ")
    amount = int(amountstr)
    amountmass.append(amount)

protax = raw_input("What profit tax (in %) is in your country? ")
protaxint = float(protax)
pentax = raw_input("What pension amount duty is in your country?: ")
pentaxint = int(pentax)
taxsum=0
for n in amountmass:
    taxsum=taxsum+(n*protaxint/100+pentaxint)

print "Your tax is "+str(taxsum)