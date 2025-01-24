import numpy as np

# Numpy Sign Function Example
# This script demonstrates the use of the numpy.sign function to compute the sign of each element in a dataset.

# Input data
data = (163, 165, 162, 189, 161, 171, 158, 151, 169,
        182, 163, 139, 172, 165, 148, 166, 172, 163, 187, 173)

# Compute the sign of each element in the data
# numpy.sign returns:
# - 1 for positive numbers
# - -1 for negative numbers
# - 0 for zeros
result = np.sign(data)

# Output the result
print("Input data:", data)
print("Sign of data elements:", result)
