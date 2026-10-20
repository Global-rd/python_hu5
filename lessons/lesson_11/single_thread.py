import time

def task1():
    print("Task 1 starting...")
    time.sleep(3)
    print("Task 1 finsihed...")

def task2():
    print("Task 2 starting...")
    time.sleep(2)
    print("Task 2 finsihed...")

#running on a single thread

print("single threaded execution")
task1()
task2()