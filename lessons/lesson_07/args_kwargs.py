

#*args

def calculate_total_price(*items):

    """
    Accepts any number of tuples e.g. (name, unit_price, quantity)
    and returns the total price.
    """

    total = 0

    for _, unit_price, quantity in items:
        total += unit_price * quantity

    return total


total = calculate_total_price(
    ("Apple", 300, 2),
    ("Pear", 250, 3),
    ("Orange", 400, 1)
)
print(total)


#**kwargs

def describe_person(**attributes):
    print(attributes)
    print(type(attributes))

    for k,v in attributes.items():
        print(k, v)


describe_person(name="Steve", age=15, job="programmer")

print("--------------")
def introduce_person(name, age, *hobbies, country="Hungary", **additional_info):
    print(name)
    print(age)
    print(country)

    if hobbies:
        for hobby in hobbies:
            print(hobby)

    if additional_info:
        for k,v in additional_info.items():
            print(k,v)


introduce_person("Steve",
                 15,
                 "hiking",
                 "reading",
                 "surfing",
                 country="Switzerland",
                 job="programmer",
                 has_pet=True
                 )
