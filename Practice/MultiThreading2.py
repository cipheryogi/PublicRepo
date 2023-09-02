import threading
import time

# Define a function that will be executed in a thread
def count_up():
    for i in range(5):
        print(f"[{time.strftime('%H:%M:%S')}] Counting up: {i}")
        time.sleep(0.5)

# Define another function that will be executed in a separate thread
def count_down():
    for i in range(5, 0, -1):
        print(f"[{time.strftime('%H:%M:%S')}] Counting down: {i}")
        time.sleep(0.5)

# Create two thread objects for our functions
thread1 = threading.Thread(target=count_up)
thread2 = threading.Thread(target=count_down)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish before moving on
thread1.join()
thread2.join()

print("Done!")
