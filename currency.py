print("US Dollar = US, Euro = EU, British Pound sterling = BP, Australian Dollar,Cinese Yaun = CY, Japanese Yen = JY, Canadian Dollar = CD")

cur_from = input("Enter 1st currency:")
cur_from = cur_from.upper()
cur_to = input("Enter 2nd currency:")
cur_to =cur_to.upper()
amount = int(input("Enter amount to amount:"))

if cur_from =="US":
      dollarValue = amount/1
elif cur_from == "EU":
      dollarValue = amount/0.93
elif cur_from == "BP":
      dollarValue = amount/0.67
elif cur_from == "AU":
      dollarValue = amount/1.29
elif cur_from == "CY":
      dollarValue = amount/6.23
elif cur_from == "JY":
      dollarValue = amount/120.3
elif cur_from == "CD":
      dollarValue = amount/1.26
else:
      dollarValue = 0


if cur_to =="US":
      conVal = dollarValue * 1
elif cur_to =="EU":
      conVal = dollarValue * 0.93
elif cur_to =="BP":
      conVal = dollarValue * 0.67
elif cur_to =="AU":
       conVal = dollarValue * 1.29
elif cur_to =="CY":
       conVal = dollarValue * 6.23
elif cur_to =="JY":
       conVal = dollarValue * 120.6
elif cur_to =="CD":
       conVal = dollarValue * 1.26
else:
      conVal==dollarValue*0

if conVal !=0:
     print ("Converted value of " + str(amount) + " " + str(cur_from) + " to " + str(cur_to) + " is "+ "{:10.2f}".format(conVal))

     


      

