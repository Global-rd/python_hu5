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
#1.feladat
prog_language = list(input("Please list four programming languages.").strip().split(","))
print(prog_language)

#user_info["skills"] = prog_language        első megoldás

user_info.update({"skills": prog_language})
print(user_info)

#2.feladat
user_info["favourite_meals"].sort()
print(user_info)

#3. feladat
print(user_info["favourite_meals"][-2])

#4. feladat
user_info["favourite_meals"].append("spaghetti")

#5. feladat

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print(user_info["favourite_meals"])

#6. feladat
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
user_info["favourite_meals"] = sorted(user_info["favourite_meals"])
#print(user_info["favourite_meals"])

#7. feladat
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(user_info["favourite_meals"])

#8.feladat
user_info["phone_contacts"]["Betti"] = "+3630123456"
print(user_info)

#9.feladat
user_info["phone_contacts"].pop("Tim")

#10.feladat
user_info["phone_contacts"]["Robbie"] = ["061236641", "0630456985"]
print(user_info)

#Extra 1
print(user_info["skills"][:-4:-1])  #miért ír ki 4 db-ot?

#Extra 2
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print(user_info)
