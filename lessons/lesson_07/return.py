# function without return value:

def add(num_1, num_2):
    print(num_1 + num_2)

value = add(1,2)
print(value)
print(type(value))

# function with return value:

def add(num_1, num_2):
    return num_1 + num_2

value = add(num_2=2, num_1=1)
print(value)
print(type(value))


#return early

def calculate_age_in_days(age):

    if age < 0:
        print("Invalid age! Please provide a positive number!")
        return #return early

    age_in_days = age * 365
    return age_in_days

age_in_days = calculate_age_in_days(20)
print(age_in_days)


#returning multiple values
def multiply_two_values(a,b):
    return a*2, b*2

num_1, num_2 = multiply_two_values(2,3)
print(type(num_1))
print(type(num_2))

#functions

def remove_negatives(nums):

    for num in nums[:]:
        if num < 0:
            nums.remove(num)

    return nums

numbers = [1, -3, 4, -5]
print(remove_negatives(numbers))



