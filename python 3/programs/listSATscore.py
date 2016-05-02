students = ["John", "Kevin", "Raj", "James", "Bill", "Jane"]
ranking = [2100, 2260, 2310, 1700, 1920, 2400]
temp_ranking = []
index = 0

temp_ranking = ranking.copy()
temp_ranking.sort()
temp_ranking.reverse()

for element in temp_ranking:
    index = ranking.index(element)
    print (students[index], "--->", ranking[index])
