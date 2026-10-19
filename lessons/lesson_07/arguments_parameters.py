def greet(name): #name: parameter
    print(f"Hello {name}")

greet("Johnny") #Johnny : argument

def add(x,y):
    return x + y

result = add(1,2) #positional arguments
result = add(x=1, y=2) # keyword argument

#default argument/parameter


def get_greeting(name="User"): #name: parameter
    print(f"Hello {name}")

get_greeting()

print("----------------")

def show_book_details(title, author="Test Author", year=2026):

    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")

show_book_details("Test Book")
show_book_details("Test Book", "XY")
show_book_details("Test Book", "XY", 1999)


#mutable objects as default arguments

#bad example

def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

print(append_to_list(1))
print(append_to_list(2))

# good example:

def append_to_list(value, my_list=None):

    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

print(append_to_list(1))
print(append_to_list(2))


