# Threading in Python allows you to perform multiple tasks concurrently, essentially running different parts of your code in parallel. It is useful when you want to execute multiple operations simultaneously and take advantage of multi-core processors.
import threading
import time

# Define a function that will be executed in a separate thread
def print_numbers():
    for i in range(1, 6):
        print(f"Thread 1: {i}")
        time.sleep(0.5)

# Define another function that will be executed in a separate thread
def print_letters():
    for letter in 'ABCDE':
        print(f"Thread 2: {letter}")
        time.sleep(0.5)

# Create two thread objects for our functions
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish before moving on
thread1.join()
thread2.join()

print("Done!")

# In this example, we have two functions print_numbers and print_letters, which will be executed in separate threads. Each function has a loop that prints some output and then sleeps for 1 second.

# We create two threading.Thread objects, thread1 and thread2, specifying the target function for each thread. We then start both threads using the start() method.

# After starting the threads, we call the join() method on each thread to wait for them to finish execution. This ensures that the main thread (the one executing the rest of the code) waits for the two threads to complete before printing "Done!".

# When you run this code, you'll see the numbers and letters being printed simultaneously, demonstrating the concurrent execution of the two threads.

# Remember, the output order may vary between runs since threads run independently and their execution order is not guaranteed.