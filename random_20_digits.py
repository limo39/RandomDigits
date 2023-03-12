import random

# Generate a random 20-digit number
number = ''.join([str(random.randint(0, 9)) for _ in range(20)])

print(number)
