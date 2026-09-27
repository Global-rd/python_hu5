# --- Feladat 1: fictive character ---
 
# User input: strip() removes leading/trailing spaces, upper() makes it uppercase
character_name = input("Name: ").strip().upper()
 
# Type conversion: input() always returns a string
age_in_years = int(input("Age (years): "))
python_exp_in_years = float(input("Python experience (years): "))
 
# Age in days, rounded (365.25 accounts for leap years; assume today is the birthday)
age_in_days = round(age_in_years * 365.25)
 
# Extra: ternary operator
wants_to_be_pro = input("Should your character be a pro Python developer? (yes/no): ").strip().lower()
pro_dev_sentence = (
    "He/she wants to be a Python developer!"
    if wants_to_be_pro == "yes"
    else "He/she does not want to be a Python developer!"
)
 
# f-string output (:g drops the trailing .0 from whole numbers, e.g. 3.0 -> 3)
print(
    f"My character is {age_in_days} days old. His/her name is {character_name} "
    f"and he/she has {python_exp_in_years:g} years experience. {pro_dev_sentence}"
)
