print("    Money Counter Program           ")

# Notes
oneHundredDollar = int(input("How many $100 notes: "))
fiftyDollar = int(input("How many $50 notes: "))
twentyDollar = int(input("How many $20 notes: "))
tenDollar = int(input("How many $10 notes: "))
fiveDollar = int(input("How many $5 notes: "))


# Coins
twoDollar = int(input("How many $2 coins: "))
oneDollar = int(input("How many $1 coins: "))
fiftyCent = int(input("How many 50c coins: "))
twentyCent = int(input("How many 20c coins: "))
tenCent = int(input("How many 10c coins: "))
fiveCent = int(input("How many 5c coins: "))
# Note totals
oneHundredDollarTotal = (oneHundredDollar * 100)
fiftyDollarTotal = (fiftyDollar * 50)
twentyDollarTotal = (twentyDollar * 20)
tenDollarTotal = (tenDollar * 10)
fiveDollarTotal = (fiveDollar * 5)

# Coin totals
twoDollarTotal = (twoDollar * 2)
oneDollarTotal = (oneDollar * 1)
fiftyCentTotal = (fiftyCent * 0.5)
twentyCentTotal = (twentyCent * 0.2)
tenCentTotal = (tenCent * 0.1)
fiveCentTotal = (fiveCent * 0.05)

print(" ")

print("   Change Breakdown     ")
print("")
print("____________Notes____________")

print("You have", "$"+(str(format(oneHundredDollarTotal,".2f"))), "in one hundred dollar notes")
print("You have", "$"+(str(format(fiftyDollarTotal,".2f"))), "in fifty dollar notes")
print("You have", "$"+(str(format(twentyDollarTotal,".2f"))), "in twenty dollar notes")
print("You have", "$"+(str(format(tenDollarTotal,".2f"))), "in ten dollar notes")
print("You have", "$"+(str(format(fiveDollarTotal,".2f"))), "in five dollar notes")
print("")

print("____________Coins____________")
print("You have", "$"+(str(format(twoDollarTotal,".2f"))), "in two dollar coins")
print("You have", "$"+(str(format(oneDollarTotal,".2f"))), "in one dollar coins")
print("You have", "$"+(str(format(fiftyCentTotal,".2f"))), "in fifty cent coins")
print("You have", "$"+(str(format(twentyCentTotal,".2f"))), "in twenty cent coins")
print("You have", "$"+(str(format(tenCentTotal,".2f"))), "in ten cent coins")
print("You have","$"+(str (format(fiveCentTotal,".2f"))), "in five cent coins")

grossTotal = (twoDollarTotal+oneDollarTotal+fiftyCentTotal+twentyCentTotal+tenCentTotal+fiveCentTotal+oneHundredDollarTotal+fiftyDollarTotal+twentyDollarTotal+tenDollarTotal+fiveDollarTotal)
print("")
print("____________Total Amount____________")
print("Total amount:", "$"+(str(format(grossTotal, ".2f"))))
