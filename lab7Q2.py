import random
import math
import matplotlib.pyplot as plt

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to separate primes and composites
def separate_prime_composite(numbers):
    primes = []
    composites = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
        elif num > 1:  # Only positive integers > 1 can be composite
            composites.append(num)
    return primes, composites

# Get user input
K = int(input("Enter the number of random numbers (K, minimum 10): "))
while K < 10:
    K = int(input("Please enter a value for K that is 10 or more: "))

N = int(input("Enter the upper limit (N): "))

# Generate K random numbers within the limit N
random_numbers = random.sample(range(1, N+1), K)
print("Generated random numbers:", random_numbers)

# Separate prime and composite numbers
primes, composites = separate_prime_composite(random_numbers)

# Calculate squares of primes and square roots of composites
prime_squares = [p ** 2 for p in primes]
composite_sqrt = [math.sqrt(c) for c in composites]

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Scatter plot for primes and their squares
ax1.scatter(primes, prime_squares, color='blue', marker='o')
ax1.set_title("Prime Numbers vs Their Squares")
ax1.set_xlabel("Prime Numbers")
ax1.set_ylabel("Square of Prime Numbers")

# Scatter plot for composites and their square roots
ax2.scatter(composites, composite_sqrt, color='red', marker='x')
ax2.set_title("Composite Numbers vs Their Square Roots")
ax2.set_xlabel("Composite Numbers")
ax2.set_ylabel("Square Root of Composite Numbers")

plt.tight_layout()
plt.show()
