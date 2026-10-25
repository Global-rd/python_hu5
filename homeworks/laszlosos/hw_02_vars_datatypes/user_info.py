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
languages = input("What languages do you know?")
languages = languages.split(",")
print(languages)
print(type(languages))
user_info["skills"] = languages
#abc sorrend
user_info["favourite_meals"].sort()
#utolso elotti elem 
print(user_info["favourite_meals"][-2])
#spagetti hozzaadasa
user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])
#harmadik, negyedik elem ismetelt hozzaadasa 
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print(user_info["favourite_meals"])
#duplikatumok eltavolitasa 
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(user_info["favourite_meals"])
user_info["favourite_meals"].sort() #abcs sorrendbe tettem megint, mert a set radnomizalta 
print(user_info["favourite_meals"])
#elemek felcserelese
temp = user_info["favourite_meals"][0]
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print(user_info["favourite_meals"])
#elem hozzaadasa a phone contact listahoz
user_info["phone_contacts"]["Bob"] = "+31611080109"
print(user_info["phone_contacts"])
#Tim torlese
del user_info["phone_contacts"]["Tim"] 
print(user_info["phone_contacts"])
#uj szemely hozzaadasa ket szammal 
user_info["phone_contacts"]["Anne"] = ["+31643082904", "+31666833910"]
print(user_info["phone_contacts"])
#Extra1
print(user_info["skills"][-3:][::-1])
#Extra2
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print(user_info["phone_contacts"])
