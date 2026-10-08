letters = ["a", "b", "c"]
mixed_type_list = ["a", 1, 1.3, None, False]
print(type(letters))

numbers = list(range(1, 100))
print(type(numbers))
print(numbers)

#indexing

names = ["Sarah", "Tim", "Jim", "Timothy"]
print(names[:2])

print(names[0])
names[:2] = ["Tarah", "Dexter"]
print(names)

names[-1] = "RandomName" 
print(names)
print(len(names))

names[1:3] = ["Timmy", "Kyle", "Sofia"]
print(names)
print(len(names))

names[1:3] = ["Jeremy"]
print(names)
print(len(names))

#methods

names.append("Steve")
print(names)
names.extend(["Steven", "Emily"])
print(names)
print(len(names))

names.insert(0, "First Name")
print(names)

names.remove("Emily")
print(names)

names.pop(1)
print(names)


del names[1]

names.clear()
print(names)

