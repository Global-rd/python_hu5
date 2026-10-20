import time
import threading


def task1():
    print("Task 1 starting...")
    time.sleep(3)
    print("Task 1 finsihed...")

def task2():
    print("Task 2 starting...")
    time.sleep(2)
    print("Task 2 finsihed...")


print("running on multiple threads")

thread_1 = threading.Thread(target=task1)
thread_2 = threading.Thread(target=task2)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print("test")


