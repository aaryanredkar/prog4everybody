
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
add = 0
for line in fh:
    #if not line.startswith("X-DSPAM-Confidence:") : continue
    if line.startswith("X-DSPAM-Confidence:"):
        dig = line.find(':')
        num = float(line[dig+2:])
        add = add + num
        count = count + 1
avg = add/count
print "Average spam confidence: ",avg



    
    


     
