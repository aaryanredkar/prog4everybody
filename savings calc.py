mon=int(input( "Enter retail price:"))
perc = int(input ("discout percentage:"))
pay = 100 - perc
dec = pay / 100
sumt = mon *dec
print("You payed:"+ str(sumt))

suma= mon-sumt

print("You saved:"+str(suma))
