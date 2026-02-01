
# in order to use random numbers
import random

random.seed(12)

# bring me an integer random number between 1-10
number: int = random.randint(1, 10)  # inclusive between 1-10

# is range inclusive ? no

print(number)

# random float between 0-0.999
float_rnd = random.random()
print(float_rnd)

# create integer random number between 1-10 using random.random()
for _ in range(10):
    print(int(10 * random.random()) + 1, end=" ")

print()

# random float between 5.0-10.0
print(random.uniform(5, 10))

# random between choices: [1, 3, 5, None, -2, 7]
for _ in range(10):
  print(random.choice([1, 3, 5, None, -2, 7]), end = " ")

print()
print(random.choice(["hello", "world", "python", "c++"]))

word = random.choice(["hello", "world", "python", "c++"])

# took all numbers from this range: for _ in range(3, 30 + 3, 3)  [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# identical to random.choice([3, 6, 9, 12, 15, 18, 21, 24, 27, 30])
print(random.randrange(3, 30 + 3, 3))

# sample
print(random.sample( range(1, 10), 5))


# 1 roll a dice and print the number (1-6) using randint
# 2 generate a random number between 20-200 using randint
# 3 generate 8 numbers between 10 and 20 using sample
# 4 generate a random amount of numbers (between 1-4) of multiples of 3 between 12-48
print(random.sample(range(12, 48 + 3, 3), random.randint(1, 4)))

# 5 choose a random color between "red" "green" "blue" "orange" "white"
# 6 input 3 numbers from the user , then choose randomly 1 of the numbers
# 7 choose a random temperature between 35.0-37.5 using uniform
print(f"{random.uniform(35.0, 37.5):.1f}")

