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

# getting the skills from the user
user_skills = input("Enter your 4 programming skills (comma-separated, no spaces): ")
# transform the string into a list
user_skills_list = user_skills.split(",")
user_info["skills"] = user_skills_list
# ordering meals alphabetically
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"][-2])  # print the second last meal in the list
user_info["favourite_meals"].append("spaghetti")  # add a new meal to the list
# Adding two new meals to the list
user_info["favourite_meals"].extend(["gulyás", "pálinka"])
# removing duplicates
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
# swaopping the first and last elements of the list using tuple
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
# adding a new contact to the dictionary
user_info["phone_contacts"].update({"John": "+36123456789"})  
# remove Tim, he's not alive (or the contact is not valid anymore, who knows)
user_info["phone_contacts"].pop("Tim")
# adding a new contact with multiple phone numbers
user_info["phone_contacts"].update({"Double David": ["+36 20 111 2222", "+36 70 333 4444"]})
"""
OK, this solution annoys me a bit. :) So I googled... Here's two numbers with more info.
user_info["phone_contacts"].update({
    "Double David": {
        "mobile": "+36 20 111 2222",
        "work": "+36 70 333 4444",
    }
})
There's still a solution that adds this contact twice with different numbers. I think best solution is based on what I want to do later. 
"""
# extra task 1
print(user_info["skills"][:-4:-1])  
# extra task 2
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"]["Tim2"]
