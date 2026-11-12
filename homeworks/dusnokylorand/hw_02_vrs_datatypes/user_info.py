user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": [
        "pizza",
        "carbonara",
        "sushi"
    ],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000"
    }
}
skills_input = input(
    "Enter 4 programming languages separated by commas: "
)
user_info["skills"] = skills_input.split(",")

user_info["favourite_meals"].sort()

print(user_info["favourite_meals"][-2])

user_info["favourite_meals"].append("spaghetti")

user_info["favourite_meals"].extend(
    user_info["favourite_meals"][2:4]
)

user_info["favourite_meals"] = list(
    dict.fromkeys(user_info["favourite_meals"])
)

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = (
    user_info["favourite_meals"][-1],
    user_info["favourite_meals"][0]
)

user_info["phone_contacts"]["John"] = "+36123456789"

del user_info["phone_contacts"]["Tim"]

user_info["phone_contacts"]["Peter"] = [
    "+36701111111",
    "+36302222222"
]

print(user_info["skills"][-3:][::-1])

user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

print(user_info)
