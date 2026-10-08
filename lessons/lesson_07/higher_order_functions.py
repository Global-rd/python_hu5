from functools import reduce

#MAP:

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(square, numbers))
print(squared_numbers)

#FILTER:
def is_even(x):
    return x % 2 == 0 #True, False

numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(is_even, numbers))
print(even_numbers)

#REDUCE
numbers = [1, 2, 3, 4]

def add(x,y):
    return x + y

total = reduce(add, numbers)
print(total)


def double(x):
    return x * 2

numbers = [1,2,3,4]

result = list(map(lambda x: x * 2, numbers))
print(result)

