import math

# Quantile Calculation Script
# This script calculates the p-th quantile for a given sorted list of values.

# Input data
data = [0.11, 0.14, 0.16, 0.19, 0.26, 0.28, 0.33, 0.38, 0.38, 0.52, 0.58, 0.62,
        0.63, 0.76, 0.86, 0.87, 0.88, 0.91, 0.92, 0.94, 0.95, 1.01, 1.15, 1.15, 1.19, 1]

# Ensure the data is sorted
data = sorted(data)
print("Sorted data:", data)

# Desired quantile (e.g., 70th percentile)
p = 0.7
n = len(data)

# Calculate the rank
rank = math.floor((n + 1) * p)
print("Rank (r):", rank)

# Calculate the weight
weight = (n + 1) * p - rank
print("Weight (w):", weight)

# Calculate the quantile
quantile = (1 - weight) * data[rank - 1] + weight * data[min(rank, n - 1)]
print(f"The {p * 100:.0f}th percentile (quantile) is:", quantile)
