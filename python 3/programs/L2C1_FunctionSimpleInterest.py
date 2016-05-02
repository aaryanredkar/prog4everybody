#Calculate Simple Interest
def simple_interest(initial_amount,rate=2, time=5):
    return initial_amount + (initial_amount * (rate/100) * time)

principalamount=float(input("Please enter the Principal Amount:"))
interestrate=float(input("Please enter the Interest Rate:"))
time=int(input("Please enter the time in years:"))

final_amount = simple_interest(principalamount)
print("You will receive $%s after 5 years." % (final_amount))
