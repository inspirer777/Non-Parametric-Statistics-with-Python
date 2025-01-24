import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
from scipy import stats

import matplotlib.pyplot as plt
from scipy.stats import kstest


# scipy.stats.kstest(rvs, cdf, args=(), N=20, alternative='two-sided', mode='auto')


x= (0.621,0.503,0.203,0.477,0.710,0.581,0.329,0.480,0.554,0.382)
ks = stats.kstest(x, 'norm', alternative='greater')
print(ks)
#seaborn.ecdfplot(data=None, *, x=None, y=None, hue=None, weights=None, stat='proportion'
#, complementary=False, palette=None,
#  hue_order=None, hue_norm=None, log_scale=None, legend=True, ax=None, **kwargs)
import seaborn as sns

sns.ecdfplot(x)
plt.show()


       
