flat_location = input("Enter the flat location: ")
flat_price = float(input("Enter the flat price (USD): "))

if flat_location == "Chicago":
    print("Flat found in Chicago! I'm moving!")
elif (flat_location == "New York" or flat_location == "San Francisco") and flat_price < 4000:
    print(f"Flat found in {flat_location} under $2000! I'm moving!")
elif flat_location == "Washington":
    print("NO WAY! I'm not moving to Washington!")
elif flat_price < 3000: 
    print(f"Flat found in {flat_location} under $3000! I'm moving!")
else:
    print(f"Flat found in {flat_location} but it's too expensive! I'm not moving!") 