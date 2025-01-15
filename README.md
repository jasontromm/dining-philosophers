Here’s the Python program to solve the Dining Philosophers problem with 8 philosophers, 8 chopsticks, and a mutex (as the waiter). Each philosopher eats three times before the program ends:

### Explanation:
1. **Chopsticks:** Each chopstick is represented as a semaphore.
2. **Waiter:** The mutex (`waiter`) ensures that at most `NUM_PHILOSOPHERS - 1` philosophers are trying to eat simultaneously, avoiding deadlock.
3. **Philosophers:** Each philosopher alternates between thinking and eating.
4. **Eating Limit:** The program terminates once all philosophers have eaten 3 times.
5. **Threading:** Each philosopher is simulated using a thread.

### How It Works:
- Philosophers think for a random amount of time.
- They wait for the waiter's permission to proceed.
- They pick up their two adjacent chopsticks and eat.
- After eating, they put down the chopsticks and release the waiter's permission.

This ensures no deadlock, as at least one philosopher will always be able to proceed.

