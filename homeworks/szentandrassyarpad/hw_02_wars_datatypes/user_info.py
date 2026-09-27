from pprint import pprint

user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": [
    "pizza",
    "carbonara",
    "sushi"
    ],
    "phone_contacts": {
    "Mary": "+36701234567",
    "Tim": "+36207654321",
    "Tim2": "+36304567321",
    "Jim": "+364005000"
    }
}

# 1.
languages=input('Adj meg 4 programozási nyelvet vesszővel elválasztva szóközök nélkül: ')
user_info.update({'skills':languages.split(',')})

# 2
user_info['favourite_meals'].sort()

# 3
print(user_info['favourite_meals'][-2])
pprint(user_info)

# 4 
user_info['favourite_meals'].append('spaghetti')

# 5
user_info['favourite_meals'].append(user_info['favourite_meals'][2])
user_info['favourite_meals'].append(user_info['favourite_meals'][3])

# 6
user_info['favourite_meals']=list(set(user_info['favourite_meals']))

# 7
tmp_meal=user_info['favourite_meals'][0]
user_info['favourite_meals'][0]=user_info['favourite_meals'][-1]
user_info['favourite_meals'][-1]=tmp_meal

# 8
user_info['phone_contacts'].update({"Columbo":"555 415"})

# 9
user_info['phone_contacts'].pop('Tim')

# 10
user_info['phone_contacts'].update({"Derrick":["+123456", "+78910"]})


# Extra 1

print(user_info['skills'][-3:][::-1])
pprint(user_info)

# Extra 2

user_info['phone_contacts'].update({"Tim":user_info['phone_contacts']['Tim2']})
user_info['phone_contacts'].pop('Tim2')
