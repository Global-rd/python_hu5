"Sarah"

city = input("where do you want living sarah?: ")
cost = int(input("how much can you pay for it?: "))
cities = {
    "liked" : [" New York", "San Fransisco"],
    "hate" : ["Washington"],
    "love" : ["Chicago"]
}

if city in cities["liked"] and  cost < 4000:
    print(f"I pay {cost}USD for this {city}")
if city in cities["hate"]:
    print("Nem költözik Sarah")
if city in cities["love"]:
        print(f"{city}-ba költözik Sarah")
elif  cost <= 3000:
    print(f"{city}-ba költözik Sarah")
    

else:
    print("Nem költözik Sarah")