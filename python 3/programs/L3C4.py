def createFoodList():
    food= dict()
    food["JOhn"] = "Pizza"
    food["Jack"] ="Burger"
    food["raj"]= "Broccoli"
    food["Jane"] ="Fish"
    food ["Kevin King"] = "Potato Salad"
    food["Bill"] = "French Fries"
    return food
user_food = createFoodList()

len_username = 0

for key in user_food:
    if (len(key) > len_username):
          len_username = len(key)
print("User and ther favorite food:")
for key in user_food:
    print("{user}: {food}".format(user=key.ljust(len_username+1), food =user_food[key]))
