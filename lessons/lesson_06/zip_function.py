students = ["Alice", "Bob", "Dexter"]
points = [99, 98, 97]


for person, score in zip(students, points):
    print(f"{person} has scored {score} points")
