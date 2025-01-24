import numpy as np
import scipy.stats

# Binomial Test Analysis Script
# This script performs a binomial test analysis to calculate the p-value.

# Input data
z = [89, 90, 86, 80, 97, 81, 94, 82, 87, 93, 94, 84, 83, 78, 98]  
p = 0.75  # Threshold probability for the binomial test

# Filter elements not equal to 85
filtered_data = [value for value in z if value != 85]
print("Filtered data (not equal to 85):", filtered_data)

# Count total observations and observations greater than 85
n = len(filtered_data)
b = sum(value > 85 for value in filtered_data)
print("Total observations (n):", n)
print("Count of values > 85 (b):", b)

# Calculate p-value for the binomial test
# d = P(X ≤ b), a = P(X ≥ b), p_value = 2 * min(a, d)
d = scipy.stats.binom.cdf(b, n, 1 - p)  # CDF for values ≤ b
a = 1 - scipy.stats.binom.cdf(b - 1, n, 1 - p)  # Complement of CDF for values ≥ b
p_value = 2 * min(a, d)
print("P-value from the binomial test:", p_value)
