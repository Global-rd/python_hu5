
# Homework 03 - Task 1
# Flat Finder - Simon David

# Asking the user for apartment information
city = input("Enter the city: ").strip().lower()

# Validating the monthly rent
while True:
    try:
        rent = float(input("Enter the monthly rent in USD: "))

        if rent < 0:
            print("Rent cannot be negative. Please try again.")
        else:
            break

    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Checking Sarah's preferences
if city == "washington":
    can_move = False

elif city == "chicago":
    can_move = True

elif city in ("new york", "san francisco", "san fransisco"):
    can_move = rent < 4000

else:
    can_move = rent <= 3000

# Displaying the result using an f-string
if can_move:
    print(
        f"Sarah would move to {city.title()} "
        f"for ${rent:.2f} per month."
    )
else:
    print(
        f"Sarah would NOT move to {city.title()} "
        f"for ${rent:.2f} per month."
    )
