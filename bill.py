def cal_tip(amt,tp):
    return amt + (amt*tp/100)

def cal_amount(totel_amt,number):
    return total_amt/number



bill = int(input("What is the total bill:"))
tip = int(input("What is the tip:"))
people = int(input("How many people are attending:"))
total_bill = bill + (bill * tip/100)

total = total_bill/people
print(total)
          
          
if bill<= 0:
    print("error")
