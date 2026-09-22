fruit = "apple"

print(type(fruit))

print(isinstance(fruit, str))

# type conversion / típus konverzió

num_int = 10
num_float = 10.5
result = num_int * num_float
print(result)
print(type(result))

age = "13"
age_in_days = int(age) * 365
print(age_in_days)

number_float = 10.9
print(int(number_float))

print(type(round(number_float)))
print("------------------")
#input

age = int(input("How old are you? "))
print(type(age))

#truthy-falsy értékek
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("appletree"))

