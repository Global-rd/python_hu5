# Decide whether based on the provided inputs (city, monthly rent) Sarah would rent the flat
import os
os.system("cls")

city = input("Enter the city where you wanna rent: ")
rent = float(input("Enter the monthly rent: "))

if city == "Chicago":
    print(f"Sarah would be so happy to rent the flat in {city} for a monthly rent of ${rent}.")
elif city in ["New York", "San Francisco"] and rent < 4000:
    print(f"Sarah would gladly rent the flat in {city} for a monthly rent of ${rent}.")
elif city != "Washington" and rent <= 3000:
    print(f"Sarah would be okay to rent the flat in {city} for a monthly rent of ${rent}.")
else:
    print(f"Sarah wouldn't rent the flat in {city} for a monthly rent of ${rent}.")