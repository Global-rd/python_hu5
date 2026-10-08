my_list = [1,2,3]
print(f"Original list ID: {id(my_list)}")

my_list.append(4)
print(f"Modified list ID: {id(my_list)}")
print(f"Modified list: {my_list}")


my_tuple =(1,2,3)
print(f"Original tuple ID: {id(my_tuple)}")

#my_tuple[0] = 4
new_tuple = my_tuple + (4,)
print(f"Modified tuple ID: {id(new_tuple)})")

# strings

name = "sarah"
#name[0] = "T"
print(name)

print(name.upper())
name = name.upper()
print(name)

#mutable: 
#list, dictionary, sets, (bytearrays)

#immutable:
#string, bool, int, tuple, frozenset, none

t = (1,2,3)
t = ([1,2], [3,4])
print(t)
t[0].append(1)
print(t)
