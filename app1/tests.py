import threading
import time

def function1(param):
    print(f"Function 1 starting with param {param}...")
    time.sleep(2)  # Simulate some work
    result = param * 2
    print(f"Function 1 finished. Result: {result}")
    return result

def function2(param):
    print(f"Function 2 starting with param {param}...")
    time.sleep(3)  # Simulate some work
    result = param * 3
    print(f"Function 2 finished. Result: {result}")
    return result

# Create Thread objects
param1 = 5
param2 = 3
thread1 = threading.Thread(target=function1, args=(param1,))
thread2 = threading.Thread(target=function2, args=(param2,))

# Start threads
thread1.start()
thread2.start()

# Join threads and retrieve results
thread1.join()
thread2.join()

result1 = thread1.result
result2 = thread2.result

print("Results:", result1, result2)
