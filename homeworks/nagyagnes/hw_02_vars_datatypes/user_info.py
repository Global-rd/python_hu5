from pprint import pprint
 
# Feladat 2: List és dictionary műveletek használata
 
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
 
print("Felhasználó adatai:")
pprint(user_info)
 
# --- 1 ---
languages = input("Írj be 4 programozási nyelvet, vesszővel, szóköz nélkül: ")
user_info["skills"] = languages.split(",")
print("1. skills:", user_info["skills"])
 
# --- 2 ---
user_info["favourite_meals"].sort()
print("2. ABC sorrend:", user_info["favourite_meals"])
 
# --- 3 ---
print("3. utolsó előtti elem:", user_info["favourite_meals"][-2])
 
# --- 4 ---
user_info["favourite_meals"].append("spaghetti")
print("4. + spaghetti:", user_info["favourite_meals"])
 
# --- 5 ---
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print("5. 3. és 4. elem újra:", user_info["favourite_meals"])
 
# --- 6 ---
user_info["favourite_meals"]=list(set(user_info["favourite_meals"]))
print("6. duplikátumok nélkül:", user_info["favourite_meals"])

# itt felborul a sorrend a set miatt
 
# --- 7 ---
meals = user_info["favourite_meals"]
meals[0], meals[-1] = meals[-1], meals[0]
print("7. első-utolsó csere:", user_info["favourite_meals"])
 
# --- 8 ---
user_info["phone_contacts"]["Agnes"] = "+36701112233"
print("8. új kontakt (Agnes):", user_info["phone_contacts"])
 
# --- 9 ---
del user_info["phone_contacts"]["Tim"]
print("9. Tim törölve:", user_info["phone_contacts"])
 
# --- 10 ---
user_info["phone_contacts"]["Tunde"] = ["+36201234567", "+36309876543"]
print("10. 2 számos kontakt (Tunde):", user_info["phone_contacts"])