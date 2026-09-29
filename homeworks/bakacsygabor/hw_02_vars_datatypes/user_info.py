"""Lista- és szótárműveletek gyakorlása."""


user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": [
        "pizza",
        "carbonara",
        "sushi",
    ],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000",
    },
}


# 1. A split(",") a vesszőkkel elválasztott szöveget listává alakítja.
programming_languages = input(
    "Enter four programming languages separated by commas without spaces: "
).split(",")
user_info["skills"] = programming_languages

# 2. A sort() ábécésorrendbe rendezi az ételeket.
user_info["favourite_meals"].sort()

# 3. A -2 index az utolsó előtti elemet jelenti.
print("Sorted favourite meals:", user_info["favourite_meals"])
print("Second-to-last favourite meal:", user_info["favourite_meals"][-2])

# 4. Az append() hozzáadja a spagettit a lista végéhez.
user_info["favourite_meals"].append("spaghetti")

# 5. A [2:4] kiválasztja a lista harmadik és negyedik elemét.
user_info["favourite_meals"].extend(
    user_info["favourite_meals"][2:4]
)

# 6. A dict.fromkeys() törli a duplikációkat, a sorrend pedig megmarad.
user_info["favourite_meals"] = list(
    dict.fromkeys(user_info["favourite_meals"])
)

# 7. Felcseréljük az első és az utolsó ételt.
favourite_meals = user_info["favourite_meals"]
favourite_meals[0], favourite_meals[-1] = (
    favourite_meals[-1],
    favourite_meals[0],
)

# 8. Hozzáadunk egy új nevet és telefonszámot.
user_info["phone_contacts"]["Anna"] = "+36705551234"

# 9. Töröljük Tim már nem használt telefonszámát.
del user_info["phone_contacts"]["Tim"]

# 10. Peter két telefonszámát egy listában tároljuk.
user_info["phone_contacts"]["Peter"] = [
    "+36305550101",
    "+36305550102",
]

# Extra 1. Az utolsó három nyelvet fordított sorrendben írjuk ki.
print("Last three skills in reverse order:", user_info["skills"][-3:][::-1])

# Extra 2. A pop() átadja Tim2 számát az új Tim kulcsnak, majd törli Tim2-t.
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop(
    "Tim2"
)

print("Final favourite meals:", user_info["favourite_meals"])
print("Final phone contacts:", user_info["phone_contacts"])
