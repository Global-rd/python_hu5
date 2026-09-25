# Feladat 1:
# A megoldasomban feleslegesnek tünö kikommentelesek vannak. Ennek oka a megoldas evolucioja, lepesröl lepesre. Nem akartam kitörölni, ezert csak kikommentaltam.

# Valtozok definialasa

fictive_character_name = input("What is your name? ")
#fictive_character_age = "What is your age? " -> kikommentelve, mert kesöbb az inputtal felülirom
#fictive_character_python_experience = "How many years of experience you have with Python?" -> kikommentelve, mert kesöbb az inputtal felülirom

# Valtozok formatalasa

#fictive_character_name = fictive_character_name.upper() -> nagybetüs
#print(fictive_character_name) -> check point
fictive_character_name = fictive_character_name.strip().upper() #nagybetüs ês szoköz se elötte, se utana
#print(fictive_character_name) -> check point
#print(len(fictive_character_name)) -> check point, hogy a strip müködik-e

fictive_character_age = int(input("What is your age? "))
#print(fictive_character_age) -> check point

fictive_character_age_days = fictive_character_age * 365
#print(fictive_character_age_days) -> check point

fictive_character_python_experience = int(input("How many years of experience you have with Python? "))
#print(fictive_character_python_experience) -> check point

# Az eredmeny nyomtatasa -> kikommentelve, mert a szorgalmiban ujra kiirja.
#print(f"My character is {fictive_character_age_days} days old. Her name is {fictive_character_name} and she has {fictive_character_python_experience} years of experience with Python.")

# Extra feladat
fictive_character_ambition = input("Would you like to become a Python developer (yes/no)? ")

""""
fictive_character_ambition_answer = {
    "yes": "She wants to become a Python developer",
    "no": "She does not want to become a Python developer."
}

print(f"My character is {fictive_character_age_days} days old. Her name is {fictive_character_name} and she has {fictive_character_python_experience} years of experience with Python. fictive_character_ambition_answer[fictive_character_ambition]")
""" #ez a megoldas probalta az inputot lekorlatozni egy dictionary-vel, de nem ez volt a feladat, ezert kikommentaltam.

"""
if fictive_character_ambition == "yes":print(f"My character is {fictive_character_age_days} days old. Her name is {fictive_character_name} and she has {fictive_character_python_experience} years of experience with Python. She wants to become a Python developer.")
else: print(f"My character is {fictive_character_age_days} days old. Her name is {fictive_character_name} and she has {fictive_character_python_experience} years of experience with Python. She does not want to become a Python developer.")
""" #ez a megoldas vegül egy sima if-else lett, ezert kikommentaltam.

fictive_character_ambition_answer = (
    "She wants to become a Python developer"
    if fictive_character_ambition == "yes"
else "She does not want to become a Python developer."
)
# Az eredmeny nyomtatasa
print(f"My character is {fictive_character_age_days} days old. Her name is {fictive_character_name} and she has {fictive_character_python_experience} years of experience with Python. {fictive_character_ambition_answer}")








    