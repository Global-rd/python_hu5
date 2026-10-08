original_set = {1,2,3,4,5,5,6}
new_set = {4,5,6,7}

print(id(original_set))
original_set.update(new_set)
print(original_set)
print(id(original_set))

numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2]
numbers_list = list(set(numbers))
print(numbers_list)

original_set.add(78)
print(original_set)

original_set.remove(78)
print(original_set)

original_set = {1,2,3,4,5}
new_set = {4,5,6,7}

intersection = original_set.intersection(new_set)
print(intersection)

intersection = original_set - new_set
print(intersection)


#FROZENSET

my_set = frozenset([1,2,3])
print(my_set)