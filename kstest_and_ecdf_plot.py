import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kstest, norm

# Kolmogorov-Smirnov Test and Empirical CDF Plot Script
# This script performs a Kolmogorov-Smirnov test and visualizes the empirical cumulative distribution function (ECDF).

# Define the dataset
x = (0.621, 0.503, 0.203, 0.477, 0.710, 0.581, 0.329, 0.480, 0.554, 0.382)

# Perform Kolmogorov-Smirnov test
# Test the data against the null hypothesis that it follows a normal distribution
ks = kstest(x, 'norm', alternative='greater')
print("Kolmogorov-Smirnov Test Results:")
print(f"Statistic: {ks.statistic:.4f}, p-value: {ks.pvalue:.4f}")

# Visualize the empirical cumulative distribution function (ECDF)
plt.figure(figsize=(8, 5))
sns.ecdfplot(x, stat="proportion", complementary=False)
plt.title("Empirical Cumulative Distribution Function (ECDF)")
plt.xlabel("Data Values")
plt.ylabel("Proportion")
plt.grid(True)
plt.show()
