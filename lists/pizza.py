my_foods = ['pizza','falafel','carrot_cake','pho','chocolate','candy']
luaras_foods = my_foods[:]
print(f"The first 3 items in the list are {my_foods[:3]}")
print(f"The middle 3 items are {my_foods[2:5]}")
print(f"the last 3 items are {my_foods[-3:]}")
first_3 = [food for food in my_foods[:3]]
print (first_3)