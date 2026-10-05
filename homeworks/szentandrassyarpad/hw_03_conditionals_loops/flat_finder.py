city=input('City: ')
rent=int(input('Rent: '))
can_move=False

if  (city in['New York', 'San Francisco'] and (rent < 4000)):
    can_move=True
elif city=='Washington':
    can_move=False
elif city=='Chicago':
    can_move=True
elif rent<=3000:
    can_move=True

print(f"Sarah can{'' if can_move else ' not' } move into {city} for {rent} $")
