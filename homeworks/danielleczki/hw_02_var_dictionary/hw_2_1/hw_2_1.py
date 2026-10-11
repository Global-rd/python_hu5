

to_be_developer = "to be a professional python developer"
name = input("name: ").strip().upper()
age = int(input("age: "))
python_exp_in_years = int(input("my python experencie in years: "))
wants_to_be_developer =  input(f"Would you like {to_be_developer}?: ")

age_in_days = age * 365

answer = "want " if wants_to_be_developer == "yes" else "dont want "

print(
    f"My age is {age_in_days} days old. "
    f"My name is {name} and mine "
    f"{python_exp_in_years} years experience. "
    f"I {answer}{to_be_developer}. "
)
