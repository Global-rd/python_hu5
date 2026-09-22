#VARIABLES / VÁLTOZÓK

name = "Jim"
age = 15

print(name)
age = 25 + 1
print(age)


camelCaseVariableName = "" #BAD PRACTICE PYTHON-BAN!
snake_case_variable_name = "" #GOOD PRACTICE PYTHON-BAN!

#CONSTANTS / KONSTANSOK

PI = 3.14
MAX_ROUNDS = 3

#DYNMACIALLY TYPED LANGUAGE / DINAMIKUSAN TÍPUSOS NYELV

number = 10
#number: int = "almafa"
print(number)
number = "appletree"
print(number)

print(number * 3)
#print(number / 3)

#reference

print("-------------------")

my_var = 15
my_var_2 = 15

print(id(my_var))
print(id(my_var_2))

#15 -> my_var, my_var_2


print("-------------------")

x = 11
y = x #11

print(id(x))
print(id(y))
print(x)
print(y)

x = 10

print(id(x))
print(id(y))
print(x)
print(y)

x = 1000 #1000 -> reference count = 1
x = 2000  #1000 -> reference count = 0
