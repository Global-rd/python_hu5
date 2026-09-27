v_name=input('Név: ').upper().strip()
v_age=input('Életkor: ')
v_python_exp_in_years=input('Python tapasztalat években: ')
v_age_in_days = int(v_age)*365

print(f'My character is {v_age_in_days} old. '+
    f'His/her name is {v_name} and he/she has {v_python_exp_in_years}'+
    f' years experience.')


# Extra 
v_profi=input('Szeretné hogy profi Python fejlesztő legyen? (yes/no): ')

print(f'My character is {v_age_in_days} old. '+
    f'His/her name is {v_name} and he/she has {v_python_exp_in_years}'+
    f' years experience.'+
    (' He/she wants to be a Python developer!' if v_profi=='yes' else 'He/she does not want to be a Python developer!'))


    




















