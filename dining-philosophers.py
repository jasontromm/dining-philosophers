import threading
import time
import random

# Number of philosophers and chopsticks
NUM_PHILOSOPHERS = 8
EATING_LIMIT = 3

# Semaphore for chopsticks
chopsticks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]

# Mutex for waiter
waiter = threading.Semaphore(NUM_PHILOSOPHERS - 1)

# Track how many times each philosopher has eaten
times_eaten = [0] * NUM_PHILOSOPHERS

def philosopher(philosopher_id):
    global times_eaten

    while times_eaten[philosopher_id] < EATING_LIMIT:
        # Think
        print(f"Philosopher {philosopher_id} is thinking.")
        time.sleep(random.uniform(1, 3))

        # Wait for waiter's attention
        waiter.acquire()

        # Pick up chopsticks
        left = philosopher_id
        right = (philosopher_id + 1) % NUM_PHILOSOPHERS

        chopsticks[left].acquire()
        chopsticks[right].acquire()

        # Eat
        print(f"Philosopher {philosopher_id} is eating.")
        time.sleep(random.uniform(1, 2))
        times_eaten[philosopher_id] += 1

        # Put down chopsticks
        chopsticks[left].release()
        chopsticks[right].release()

        # Release waiter's attention
        waiter.release()

    print(f"Philosopher {philosopher_id} has finished eating.")

# Create and start threads
threads = []
for i in range(NUM_PHILOSOPHERS):
    thread = threading.Thread(target=philosopher, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All philosophers have finished eating.")

