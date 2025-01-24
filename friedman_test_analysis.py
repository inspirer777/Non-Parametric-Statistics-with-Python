import pandas as pd
from scipy.stats import friedmanchisquare

# Friedman Test Analysis Script
# This script performs the Friedman test to compare distributions across multiple groups.

# Define datasets
x1 = (3, 4, 3)
x2 = (4, 3, 4)
x3 = (2, 2, 1)
x4 = (1, 1, 2)

# Combine datasets into a single list
X = [x1, x2, x3, x4]
print("Input Data (X):", X)

# Convert the data into a pandas DataFrame for better visualization
df = pd.DataFrame(X)
print("\nDataFrame Representation:")
print(df)

# Perform the Friedman test
stat, p = friedmanchisquare(x1, x2, x3, x4)
print("\nFriedman Test Results:")
print(f"Statistics = {stat:.3f}, p-value = {p:.3f}")

# Interpret the results
alpha = 0.05
if p > alpha:
    print("Interpretation: Same distributions (fail to reject H0)")
else:
    print("Interpretation: Different distributions (reject H0)")
