name=input('Név: ').upper().strip()
age=input('Életkor: ')
python_exp_in_years=input('Python tapasztalat években: ')
age_in_days = int(age)*365

print(f'My character is {age_in_days} old. '+
    f'His/her name is {name} and he/she has {python_exp_in_years}'+
    f' years experience.')


# Extra 
pro_dev_intention=input('Szeretné hogy profi Python fejlesztő legyen? (yes/no): ')

print(f'My character is {age_in_days} old. '+
    f'His/her name is {name} and he/she has {python_exp_in_years}'+
    f' years experience.'+
    f' He/she {'wants' if pro_dev_intention=='yes' else 'does not want'} to be a Python developer!' 
)


