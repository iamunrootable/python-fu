prompt = "\nEnter pizza toppings: "
prompt += "\n(Enter quit when you're done.) "
toppings = ""
current_toppings = 0
toppings_list = []
while current_toppings < 5:
    current_toppings += 1
    toppings = input(prompt)
    if toppings == "quit":
        break
    else:
        toppings_list.append(toppings)
        print(f"Adding {toppings} to your pizza")
pizza_list = "\n".join(toppings_list)
print("Your pizza with the following toppings is on the way:")
print(f"{pizza_list}")