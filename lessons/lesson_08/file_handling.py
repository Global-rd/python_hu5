import os
from pathlib import Path

print(os.getcwd())

file_path = Path("lessons") /"lesson_08"/ "sample.txt"

#without context manager

file = open(file_path, "w")

try:
    file.write("This is a sample text")
finally:
    file.close()


#with context manager:
with open(file_path, "w") as file:
    file.write("This is a sample text from a context manager.\n")


with open(file_path, "a") as file:
    file.write("This is a sample text from a context manager in append mode.\n")


with open(file_path, "r") as file:
    lines = file.readlines()
    print(lines)
    print(type(lines))
    for line in lines:
        print(line.strip())



#GENERATOR FUNCTION
print("----------------")


def read_file_line_by_line(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line


for line in read_file_line_by_line(file_path=file_path):
    print(line)




