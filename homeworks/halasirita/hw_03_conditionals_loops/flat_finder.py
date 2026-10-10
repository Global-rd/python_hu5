city = input("Enter city name: ").strip().title()

rent = int(input("Enter rent (USD): "))

decision = "not "

if city == "Washington":
    decision = "not "

elif city == "Chicago":
    decision = ""

elif city in ["New York", "San Francisco"] and rent < 4000:
    decision = ""

elif city in ["New York", "San Francisco"] and rent >= 4000:
    decision = "not "

elif rent < 3000:
    decision = ""

else:
    decision = "not "

text = f"Sarah would {decision}move to {city} if the rent costs ${rent}."
print(text)
