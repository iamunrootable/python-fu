import time
import random
# Time decorator
def timed_func(func_to_time):
    def timed(*args, **kwargs):
        start = time.perf_counter()
        res = func_to_time(*args, **kwargs)
        print(time.perf_counter() - start)
        return res
    return timed
# Bubble sort has a O(n^2) time complexity due to the ensted for loops
@timed_func
def bubble_sort(items):
    for i in range(len(items)):
        already_sorted = True
        for j in range(len(items)-i-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                already_sorted = False
        if already_sorted:
            break
    return items
items = [random.randint(1,1000) for _ in range(10000)]
sorted_items = bubble_sort(items)
print(sorted_items[1])