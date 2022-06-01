sandwhich_orders = ['pastrami','reuben','ham','blt','pastrami','turkey','pastrami']
finished_sandwhiches = [] 

print("The kitchen has ran out of pastrami.")
while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')

while sandwhich_orders:
    current_order = sandwhich_orders.pop()
    print(f"Your {current_order} sandwhich is ready.")
    finished_sandwhiches.append(current_order)
final_list = "\n".join(finished_sandwhiches)
print(f"\nThe following sandwhiches have been made:")
print(final_list)
