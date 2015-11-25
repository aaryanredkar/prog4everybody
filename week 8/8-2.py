fname = raw_input("Enter file name: ")


fh = open(fname)
dic = dict()


for line in fh:
  
  if line.startswith('From'):
    t=line.split()
    email = t[1]
    if email not in dic:
        dic[email] = 1

    else:
        dic[email] +=1

bigcount = None
bigemail = None
for email,count in dic.items():
  if bigcount is None or count > bigcount:
    bigemail = email
    bigcount = count
        
print bigemail, bigcount
