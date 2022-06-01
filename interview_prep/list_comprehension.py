lst = [1,2,-5,4]
def square(x):
    return x * x

squares = [square(num) for num in lst] 
print(squares)

def is_odd(x):
    return x %2 == 1

odds = [num for num in lst if is_odd(num)]
print(odds)