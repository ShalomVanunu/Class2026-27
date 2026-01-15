import time
import threading

def func1():
    print("1")
    time.sleep(1)
    print("2")


def func2():
    print("3")
    time.sleep(1)
    print("4")

start_time = time.perf_counter()


th1 = threading.Thread(target=func1)
th1.start()

th2 = threading.Thread(target=func2)
th2.start()
th2.join()

print(time.perf_counter()-start_time)

