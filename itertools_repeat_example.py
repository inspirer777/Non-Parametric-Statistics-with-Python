import itertools
import numpy as np

# Itertools Repeat Example
# This script demonstrates the use of itertools.repeat to repeat elements multiple times.

# Repeat the number 1 four times
print("Repeating 1 four times:")
for n1 in itertools.repeat(1, 4):
    print(np.array([n1]))

# Repeat the number 2 three times
print("Repeating 2 three times:")
for n2 in itertools.repeat(2, 3):
    print(np.array([n2]))

# Repeat the number 3 three times
print("Repeating 3 three times:")
for n3 in itertools.repeat(3, 3):
    print(np.array([n3]))

# Demonstrating the repeat object
a = itertools.repeat(1, 4)  # Create a repeat object for the number 1 repeated four times
print("Repeat object (a):", list(a))  # Convert the repeat object to a list and print
