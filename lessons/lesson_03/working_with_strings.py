fruit = "raspberry apple"

fruit_length = len(fruit)
print(fruit_length)

#concatenation
first_name = "Istvan Gabor"
last_Name = "Nagy"

full_name = first_name + " " + last_Name
print(full_name)
introduction = "My name is " + first_name + " " + last_Name + "."
print(introduction)

#interpolation / interpoláció - F STRING

introduction = f"My name is {first_name} {last_Name}."
print(introduction)

# indexing, slicing, striding

print(fruit)
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])
print(fruit[-1])

print(fruit[1:3]) #1. elem: inclusive, záró elem: exclusive
print(fruit[3:])
print(fruit[-2:])
print(fruit[-1::-2])

# string methods / metódus

#metódus: az amit egy objektum tud csinálni, vagy egy objektummal tudunk csinálni
#attribútum: ami jellemzi az objektumot

# objektum: kutya
# metódus: ugat, eszik, iszik, alszik, játszik
# atribútum: életkor, fajta, testsúly, neve

print("----------------")
print(fruit)

print(fruit.capitalize())
print(fruit.upper())
print(fruit.title())

print(fruit.replace("a", "*"))
fruit = "         apple      "
print(fruit.strip())
print(fruit)
#method chaining

print(fruit.upper()
           .replace("A", "#")
           .strip())

