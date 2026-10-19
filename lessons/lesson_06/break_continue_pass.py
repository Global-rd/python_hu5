#BREAK

attempts = 0

while attempts < 3:
    password = input("Enter your password: ")
    if password == "secret":
        print("Access granted!")
        break
    else:
        print("Wrong password, try again!")
    attempts += 1

#CONTINUE

number = 0

while number < 10:
    #number += 1
    if number % 2 == 0:
        continue
    print(f"Processing number {number}")


#PASS

numbers = [1,2,3,4]

for num in numbers:
    pass
