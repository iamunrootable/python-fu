people = input("How many people are in your group: ")
people = int(people)
if people < 8:
    print(f"I found a table that can fit {people} people")
else: 
    print(f"I am sorry we don't have a table that will fit {people} people")