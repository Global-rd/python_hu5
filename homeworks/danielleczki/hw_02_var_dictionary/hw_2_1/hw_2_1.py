


name = input("name: ").strip().upper()
age = int(input("age: "))
python_exp_in_years = int(input("my python experencie in years: "))
what_i_want =  input("Would you like to be a professional python developer?: ")

age_in_days = age * 365

answer = "I want to be professional python developer. " if what_i_want == "yes" else "I dont want to be a professional python developer. "

print(
    f"My age is {age_in_days} days old. "
    f"My name is {name} and mine "
    f"{python_exp_in_years} years experience. "
    f"{answer}"
)
