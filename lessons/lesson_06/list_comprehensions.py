import time
numbers = [1,2,3,4,5]

squared_numbers = []

#with for loop:
for number in numbers:
    squared_numbers.append(number ** 2)

print(squared_numbers)

#list comprehension:

squared_numbers = [number ** 2 for number in numbers]

print(squared_numbers)


#with for loop:

even_squares = []
for number in numbers:
    if number % 2 == 0:
        even_squares.append(number ** 2)

print(even_squares)

#list comprehension

even_squares = [number ** 2 for number
                 in numbers if number % 2 == 0]


numbers = range(1, 10000000)
start = time.time()

squares_loop = []

for num in numbers:
    squares_loop.append(num ** 2)

end = time.time()

print(f"For loop: {end-start}")

start_time = time.time()
squares_comprehension = [num ** 2 for num in numbers]
end_time = time.time()
print(f"comprehension: {end_time-start_time}")



