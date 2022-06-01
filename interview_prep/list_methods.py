from logging import lastResort


lst = [1,2,-5,7]
is_truth = any(lst)

is_odd = [(lambda x: x % 2 == 1)(num) for num in lst]
print(is_odd)