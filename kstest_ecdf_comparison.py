import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kstest

# Kolmogorov-Smirnov Test and ECDF Comparison Script
# This script compares two datasets using the Kolmogorov-Smirnov test and visualizes their ECDFs.

# Define datasets
x = (10.3, 11.2, 11.5, 11.9, 12.8)
y = (10.4, 11.8, 12.5, 12.6, 13.8, 13.9)

# Perform Kolmogorov-Smirnov test
ks_result = kstest(x, y)
print("Kolmogorov-Smirnov Test Results:")
print(f"Statistic: {ks_result.statistic:.4f}, p-value: {ks_result.pvalue:.4f}")

# Visualize ECDFs for both datasets
plt.figure(figsize=(8, 5))
sns.ecdfplot(x, stat="proportion", label="Dataset X", color="blue")
sns.ecdfplot(y, stat="proportion", label="Dataset Y", color="red")

# Add labels and title
plt.title("Empirical Cumulative Distribution Function (ECDF) Comparison")
plt.xlabel("Values")
plt.ylabel("Proportion")
plt.legend()
plt.grid(True)
plt.show()
