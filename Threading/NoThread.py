import threading
import time


def func1():
    print("1")
    time.sleep(1)
    print("2")


def func2():
    print("3")
    time.sleep(1)
    print("4")

start_time = time.perf_counter()

func1()
func2()

print(time.perf_counter()-start_time)
