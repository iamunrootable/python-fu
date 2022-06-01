vacations = {}
polling_active = True

while polling_active:
    name = input("\n What is your name? ")
    dream_vacation = input("Where in the world would you dream of going? ")

    vacations[name] = dream_vacation

    more_travelers = input("Is anyone else joining? yes/no ")
    if more_travelers != "yes":
        polling_active = False

print("\n---Vacation voting results ---")
for name, dream_vacation in vacations.items():
    print(f"{name} would like to visit {dream_vacation}")
