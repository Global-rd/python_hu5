#list és dictionary műveletek használata

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
        "Jim": "+364005000"
    }
}


#Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva, 
#szóközök nélkül. Konvertáld a kapott stringet egy listává, és add hozzá 
#a fenti dictionary-hez “skills” néven. 

languages_lists = input("Kérlek, adj meg 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül: ")
skills = languages_lists.split(",")
user_info.update({"skills": skills})

print(user_info)

#Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.

user_info["favourite_meals"].sort()

print("2. favourite_meals ABC:")
print(user_info["favourite_meals"])

#Printeld ki a favourite_meals lista utolsó előtti elemét 

print(user_info["favourite_meals"][-2])

#Adj hozzá egy “spaghetti” string-et ugyanehhez a listához. 

user_info["favourite_meals"].append("spaghetti")

print(user_info["favourite_meals"])

#Add hozzá a favourite_meals-hez az aktuális favourite_meals lista 
#harmadik és negyedik elemét (nem az index-ét) újra. 

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

print(user_info["favourite_meals"])

#Ezután töröld az így keletkezett duplikátumokat!

user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

print(user_info["favourite_meals"])

#Cseréld fel a favourite_meals lista első és utolsó elemét!

user_info["favourite_meals"][0],user_info["favourite_meals"][-1] = (
    user_info["favourite_meals"][-1],
    user_info["favourite_meals"][0]
)

print(user_info["favourite_meals"])

#A “phone_contacts” dictionary-hez adj hozzá egy új elemet, 
#tetszőleges névvel és telefonszámmal. 

user_info["phone_contacts"]["Beam"] = "+36201234567"

print(user_info["phone_contacts"])

#Tim és Tim2 ugyanazt az embert reprezentálják a 
#“phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám 
#már nem él. Töröld ki a telefonkönyvből!

del user_info["phone_contacts"]["Tim"]

print(user_info["phone_contacts"])

#Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 
#telefonszáma is van!

user_info["phone_contacts"]["Ben"] = ["+36704774774", "+36303233322"]

print(user_info["phone_contacts"])









