import numpy as np
import scipy.stats

# Paired Binomial Test Script
# This script compares two paired datasets using a binomial test.

# Input data
a = np.array([75, 69.8, 85.7, 74, 69, 83.3, 68.9, 77.8, 72.2, 77.4])
b = np.array([85.4, 83.1, 80.2, 74.5, 70, 81.5, 75.4, 78, 85.4, 80.4])

# Calculate paired differences
d = b - a
d = d[d != 0]  # Remove zero differences
print("Differences (d):", d)

# Calculate key statistics
n = len(d)  # Number of non-zero differences
print("Number of non-zero differences (n):", n)

B = len(d[d > 0])  # Count of positive differences
print("Count of positive differences (B):", B)

# Perform binomial test
# l1: CDF for B
# l2: Complement CDF for B-1
l1 = scipy.stats.binom.cdf(B, n, 0.5)
l2 = 1 - scipy.stats.binom.cdf(B - 1, n, 0.5)

# Two-tailed p-value
pval = 2 * min(l1, l2)
print("P-value:", pval)
