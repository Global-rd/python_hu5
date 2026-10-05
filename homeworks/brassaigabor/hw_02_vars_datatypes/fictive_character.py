#-----------------------#
# HomeWork lessons 4 /1 #
#-----------------------#

"""
person_full_name = input("Name:")
person_age = input("Age (in years):")
person_python_exp = input("Python axperience:")
"""

person = {"full_name": input("Name:").strip().upper(),
          "age":       (int(input("Age:")) * 365),
          "python_exp": input("Python experience:")
          }

print(f"My character is {person["age"]} old. His/her name is {person["full_name"]} and he/she has {person["python_exp"]} years experience.")

# ------------ #
# Extra
# ------------ #

#print(f"My character is {person["age"]} old. His/her name is {person["full_name"]} and he/she has {person["python_exp"]} years experience. He/she wants to be a Python developer!") if input("Would you like an expert Python coder? (\"yes/no\")") == "yes" else print(f"My character is {person["age"]} old. His/her name is {person["full_name"]} and he/she has {person["python_exp"]} years experience. He/she does not want to be a Python developer!")
dev_intention = "wants" if input('Would you like an expert Python coder? ("yes/no")') == "yes" else "does not want"
print(f"My character is {person['age']} old. His/her name is {person['full_name']} and he/she has {person['python_exp']} years experience. He/she {dev_intention} to be a Python developer!")