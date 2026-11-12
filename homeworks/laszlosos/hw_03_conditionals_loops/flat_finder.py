city = input("Which city? ")
rent = int(input("How much rent? "))
print(city, rent)
if city in ["New York", "San Fransisco"] and rent < 4000:
    moving = True
elif city == "Washington":
    moving = False
elif city == "Chicago":
    moving = True 
elif rent <= 3000:
    moving = True 
else:
    moving = False
can_or_cannot = "can" if moving else "cannot"
print(f"Sarah {can_or_cannot} move to {city} for {rent}")