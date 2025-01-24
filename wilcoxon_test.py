import math
import statistics
import numpy as np
import scipy.stats

# Wilcoxon Signed-Rank Test Script
# This script performs the Wilcoxon signed-rank test on a given dataset.

# Input data
data = (0.11, 0.14, 0.16, 0.19, 0.26, 0.28, 0.33, 0.38, 0.38, 0.52, 0.58,
        0.62, 0.63, 0.76, 0.86, 0.87, 0.88, 0.91, 0.92, 0.94, 0.95, 1.01,
        1.15, 1.15, 1.19, 1)

# Perform the Wilcoxon signed-rank test (default parameters)
result_default = scipy.stats.wilcoxon(data)
print("Wilcoxon Test (default parameters):", result_default)

# Perform the Wilcoxon signed-rank test (custom parameters)
result_custom = scipy.stats.wilcoxon(data, y=None, zero_method='wilcox',
                                     correction=False, alternative='greater', mode='exact')
print("Wilcoxon Test (custom parameters):", result_custom)
