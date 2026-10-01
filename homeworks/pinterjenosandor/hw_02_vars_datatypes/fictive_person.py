""""
My 2nd homework, fictive person
The birtday of the fictive person is today
"""

#Text prep for input fictive person
txt_in_name = ("Please add a name: ")
txt_in_experience = ("add python experience in years: ")

#show today
import datetime
print(f"{"Date: "}{datetime.date.today()}")
#fictive person data input

#name input
name1 = input(txt_in_name)
"""
Modify name
remove the spaces from the begining and the end from name,
the tittle is change the first and last name first character to capital
"""
name_moded = name1.strip().title()
#age input of person
age = int(input(f"{"add "}{name_moded}{"'s age: "}"))
#counting the fictive person age in days
age_in_days = age * 365
#the person python experience input in years, integer type convert
experience = int(input(txt_in_experience))
#person wanna pro python developer question
python_dev = input(f"{"You want "}{name_moded}{" to be a professional python developer?: "}")
#pro result
ok_result = ("He/she wants to be a Python developer!")
ng_result = ("He/she does not want to be a Python developer!")
extra = ok_result if python_dev == "yes" else ng_result
#show result
print(f"{"My character is "}{age_in_days}{" days old. "}")
print(f"{"His/her name is "}{name_moded}{" and he/she has "}{experience}{" years python experience."}")
print(extra)
