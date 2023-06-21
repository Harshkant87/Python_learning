# 1. functions with multiple arguements
def area(a, b):
    return a*b

print(area(4, 5))

# 2. when variable postions are not in order
def division(a, b):
    return a / b

print(division(b = 2, a = 10))

# 3. Default arguments with values
def multi(a, b = 10):
    return a * b

print(multi(3))

# 4. pass as many args as you want, here args is a tuple
def mean(*args):
    return sum(args) / len(args)

print(mean(1,2,3,4,5))

# 5. pass as many args with keywords(kwargs), here kwargs is a dictionary
def meanK(**kwargs):
    return kwargs

print(meanK(a=2, b=4, c=8))