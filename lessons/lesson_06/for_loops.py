import time

songs = ["Warrior", "Meet your maker", "End the transmission", "I'm still fine"]

for song in songs:
    print(f"Playing {song}")
    #time.sleep(2)

print("test")

student = {"name": "John",
           "age": 15, 
           "spec": "CS"}

for student_key, student_value in student.items():
    print(f"Key: {student_key}, value: {student_value}")


for k in student.keys():
    print(k)

for v in student.values():
    print(v)


#range looping

for number in range(0, 11):
    print(number)