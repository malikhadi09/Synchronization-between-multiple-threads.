#NAME MALIK ABDUL HADI
#REG NO : 200901053
#COURSE: OPERATING SYSTEM LAB
#SUBMITTED TO : MADAM REEDA

#Question 2:
#Program to process synchronization using semaphores.

import threading
import time

# Creating a semaphore with a value of 1
semaphore = threading.Semaphore(1)

def Thread1():
    print("Thread 1 is acquiring semaphore")
    # Acquire the semaphore
    semaphore.acquire()
    try:
        # Critical section
        print("Thread 1 is in the critical section")
        time.sleep(2)
    finally:
        # Release the semaphore
        print("Thread 1 is releasing semaphore")
        semaphore.release()

def Thread2():
    print("Thread 2 is acquiring semaphore")
    # Acquire the semaphore
    semaphore.acquire()
    try:
        # Critical section
        print("Thread 2 is in the critical section")
        time.sleep(2)
    finally:
        # Release the semaphore
        print("Thread 2 is releasing semaphore")
        semaphore.release()

thread1 = threading.Thread(target=Thread1)
thread2 = threading.Thread(target=Thread2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Finished Both the threads.")