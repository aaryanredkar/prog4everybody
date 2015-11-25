fname = raw_input("Enter file name: ")
fh = open(fname)
dic = dict()
for line in fh:
	words = line.split()
	for word in words:
                if word not in dic:
                        dic[word] = 1
                else:
                        dic[word] += 1
    
print dic
