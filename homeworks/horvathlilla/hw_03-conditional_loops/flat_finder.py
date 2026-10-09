city=input ("Enter the city name: ")
rent=float(input ("Enter monthly rent: "))

if city=="New York" or city=="San Francisco":
    if rent<4000:
        print (f"Sarah can afford to rent in {city} with a monthly rent of ${rent}.")
    else: 
        print (f"Sarah cannot afford to rent in {city} with a monthly rent of ${rent}.")

elif city=="Washington":
    if rent!=0:
        print (f"Sarah will not rent in {city}.")

elif city=="Chicago":
    if rent!=0:
        print (f"Sarah is happy to rent in {city} with a monthly rent of ${rent}.")

elif city!="New York" and city!="San Francisco" and city!="Washington" and city!="Chicago":
    if rent<3000:
        print (f"Sarah can afford to rent in {city} with a monthly rent of ${rent}.")
    else:
        print (f"Sarah cannot afford to rent in {city} with a monthly rent of ${rent}.")

#kerdes: lehet ezt ugy csinalni hogy ne legyen "case sensitive"?
#vert izzadtam mire rajottem hogy miert nem akarja kiprintelni a helyes uzenetet amikor teszteltem :D
