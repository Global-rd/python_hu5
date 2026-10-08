# --- Feladat 2: list and dictionary operations ---
 
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
 
# 1. Ask for 4 programming languages (comma-separated, no spaces) -> list -> "skills"
languages_input = input("Enter 4 programming languages separated by commas (no spaces): ")
user_info["skills"] = languages_input.split(",")
print("1. skills:", user_info["skills"])
 
# 2. Sort favourite_meals alphabetically (ascending)
user_info["favourite_meals"].sort()
print("2. sorted:", user_info["favourite_meals"])
 
# 3. Print the second-to-last element
print("3. second-to-last:", user_info["favourite_meals"][-2], "|", user_info["favourite_meals"])
 
# 4. Append "spaghetti"
user_info["favourite_meals"].append("spaghetti")
print("4. with spaghetti:", user_info["favourite_meals"])
 
# 5. Add the current 3rd and 4th elements (indexes 2 and 3) again
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print("5. with duplicates:", user_info["favourite_meals"])
 
# 6. Remove duplicates, keeping the original order
#    (set() would also dedupe, but it does not preserve order)
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
print("6. deduplicated:", user_info["favourite_meals"])
 
# 7. Swap the first and last elements (tuple unpacking)
meals = user_info["favourite_meals"]
meals[0], meals[-1] = meals[-1], meals[0]
print("7. swapped:", meals)
 
# 8. Add a new contact to phone_contacts
user_info["phone_contacts"]["Anna"] = "+36309876543"
print("8. new contact:", user_info["phone_contacts"])
 
# 9. Tim's old number is dead -> delete the "Tim" key
del user_info["phone_contacts"]["Tim"]
print("9. Tim deleted:", user_info["phone_contacts"])
 
# 10. Add a person with 2 phone numbers (value is a list)
user_info["phone_contacts"]["Peter"] = ["+36201112233", "+36704445566"]
print("10. two numbers:", user_info["phone_contacts"])
 
# Extra 1: last 3 elements of skills in reverse order
print("Extra 1:", user_info["skills"][-3:][::-1], "|", user_info["skills"])
 
# Extra 2: rename Tim2 -> Tim (pop returns the value and removes the old key)
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print("Extra 2:", user_info["phone_contacts"])
