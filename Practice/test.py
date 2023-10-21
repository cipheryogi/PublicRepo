
import time

def looper():
    def func(x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return func(x-1) + func(x-2)

    for x in range(10):
        time.sleep(0.5)
        print(func(x))

print(looper())
