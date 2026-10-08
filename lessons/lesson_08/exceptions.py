def divide_numbers(a,b):
    return a / b

result = divide_numbers(1,2)
print(result)


#ZERO DIVISION ERROR

result = divide_numbers(10, 1)
print(result)

#INDEX ERROR

my_list = [1,2,3,4,5]

print(my_list[0])

#KEY ERROR

my_dict = {"a": 1,
           "b": 2}

#print(my_dict.get("c", 3))

try:
    a = float(input("First number"))
    b = float(input("Second number"))
    c = a / b
    print(c)
except ValueError as e:
    print(f"Value error: {e}")
except ZeroDivisionError as e:
    print(f"You can not divide by zero. {e}")
except Exception as e:
    print(f"Something unexpected happened: {e}")
finally:
    print("Division attempt finished")

print("test")


print("--------------------")
#bad example:
def calculate_rectangle_area(a,b):
    return a * b

area = calculate_rectangle_area(-1,5)
print(area)

def calculate_rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError(f"Both params must be a postitive number! Length: {length} Width: {width}")

    return length * width

print(calculate_rectangle_area(5, -1))

try:
    area = calculate_rectangle_area(5, -1)
except ValueError as e:
    print(f"Value error: {e}")


