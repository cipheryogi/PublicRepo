# Thread synchronization in Python involves coordinating the execution of multiple threads to ensure they access shared resources or critical sections of code in an orderly and controlled manner. A common synchronization mechanism in Python is the Lock object provided by the threading module. It allows threads to acquire and release locks to control access to shared resources. Here's a simple example to illustrate threading synchronization using a Lock:
import threading

# Shared variable
counter = 0

# Create a lock object
lock = threading.Lock()

# Define a function that will be executed in a thread
def increment():
    global counter
    for _ in range(100000):
        # Acquire the lock before accessing the shared variable
        lock.acquire()
        counter += 1
        # Release the lock after modifying the shared variable
        lock.release()

# Create two thread objects for our function
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish before moving on
thread1.join()
thread2.join()

print("Counter:", counter)
