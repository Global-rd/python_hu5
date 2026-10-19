#arithmetic operators

a = 1 + 2
print(7//3)

#assignment operators
x = 12
x += 5

#comparison operators
a = 2
b = 3

print(a == b)
print(a != b)

#logical operators
print("------------------")
a  = True
b = False
print(a and b)
print(a or b)
print(not a and not b)
print("------------------")
x = 9
y = 3

print(x < 10 and y == 2)
print(x < 10 or y == 2)


#identity operators
print("------------------")
print(x is y)
print(x is not y)

# identity vs comparison operator
print("------------------")

a = 10
b = 10

print(a is b)
print(a == b)
print(id(a))
print(id(b))

print("------------------")
x = [1,2,3]
y = [1,2,3]

print(id(x))
print(id(y))

print(x is y)
print(x == y)
print("------------------")
a = 10
b = a #10
a = 11
b = a #11

print(a)
print(b)
print("------------------")
x = [1,2,3]
y = x #[1,2,3]

x.append(4)
print(x)
print(y)

print(id(x))
print(id(y))

#membership operators
print("------------------")
print(1 in x)
print(1 not in x)

#operator precedence
print("------------------")
print(True or False and False)
print((True or False) and False)

# short circuit evalution
print(False and True and False and True)



