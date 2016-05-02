subject =["Math", "History", "Science", "English","PE"]
score = [20/20, 19/20, 18/20, 17/20, 19.5/20]
percent = 0

for i in range (len(subject)):
    percent = score[i] * 100
    print ("{0} {1:.2f}".format(subject[i].ljust(10), percent))
    
