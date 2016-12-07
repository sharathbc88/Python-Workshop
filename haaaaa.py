"""import random
from operator import itemgetter

def get_day(num):
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    return days[num]

foods = ['Sandwich', 'Burger', 'Chicken Rice', 'Udon', 'Teriyaki chicken', 'Sushi', 'Fried Noodles']

#print(list(range(7))

for i in range(7): #7 days in a week
    print(i)
    daily_meals = []
    print (daily_meals)
    for j in range(3): #3 meals
        print("inner", j)
        rand_num = random.randint(0,len(foods)-1)
        print(rand_num)
        print(len(foods))
        daily_meals.append(foods[rand_num])
        print(daily_meals)
    print("{}: breakfast {}; lunch {}; dinner {}. ".format(get_day(i), daily_meals[0], daily_meals[1], daily_meals[2]))


for i in range(7): #7 days in a week
    daily_meals = []
    for j in range(3): #3 meals
        rand_num = random.randint(0,len(foods)-1)
        daily_meals.append(foods[rand_num])
    print("{}: breakfast {}; lunch {}; dinner {}. ".format(get_day(i), daily_meals[0], daily_meals[1], daily_meals[2]))

name_list = [["John", 20, "yellow"], ["Jordan", 25, "red"], ["Dunken", 25, "Black"]]
print("before sort: ", foods)
print (name_list)
foods.sort()
print("after sort: ", foods)
print("before sort: ", name_list)
name_list.sort(key=itemgetter(1, 0))
print("after sort: ", name_list)

"""

