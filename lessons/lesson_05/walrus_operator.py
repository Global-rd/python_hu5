items = ["apple", "cherry", "banana", "elderflower"]

treshold = 3

#without walrus operator
length = len(items)

if length > treshold:
    print(f"The list has {length} items, which is greater than {treshold}")

#wth walrus operator

if (length := len(items)) > treshold:
    print(f"The list has {length} items, which is greater than {treshold}")
