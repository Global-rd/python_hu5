#syntax 

condition = None

if condition == True:
    print("The condition is True")
else:
    print("The condition is not True")


#truthy-falsy values
print(bool(1))
print(bool(0))
print(bool("apple"))
print(bool(""))
print(bool([1,2,3]))
print(bool([]))
print(bool(None))

if condition:
    print("The condition is True")
else:
    print("The condition is not True")

number = 1

if number:
    print("The value is a different number than 0")
else:
    print("The value is 0 (if number)")

my_list = []

if my_list:
    print("The list has items")


number = 10

if number == 10:
    print("The number is 10")
elif number == 11:
    print("The number is 11")
elif number == 13:
    print("The number is 13")
elif number == 14:
    print("The number is 14")
else:
    print(f"The number is something different: {number}")

fruits = ["raspberry", "cherry", "banana", "elderflower"]

if "raspberry" in fruits:
    print("raspberry  is present in fruits")

if "banana" in fruits:
    print("banana  is present in fruits")

#identity
a = 1
b = 2
c = 3

if a is b:
    print("Ther 2 objects are the same by ID!")


#combining multiple operators:

if (a is not b and c == 4) and ("cherry" in fruits or "elderflower" in fruits):
    print("OK")
else:
    print("NOT OK!")


