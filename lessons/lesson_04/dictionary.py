from pprint import pprint

student = {
    "name": "Johnny",
    "age": 19,
    "grades": {"grammar": [1,2,3],
               "math": [4,5,5]},
    "major": "Computer science",
    "is_active": True
}

pprint(student)

print(student["name"])
print(student["grades"]["math"][0])


print(type(student["grades"]))

print(student.get("first_name", "N/A"))

print(list(student.keys()))
print(type(student.keys()))

print(student.values())
print(type(student.values()))

student["failed_exams"] = 2
pprint(student)

#---------------------------
latest_grade = int(input("Latest grade: "))

us_grade_mapping = {
    5: "A",
    4: "B",
    3: "C",
    2: "D",
    1: "F"
}

print(us_grade_mapping[latest_grade])