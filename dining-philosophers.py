import threading
import time

class Philosopher(threading.Thread):
    def __init__(self, index, chopsticks, waiter):
        super().__init__()
        self.index = index
        self.chopsticks = chopsticks
        self.waiter = waiter

    def run(self):
        while True:
            # Think
            time.sleep(1)

            # Request waiter's attention
            self.waiter.acquire()

            # Pick up chopsticks
            left_chopstick = self.chopsticks[self.index]
            right_chopstick = self.chopsticks[(self.index + 1) % len(self.chopsticks)]
            left_chopstick.acquire()
            right_chopstick.acquire()

            # Eat
            print(f"Philosopher {self.index} is eating")
            time.sleep(2)

            # Release chopsticks
            left_chopstick.release()
            right_chopstick.release()

            # Release waiter
            self.waiter.release()

if __name__ == "__main__":
    num_philosophers = 8
    chopsticks = [threading.Semaphore(1) for _ in range(num_philosophers)]
    waiter = threading.Semaphore(1)

    philosophers = [Philosopher(i, chopsticks, waiter) for i in range(num_philosophers)]

    for philosopher in philosophers:
        philosopher.start()
