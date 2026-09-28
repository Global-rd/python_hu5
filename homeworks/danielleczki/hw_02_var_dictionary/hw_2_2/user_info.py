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


# 1. Programozási nyelvek bekérése
programming_languages = input(
    "Adj meg 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül: "
)

# A kapott string átalakítása listává
programming_languages = programming_languages.split(",")

# A lista hozzáadása a dictionary-höz "skills" néven
user_info["skills"] = programming_languages


# 2. favourite_meals rendezése ABC szerint
user_info["favourite_meals"].sort()


# Eredmény kiírása
print(user_info)

print(user_info["favourite_meals"][-1])
user_info["favourite_meals"].append("spagetti")
print(user_info["favourite_meals"])
input()