
# Név bekérése és formázása
name = input("Enter name: ").strip().title()

# Életkor bekérése és konvertálása
age = int(input("Enter age: "))

# Python tapasztalat bekérése
python_exp_years = int(input("Enter Python experience in years: "))

# Életkor napokban
age_in_days = age * 365

# Szorgalmi
wants_python_dev = input(
"Do you want to be a professional Python developer? (yes/no): "
).strip().lower()

developer_text = (
    "wants"
    if wants_python_dev == "yes"
    else "does not want"
)

print(
    f"My character is {age_in_days} old. "
    f"His/her name is {name} and he/she has "
    f"{python_exp_years} years experience. "
    f"He/she {developer_text} to be a Python developer!"
)