# Synchronization-between-multiple-threads.

# Explanation of the code: 

Only one thread can acquire the semaphore at a time because it is created with a value of 1. A thread enters a critical area and is able to run code that shouldn't be stopped by another thread when it gains the semaphore. The semaphore is released after the thread is finished, allowing the other thread to pick it up and enter the crucial part.

Each thread in this example obtains the semaphore, reaches the  critical section, and then sleeps for two seconds. By doing so, a lengthy task that shouldn't be interrupted by another thread is simulated. The try-finally block is used to ensure that the semaphore is always released, even if an exception is raised in the critical section.

# Output of the code :

![image](https://user-images.githubusercontent.com/92660593/212483923-6d94a757-46a0-4f88-8a72-aff70fdc4315.png)
